#!/usr/bin/env python3
"""
YAML → Copilot Markdown Build Script

從 lion-erp-schema-docs 的 tables/*.yaml 重新產出 schemas/*.md。
這是日常工作流的核心：

    修改 tables/xxx.yaml  →  跑這個腳本  →  commit schemas/

用法（在 lion-erp-schema-docs repo 根目錄執行）：
    python3 scripts/yaml_to_md.py

或指定路徑：
    python3 yaml_to_md.py --input /path/to/tables --output /path/to/schemas

會做的驗證：
  - YAML 必填欄位檢查（table, columns）
  - FK 指向的 table 是否存在（若不存在會 warning）
  - 重複 table 檢查

退出狀態：
  0 = 成功
  1 = 有 validation error（CI 應該 fail）
"""

import argparse
import sys
import yaml
from pathlib import Path


# ============ YAML 讀取 ============

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ============ 驗證 ============

class ValidationError(Exception):
    pass


def validate_yaml(data, path):
    errors = []

    if not isinstance(data, dict):
        errors.append(f"{path.name}: 檔案內容不是 YAML dict")
        return errors

    if "table" not in data:
        errors.append(f"{path.name}: 缺少 table 欄位")

    if "columns" not in data or not isinstance(data.get("columns"), list):
        errors.append(f"{path.name}: 缺少 columns 或 columns 不是 list")

    # 檔名必須 = table name
    expected_name = path.stem
    if data.get("table") and data["table"] != expected_name:
        errors.append(f"{path.name}: table 欄位 '{data['table']}' 與檔名 '{expected_name}' 不符")

    # 每個 column 必須有 name
    for i, col in enumerate(data.get("columns", [])):
        if not isinstance(col, dict):
            errors.append(f"{path.name}: columns[{i}] 不是 dict")
            continue
        if not col.get("name"):
            errors.append(f"{path.name}: columns[{i}] 缺少 name")

    return errors


def validate_fk_targets(all_tables, all_table_names):
    """檢查所有 fk: x.y 裡的 x 是否存在。只 warning 不 error（FK 可能指向未收錄的 table）。"""
    warnings = []
    for table_name, data in all_tables.items():
        for col in data.get("columns", []):
            fk = col.get("fk")
            if not fk:
                continue
            # fk 格式：'table' 或 'table.column'
            fk_table = fk.split(".")[0]
            if fk_table not in all_table_names:
                warnings.append(f"{table_name}.{col['name']}: fk → {fk_table} (目標 table 未收錄)")
    return warnings


# ============ Render Markdown ============

def render_md(data):
    """把 YAML dict render 成 Copilot 友好的 md"""
    lines = []
    table = data["table"]
    desc = data.get("description", "")

    # H1
    if desc:
        lines.append(f"# {table} — {desc}")
    else:
        lines.append(f"# {table}")
    lines.append("")

    # 元資料
    aliases = data.get("aliases") or []
    if aliases:
        lines.append(f"**Aliases**: {', '.join(aliases)}")
    else:
        lines.append(f"**Aliases**: (尚未補)")
    lines.append(f"**Database**: {data.get('database', '')}")
    lines.append(f"**Module**: {data.get('module', '')}")
    lines.append("")

    # Columns
    lines.append("## Columns")
    lines.append("")
    lines.append("| Column | Type | Null | Key | FK | Description |")
    lines.append("|--------|------|------|-----|-----|-------------|")

    for col in data.get("columns", []):
        name = col["name"]
        ctype = col.get("type", "")

        # nullable
        if "nullable" in col:
            null_mark = "NULL" if col["nullable"] else "NOT NULL"
        else:
            null_mark = "—"

        # key
        key = "PK" if col.get("pk") else "—"

        # fk
        fk = col.get("fk") or col.get("fk_note") or "—"

        # description（處理 | 轉義和換行）
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
    parser = argparse.ArgumentParser(description="從 YAML SSOT 產出 Copilot 友好 Markdown")
    parser.add_argument("--input",  default="tables",  help="YAML 輸入目錄（預設: tables）")
    parser.add_argument("--output", default="schemas", help="Markdown 輸出目錄（預設: schemas）")
    parser.add_argument("--strict", action="store_true", help="FK warning 也當 error（CI 用）")
    args = parser.parse_args()

    input_dir  = Path(args.input)
    output_dir = Path(args.output)

    if not input_dir.is_dir():
        print(f"錯誤：輸入目錄不存在: {input_dir}", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. 載入所有 YAML
    yaml_files = sorted(input_dir.glob("*.yaml"))
    if not yaml_files:
        print(f"錯誤：{input_dir} 沒有 yaml 檔", file=sys.stderr)
        sys.exit(1)

    all_tables = {}
    all_errors = []

    for yf in yaml_files:
        try:
            data = load_yaml(yf)
        except yaml.YAMLError as e:
            all_errors.append(f"{yf.name}: YAML 解析失敗 — {e}")
            continue

        errors = validate_yaml(data, yf)
        if errors:
            all_errors.extend(errors)
            continue

        table_name = data["table"]
        if table_name in all_tables:
            all_errors.append(f"重複 table 名稱: {table_name}（{yf.name}）")
            continue
        all_tables[table_name] = data

    if all_errors:
        print("=== 驗證錯誤 ===", file=sys.stderr)
        for e in all_errors:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)

    # 2. FK 目標檢查（warning）
    fk_warnings = validate_fk_targets(all_tables, set(all_tables.keys()))
    if fk_warnings:
        print("=== FK 警告（目標 table 未收錄）===")
        for w in fk_warnings:
            print(f"  {w}")
        if args.strict:
            print("\n--strict 模式：FK warning 視為 error", file=sys.stderr)
            sys.exit(1)

    # 3. 清掉舊的 md（避免刪過的 YAML 留下孤兒 md）
    existing_md = set(f.stem for f in output_dir.glob("*.md"))
    current_yaml = set(all_tables.keys())
    orphans = existing_md - current_yaml
    for orphan in orphans:
        (output_dir / f"{orphan}.md").unlink()
        print(f"  刪除孤兒: {orphan}.md")

    # 4. 寫 md
    written = 0
    for table_name, data in all_tables.items():
        md_str = render_md(data)
        (output_dir / f"{table_name}.md").write_text(md_str, encoding="utf-8")
        written += 1

    # 5. 統計
    total_cols = sum(len(d.get("columns", [])) for d in all_tables.values())
    need_aliases = sum(1 for d in all_tables.values() if not d.get("aliases"))
    no_module = sum(1 for d in all_tables.values() if not d.get("module"))

    print(f"\n=== Build 完成 ===")
    print(f"  YAML 輸入:   {len(all_tables)}")
    print(f"  MD 寫入:     {written}")
    print(f"  孤兒 md 刪除: {len(orphans)}")
    print(f"  總欄位數:    {total_cols}")
    print(f"  FK warning:  {len(fk_warnings)}")
    print(f"  待補 aliases: {need_aliases} 張")
    print(f"  待補 module:  {no_module} 張")


if __name__ == "__main__":
    main()
