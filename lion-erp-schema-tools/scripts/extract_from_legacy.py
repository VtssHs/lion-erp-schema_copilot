#!/usr/bin/env python3
"""
ERP Schema 提取器（一次性遷移工具）
將現有 erp-schema skill 的 table md 檔轉換為：
  1. <output_dir>/tables/{table}.yaml  — SSOT YAML
  2. <output_dir>/schemas/{table}.md    — Copilot 索引友好 md

用法：
  python3 extract_from_legacy.py \
      --input  /path/to/erp-schema/tables \
      --output /path/to/lion-erp-schema-docs

此工具設計為一次性遷移使用。遷移完成後日常工作流為：
  改 tables/*.yaml → 跑 yaml_to_md.py → commit

設計原則：
  - 欄位分組（H3 title）直接丟掉，攤平成單一欄位清單
  - 無法解析的檔案整份 skip，記錄到 failed.log
  - FK 用最寬鬆的 regex 抓，抓不到就放 fk_note 讓人工補
  - 已棄用欄位區塊（3 欄 table）直接略過不解析
"""

import os
import re
import sys
import argparse
import yaml
from pathlib import Path
from collections import OrderedDict

# ============ 設定（會被 CLI 參數覆蓋） ============
INPUT_DIR = None
OUTPUT_YAML_DIR = None
OUTPUT_MD_DIR = None
LOG_DIR = None

# ============ 日誌 ============
failed_log = []      # 整份 skip 的檔案
warning_log = []     # 部分解析有問題但仍輸出的檔案


def log_fail(filename, reason):
    failed_log.append(f"{filename}\t{reason}")


def log_warn(filename, reason):
    warning_log.append(f"{filename}\t{reason}")


# ============ H1 解析：table_name + chinese_name ============
H1_PATTERN = re.compile(r"^#\s+(\w+)\s*[-–—]\s*(.+?)\s*$", re.MULTILINE)


def parse_h1(content, filename):
    m = H1_PATTERN.search(content)
    if not m:
        return None, None
    return m.group(1).strip(), m.group(2).strip()


# ============ 前置元資料解析 ============
# 模板 A: **模組**: xxx
# 模板 A: **主鍵**: `xxx`
META_A_PATTERNS = {
    "module":      re.compile(r"\*\*(?:模組|所屬模組)\*\*\s*[:：]\s*(.+?)(?:\n|  )", re.MULTILINE),
    "description": re.compile(r"\*\*用途\*\*\s*[:：]\s*(.+?)(?:\n|  )", re.MULTILINE),
    "pk":          re.compile(r"\*\*(?:主鍵|Primary Key)\*\*\s*[:：]\s*`?([^`\n]+?)`?(?:\s|$)", re.MULTILINE),
}

# 模板 B: | 項目 | 內容 | 的 table
META_B_ROW = re.compile(
    r"\|\s*\*{0,2}(Table 名稱|中文名稱|DB 系統|所屬模組|Primary Key|模組)\*{0,2}\s*\|\s*(.+?)\s*\|"
)


def parse_metadata(content, filename):
    """回傳 dict: module, database, pk, description"""
    meta = {"module": None, "database": None, "pk": None, "description": None}

    # 先試模板 A
    for key, pat in META_A_PATTERNS.items():
        m = pat.search(content)
        if m:
            val = m.group(1).strip().strip("`").strip()
            meta[key] = val

    # 再試模板 B（會覆蓋模板 A 的結果，因為模板 B 通常更完整）
    for m in META_B_ROW.finditer(content):
        key_raw = m.group(1).strip()
        val = m.group(2).strip().strip("`").strip()
        if val.startswith("**") and val.endswith("**"):
            val = val[2:-2].strip("`").strip()
        key_map = {
            "Table 名稱": None,   # 已從 H1 取得
            "中文名稱":   None,   # 已從 H1 取得
            "DB 系統":    "database",
            "所屬模組":   "module",
            "模組":       "module",
            "Primary Key": "pk",
        }
        mapped = key_map.get(key_raw)
        if mapped:
            meta[mapped] = val

    # pk 可能帶了描述，例如 "prod_prod (團號)" —— 只留 code
    if meta["pk"]:
        pk_m = re.match(r"^[\w_,\s]+", meta["pk"])
        if pk_m:
            meta["pk"] = pk_m.group(0).strip().rstrip(",")

    return meta


# ============ 欄位 table 解析（動態 header 映射） ============

# Header cell → 角色
HEADER_ROLE_MAP = {
    # name
    "欄位": "name", "欄位名": "name", "欄位名稱": "name", "Column": "name",
    # type
    "型態": "type", "型別": "type", "資料型別": "type", "資料型態": "type", "Type": "type",
    # description（主要）
    "說明": "desc", "資料說明": "desc", "Description": "desc",
    # chinese name（對我們來說也算描述的一部分）
    "中文名稱": "cname",
    # note / remark
    "備註": "note", "約束": "note", "Note": "note", "Remark": "note",
    # nullable
    "允許 NULL": "nullable", "Null": "nullable", "Nullable": "nullable", "必填": "required",
    # default
    "預設值": "default", "Default": "default",
    # pk / fk 獨立欄位
    "PK": "pk", "FK": "fk", "Key": "key", "Primary Key": "pk",
}


def classify_header(header_cells):
    """
    把 header cells 映射成角色 list，回傳：
      - roles: [role or None, ...]  （None 表示不認識）
      - 是否為合法的欄位 table
    判定：至少要有 name 角色；「中文名稱」出現次數不可大於 1。
    """
    roles = []
    for cell in header_cells:
        key = cell.strip().replace("*", "").strip("` ")
        role = HEADER_ROLE_MAP.get(key)
        roles.append(role)

    if "name" not in roles:
        return roles, False
    # 至少要有 desc 或 cname 其中一個（否則就是個無意義的 table）
    if "desc" not in roles and "cname" not in roles:
        return roles, False
    return roles, True


def strip_markdown_emphasis(text):
    """移除 **bold** 和 backtick"""
    text = text.strip()
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = text.strip("`").strip()
    return text


# FK 解析：寬鬆抓「FK → xxx.yyy」、「FK → xxx」、「FK → xxx (ATTR)」
FK_PATTERN_FULL   = re.compile(r"FK\s*(?:→|->|-->)\s*([A-Za-z]\w*)\.([A-Za-z]\w*)")
FK_PATTERN_TBL    = re.compile(r"FK\s*(?:→|->|-->)\s*([A-Za-z]\w*)(?:\s*\(([^)]+)\))?")


def parse_fk_from_note(note):
    """
    從備註欄文字抓 FK。
    回傳 (fk, fk_note)：
      - 解析成功：fk = "table.col" 或 "table"，fk_note = None
      - 解析失敗但像 FK：fk = None，fk_note = 原文片段
      - 完全不像 FK：fk = None，fk_note = None
    """
    if not note or "FK" not in note:
        return None, None

    # 1. 嘗試完整 table.col
    m = FK_PATTERN_FULL.search(note)
    if m:
        return f"{m.group(1)}.{m.group(2)}", None

    # 2. 嘗試 table + 可能的括號條件 (ATTR)
    m = FK_PATTERN_TBL.search(note)
    if m:
        table = m.group(1)
        cond = m.group(2)
        if cond:
            return None, f"FK → {table} ({cond.strip()})"
        else:
            return f"{table}", None

    # 3. 看起來像 FK 但無法標準化
    return None, note.strip()


def is_pk(note):
    if not note:
        return False
    note_norm = note.replace("*", "").strip().upper()
    return "PK" in note_norm.split() or "PRIMARY KEY" in note_norm


def clean_cell(cell):
    """清理 cell 內容：處理 <br> 換行、strip"""
    return cell.replace("<br>", " ").replace("<br/>", " ").replace("<br />", " ").strip()


def parse_column_row(row_cells, roles):
    """用 role mapping 解析一列 row"""
    if len(row_cells) != len(roles):
        return None

    # 先把 cell 依 role 分裝
    slots = {}  # role → list of values
    for cell, role in zip(row_cells, roles):
        if role is None:
            continue
        slots.setdefault(role, []).append(clean_cell(cell))

    name_raw = slots.get("name", [""])[0]
    name = strip_markdown_emphasis(name_raw)
    if not name or not re.match(r"^\w+$", name):
        return None

    col = OrderedDict()
    col["name"] = name

    # type
    type_raw = slots.get("type", [""])[0] if slots.get("type") else ""
    col["type"] = (strip_markdown_emphasis(type_raw).lower() or "unknown")

    # nullable
    nullable_raw = slots.get("nullable", [""])[0] if slots.get("nullable") else ""
    required_raw = slots.get("required", [""])[0] if slots.get("required") else ""
    if nullable_raw:
        nv = nullable_raw.strip().upper()
        if nv in ("NO", "N", "NOT NULL"):
            col["nullable"] = False
        elif nv in ("YES", "Y", "NULL"):
            col["nullable"] = True
    elif required_raw:
        rv = required_raw.strip().upper()
        if rv == "Y":
            col["nullable"] = False
        elif rv == "N":
            col["nullable"] = True

    # description：desc + cname 合併
    desc_parts = []
    cname = strip_markdown_emphasis(slots.get("cname", [""])[0]) if slots.get("cname") else ""
    dtext = strip_markdown_emphasis(slots.get("desc", [""])[0]) if slots.get("desc") else ""
    if cname and dtext and cname != dtext:
        description = f"{cname}。{dtext}"
    else:
        description = cname or dtext or ""

    # note
    note_raw = slots.get("note", [""])[0] if slots.get("note") else ""

    # pk：可能在獨立欄位或藏在 note
    pk_raw = slots.get("pk", [""])[0] if slots.get("pk") else ""
    if pk_raw:
        if pk_raw.strip() in ("✓", "Y", "YES", "PK", "1", "true", "True"):
            col["pk"] = True
    if not col.get("pk") and is_pk(note_raw):
        col["pk"] = True

    # fk：獨立欄位優先
    fk_raw = slots.get("fk", [""])[0] if slots.get("fk") else ""
    fk_source = None
    if fk_raw and fk_raw.strip() not in ("", "—", "-", "✓"):
        fk_source = fk_raw
    elif "FK" in note_raw:
        fk_source = note_raw

    if fk_source:
        fk, fk_note = parse_fk_from_note(fk_source)
        if fk:
            col["fk"] = fk
        elif fk_note:
            col["fk_note"] = fk_note

    col["description"] = description

    # 處理 note 剩餘部分（扣掉 PK/FK 資訊）
    if note_raw:
        note_clean = note_raw
        note_clean = re.sub(r"\*\*PK\*\*|Primary Key|\bPK\b", "", note_clean, flags=re.IGNORECASE)
        note_clean = re.sub(r"FK\s*(?:→|->|-->)\s*[\w\.\s\(\)/]+", "", note_clean)
        note_clean = note_clean.strip(", ，").strip()
        if note_clean and note_clean != "—" and note_clean != "-":
            col["note"] = note_clean

    # default
    default_raw = slots.get("default", [""])[0] if slots.get("default") else ""
    if default_raw and default_raw.strip() not in ("", "-", "—", "N/A"):
        col["default"] = default_raw.strip()

    return col


def extract_columns(content, filename):
    """
    從 md 內容抓所有欄位。
    策略：找所有 markdown table，用 classify_header 判斷是不是「欄位 table」。
    「已棄用欄位」區塊的內容會被 skip。
    """
    lines = content.split("\n")
    columns = []
    seen_names = set()
    in_deprecated_section = False

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 偵測「已棄用欄位」區塊
        if re.match(r"^#{2,4}\s*已棄用", line) or re.match(r"^#{2,4}\s*(?:棄用|deprecated)", line, re.IGNORECASE):
            in_deprecated_section = True
            i += 1
            continue

        # 遇到下一個 H2/H3 重設 flag
        if re.match(r"^#{2,3}\s", line) and not re.match(r"^#{2,4}\s*已棄用", line):
            in_deprecated_section = False

        # 找 markdown table header
        if line.startswith("|") and line.endswith("|") and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if re.match(r"^\|[\s\-:|]+\|$", next_line):
                header_cells = [c.strip() for c in line.strip("|").split("|")]
                roles, is_col_table = classify_header(header_cells)
                if is_col_table and not in_deprecated_section:
                    j = i + 2
                    while j < len(lines) and lines[j].strip().startswith("|") and lines[j].strip().endswith("|"):
                        row_line = lines[j].strip()
                        row_cells = [c for c in row_line.strip("|").split("|")]
                        col = parse_column_row(row_cells, roles)
                        if col:
                            if col["name"] not in seen_names:
                                seen_names.add(col["name"])
                                columns.append(col)
                        j += 1
                    i = j
                    continue
        i += 1

    return columns


# ============ 主流程：單檔處理 ============

def process_file(md_path):
    """
    處理一份 md。
    成功回傳 (yaml_dict, md_content_str)
    失敗回傳 None 並記錄到 failed_log
    """
    filename = md_path.name
    try:
        content = md_path.read_text(encoding="utf-8")
    except Exception as e:
        log_fail(filename, f"read error: {e}")
        return None

    # 1. 解析 H1
    table_name, chinese_name = parse_h1(content, filename)
    if not table_name:
        log_fail(filename, "no H1 found")
        return None

    # 2. 解析 metadata
    meta = parse_metadata(content, filename)

    # 3. 抓欄位
    columns = extract_columns(content, filename)
    if not columns:
        log_fail(filename, "no columns extracted")
        return None

    # 4. 組 YAML dict
    yaml_obj = OrderedDict()
    yaml_obj["table"] = table_name
    yaml_obj["database"] = meta["database"] or "LionGroupERP"  # 預設
    yaml_obj["module"] = meta["module"] or ""
    yaml_obj["aliases"] = []  # 留給人工補
    yaml_obj["description"] = chinese_name if not meta["description"] else f"{chinese_name}。{meta['description']}"
    yaml_obj["columns"] = columns

    # 5. 處理 pk：優先用 metadata 裡的，若 columns 裡已有 pk=True 則不動
    has_pk_marked = any(c.get("pk") for c in columns)
    if not has_pk_marked and meta["pk"]:
        pk_names = [p.strip() for p in re.split(r"[,，]", meta["pk"])]
        for col in columns:
            if col["name"] in pk_names:
                col["pk"] = True

    return yaml_obj


# ============ YAML 輸出 ============

class LiteralStr(str):
    pass


def represent_ordereddict(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())


def represent_str(dumper, data):
    # 多行字串用 literal block
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(OrderedDict, represent_ordereddict)
yaml.add_representer(str, represent_str)


def dump_yaml(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(obj, f, allow_unicode=True, sort_keys=False, width=120)


# ============ Copilot 友好 MD 輸出 ============

def render_copilot_md(yaml_obj):
    """把 yaml_obj render 成 Copilot 索引友好的 md。
    此格式必須與 yaml_to_md.py 的 render_md 完全一致，
    這樣遷移完第一次跑 yaml_to_md.py 時不會產生無意義的 diff。"""
    lines = []
    table = yaml_obj["table"]
    desc = yaml_obj.get("description", "")

    if desc:
        lines.append(f"# {table} — {desc}")
    else:
        lines.append(f"# {table}")
    lines.append("")

    aliases = yaml_obj.get("aliases") or []
    if aliases:
        lines.append(f"**Aliases**: {', '.join(aliases)}")
    else:
        lines.append(f"**Aliases**: (尚未補)")
    lines.append(f"**Database**: {yaml_obj.get('database', '')}")
    lines.append(f"**Module**: {yaml_obj.get('module', '')}")
    lines.append("")

    lines.append("## Columns")
    lines.append("")
    lines.append("| Column | Type | Null | Key | FK | Description |")
    lines.append("|--------|------|------|-----|-----|-------------|")
    for col in yaml_obj["columns"]:
        name = col["name"]
        ctype = col.get("type", "")
        if "nullable" in col:
            null_mark = "NULL" if col["nullable"] else "NOT NULL"
        else:
            null_mark = "—"
        key = "PK" if col.get("pk") else "—"
        fk = col.get("fk") or col.get("fk_note") or "—"
        d = col.get("description", "") or ""
        d = d.replace("|", "\\|").replace("\n", " ")
        note = col.get("note")
        if note:
            note_escaped = note.replace("|", "\\|").replace("\n", " ")
            d = f"{d}（{note_escaped}）" if d else note_escaped
        lines.append(f"| {name} | {ctype} | {null_mark} | {key} | {fk} | {d} |")

    lines.append("")
    return "\n".join(lines)


# ============ main ============

def main():
    parser = argparse.ArgumentParser(description="遷移舊版 erp-schema md 到 YAML + Copilot md")
    parser.add_argument("--input",  required=True, help="舊版 erp-schema/tables 目錄（含 *.md）")
    parser.add_argument("--output", required=True, help="輸出 repo 根目錄（會建 tables/、schemas/、logs/）")
    args = parser.parse_args()

    global INPUT_DIR, OUTPUT_YAML_DIR, OUTPUT_MD_DIR, LOG_DIR
    INPUT_DIR       = Path(args.input)
    OUTPUT_YAML_DIR = Path(args.output) / "tables"
    OUTPUT_MD_DIR   = Path(args.output) / "schemas"
    LOG_DIR         = Path(args.output) / "logs"

    if not INPUT_DIR.is_dir():
        print(f"錯誤：輸入目錄不存在: {INPUT_DIR}", file=sys.stderr)
        sys.exit(1)

    OUTPUT_YAML_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(INPUT_DIR.glob("*.md"))
    print(f"Found {len(md_files)} md files in {INPUT_DIR}")

    success = 0
    failed = 0
    total_columns = 0
    fk_parsed = 0
    fk_note_only = 0

    for md_path in md_files:
        result = process_file(md_path)
        if result is None:
            failed += 1
            continue

        table = result["table"]
        dump_yaml(result, OUTPUT_YAML_DIR / f"{table}.yaml")
        md_str = render_copilot_md(result)
        (OUTPUT_MD_DIR / f"{table}.md").write_text(md_str, encoding="utf-8")

        success += 1
        total_columns += len(result["columns"])
        for col in result["columns"]:
            if col.get("fk"):
                fk_parsed += 1
            elif col.get("fk_note"):
                fk_note_only += 1

    (LOG_DIR / "failed.log").write_text("\n".join(failed_log) or "(none)", encoding="utf-8")
    (LOG_DIR / "warnings.log").write_text("\n".join(warning_log) or "(none)", encoding="utf-8")

    print(f"\n=== 提取結果 ===")
    print(f"成功: {success}")
    print(f"失敗: {failed}")
    print(f"總欄位數: {total_columns}")
    print(f"FK 成功標準化: {fk_parsed}")
    print(f"FK 只能保留原文（fk_note）: {fk_note_only}")
    print(f"\n輸出目錄:")
    print(f"  YAML:       {OUTPUT_YAML_DIR}")
    print(f"  Copilot md: {OUTPUT_MD_DIR}")
    print(f"  Logs:       {LOG_DIR}")


if __name__ == "__main__":
    main()
