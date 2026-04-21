#!/usr/bin/env python3
"""
seed_aliases.py — 從舊版 erp-schema md 自動抽 aliases 填進 YAML

讀舊 md 的 H1、模組、用途段落，抽出建議的 aliases，直接寫進
lion-erp-schema-docs/tables/{table}.yaml 的 aliases 欄位。

設計原則：
  - H1 中文標題 → 永遠保留（這是 table 正式名）
  - 英文變體（大寫 + 小寫 + 原名）→ 永遠保留
  - 模組名 → 保留但會進入頻率過濾
  - 用途段落關鍵字 → 保留但會進入頻率過濾
  - 全域出現 ≥ N 張的泛詞 → 自動剔除（預設 N=5）

用法：
  python3 seed_aliases.py \
      --legacy   /path/to/old-erp-schema/tables \
      --yaml-dir /path/to/lion-erp-schema-docs/tables \
      [--threshold 5] \
      [--dry-run]

安全措施：
  - 只會補「空 aliases」的 YAML；若 aliases 已有內容則 skip
  - --dry-run 只印預覽不改檔
  - 會產出 logs/alias_seeding_report.md 記錄每張 table 最終收了什麼、剔除了什麼
"""

import argparse
import re
import sys
import yaml
from pathlib import Path
from collections import Counter, OrderedDict


# ============ 從舊 md 抽 alias 候選 ============

H1_PATTERN = re.compile(r"^#\s+(\w+)\s*[-–—]\s*(.+?)\s*$", re.MULTILINE)

# 模板 A 元資料
META_A_MODULE = re.compile(r"\*\*(?:模組|所屬模組)\*\*\s*[:：]\s*(.+?)(?:\n|  )", re.MULTILINE)
META_A_PURPOSE = re.compile(r"\*\*用途\*\*\s*[:：]\s*(.+?)(?:\n|  )", re.MULTILINE)

# 模板 B 元資料（table 格式）
META_B_ROW = re.compile(r"\|\s*\*{0,2}([^|*]+?)\*{0,2}\s*\|\s*(.+?)\s*\|")

# 模板 C (表格概述用 bullet)
META_C_PURPOSE = re.compile(r"[-*]\s*\*\*用途\*\*[:：]\s*(.+)")
META_C_MODULE  = re.compile(r"[-*]\s*\*\*所屬模組\*\*[:：]\s*(.+)")

# 用途說明區塊（iscpm00 那種）
PURPOSE_SECTION = re.compile(
    r"##\s*(?:🎯\s*)?用途說明\s*\n(.+?)(?=\n##|\Z)", re.DOTALL
)


def strip_noise(text):
    """清掉 markdown 語法雜訊"""
    if not text:
        return ""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = text.replace("（", "(").replace("）", ")")
    return text.strip()


def extract_chinese_name(h1_title):
    """從 H1 '團體主檔' / '公司主檔（供應商主檔）' 抽出主名和副名"""
    # 去掉括號部分和括號內容
    main = re.sub(r"[(（].+?[)）]", "", h1_title).strip()
    # 但也把括號內的東西單獨收
    extras = re.findall(r"[(（]([^()（）]+)[)）]", h1_title)
    return main, extras


def extract_module(content):
    """抽模組名"""
    for pat in (META_A_MODULE, META_C_MODULE):
        m = pat.search(content)
        if m:
            return strip_noise(m.group(1))

    # 模板 B table
    for m in META_B_ROW.finditer(content):
        key = strip_noise(m.group(1))
        if key in ("所屬模組", "模組"):
            val = strip_noise(m.group(2))
            if val:
                return val
    return None


def extract_purpose(content):
    """抽用途描述"""
    for pat in (META_A_PURPOSE, META_C_PURPOSE):
        m = pat.search(content)
        if m:
            return strip_noise(m.group(1))

    m = PURPOSE_SECTION.search(content)
    if m:
        return strip_noise(m.group(1))[:200]  # 只取前 200 字

    # 模板 B table
    for m in META_B_ROW.finditer(content):
        key = strip_noise(m.group(1))
        if key in ("用途",):
            return strip_noise(m.group(2))
    return None


def simplify_module_name(module_raw):
    """
    把模組名簡化成 alias 候選。
    例：'團體產品系統 (Group Product)' → ['團體產品系統']
    '團體產品管理 (TPPDM) — 郵輪子系統' → ['團體產品管理', '郵輪子系統']
    'TPPDM (標準團名管理)' → ['標準團名管理']
    'BOOKM(預訂管理)' → ['預訂管理']
    """
    if not module_raw:
        return []
    text = module_raw.strip()

    # 如果整串是「英文代號 + 括號內中文說明」的格式，優先取括號內的中文
    # 例：'TPPDM (標準團名管理)' → '標準團名管理'
    m = re.match(r"^([A-Za-z0-9_]+)\s*[(（]([^)）]+)[)）]\s*$", text)
    if m:
        inner = m.group(2).strip()
        if re.search(r"[\u4e00-\u9fff]", inner):
            return [inner]

    # 去括號內英文代號（保留中文括號內容）
    def _strip_english_paren(match):
        inner = match.group(1).strip()
        if re.match(r"^[A-Za-z0-9_\s]+$", inner):
            return ""
        return match.group(0)

    cleaned = re.sub(r"[(（]([^)）]*)[)）]", _strip_english_paren, text)

    # 切斷破折號和各種分隔符
    parts = re.split(r"\s*[—–]\s*|\s+[-]\s+", cleaned)

    results = []
    for p in parts:
        p = strip_noise(p).strip()
        if not p:
            continue
        # 去掉純英文
        if re.match(r"^[A-Za-z0-9_\s]+$", p):
            continue
        # 去掉殘留的括號
        p = re.sub(r"[(（][^)）]*[)）]", "", p).strip()
        if p and re.search(r"[\u4e00-\u9fff]", p):
            results.append(p)
    return results


# 停用詞（太短、太泛、或純連接詞/助詞片段）
STOPWORDS = {
    # 功能詞
    "資料", "系統", "記錄", "用途", "說明", "本表", "目前", "主要", "必要", "基本",
    "一般", "共通", "相關", "各種", "所有", "其他", "等等", "或者", "以及",
    "典型用途", "核心代碼主檔", "基礎代碼主檔",
    # 連接詞/助詞片段
    "的關係", "是整個系統", "被訂單", "分類的根基", "透過序號區分",
    "提供下拉選單", "補充", "包含姓名", "包含航班", "的航班資料",
    "會計入帳", "訂單處理流程", "訂單業績計算",
    # 英文/技術
    "TABLE", "Table", "table", "Primary", "Key",
}

# 業務實體的命名規則：關鍵字必須以這些詞為結尾才被視為有效
VALID_ENTITY_SUFFIXES = (
    "主檔", "副檔", "明細檔", "明細", "關聯檔", "對照檔", "設定檔", "暫存檔",
    "檔", "表", "統計表", "記錄檔", "log檔",
)


def is_valid_entity_name(text):
    """判斷一個詞是否像業務實體名"""
    if not text or text in STOPWORDS:
        return False
    if len(text) < 2 or len(text) > 12:
        return False
    return text.endswith(VALID_ENTITY_SUFFIXES)


def extract_keywords_from_purpose(purpose_text):
    """
    從用途段落抽關鍵字。
    策略：只收以「主檔/副檔/明細檔/檔/表」結尾的業務實體名。
    """
    if not purpose_text:
        return []

    # 去掉括號內容
    text = re.sub(r"[(（][^)）]*[)）]", "", purpose_text)
    # 切成短句
    segments = re.split(r"[，。、,.;；\n\s]+", text)

    candidates = []
    for seg in segments:
        seg = seg.strip()
        if not seg:
            continue
        # 只留中文字符
        chinese_part = re.sub(r"[^\u4e00-\u9fff]", "", seg)
        if not chinese_part:
            continue

        # 必須通過業務實體檢查
        if is_valid_entity_name(chinese_part):
            candidates.append(chinese_part)

    return candidates


def extract_aliases_from_md(md_path):
    """
    從一份舊 md 抽所有 alias 候選，依類別分開回傳。
    回傳 dict:
      - h1_main:    H1 主標題 [str]
      - h1_extra:   H1 括號內的額外名稱 [str]
      - module:     模組名衍生 [str]
      - keywords:   用途關鍵字 [str]
      - english:    英文變體 [str]
      - table_name: table 英文名（用來產英文變體）
    """
    content = md_path.read_text(encoding="utf-8")
    h1_match = H1_PATTERN.search(content)
    if not h1_match:
        return None

    table_name = h1_match.group(1).strip()
    h1_title = h1_match.group(2).strip()
    main_name, extras = extract_chinese_name(h1_title)

    module_raw = extract_module(content)
    module_aliases = simplify_module_name(module_raw) if module_raw else []

    purpose = extract_purpose(content)
    keywords = extract_keywords_from_purpose(purpose)

    # 英文變體
    english = []
    english.append(table_name)                    # tppdm10
    if table_name.lower() != table_name:
        english.append(table_name.lower())        # tppdm10
    # 大寫去字首 'tp'/'is'/'op' 等常見 prefix 後剩下的名（例如 tppdm10 → PDM10）
    m = re.match(r"^(tp|is|op|ss|wt|bk|ex|gi|cr|bo)(\w+)$", table_name, re.IGNORECASE)
    if m:
        short = m.group(2).upper()
        if short and short not in english:
            english.append(short)
    # 全大寫版
    upper = table_name.upper()
    if upper not in english:
        english.append(upper)

    return {
        "table_name": table_name,
        "h1_main": [main_name] if main_name else [],
        "h1_extra": extras,
        "module": module_aliases,
        "keywords": keywords,
        "english": english,
    }


# ============ 頻率過濾 ============

def filter_by_frequency(alias_candidates_per_table, threshold):
    """
    統計每個 alias 出現在幾張 table，回傳「泛詞黑名單」。
    H1 主名和 table 原名不列入黑名單。
    但「英文縮寫去前綴版」若跨 table 衝突（>= 2 張）也會進黑名單，
    避免 TBM00 同時指向 istbm00 和 tptbm00 這種情況。
    """
    freq = Counter()
    english_short_freq = Counter()

    for table_name, cats in alias_candidates_per_table.items():
        # 模組 + 關鍵字的頻率（原本邏輯）
        for alias in cats["module"] + cats["keywords"]:
            freq[alias] += 1
        # 英文去前綴縮寫也要統計（只統計「非原名」「非全大寫」的那個）
        # english list 順序：[table_name, lower_name?, short_upper?, full_upper]
        original_lower = cats["table_name"].lower()
        original_upper = cats["table_name"].upper()
        for eng in cats["english"]:
            if eng.lower() != original_lower and eng != original_upper:
                english_short_freq[eng] += 1

    blacklist = {alias for alias, count in freq.items() if count >= threshold}
    # 英文短縮寫只要 >= 2 就衝突
    english_blacklist = {e for e, c in english_short_freq.items() if c >= 2}

    return blacklist, freq, english_blacklist, english_short_freq


def finalize_aliases(cats, blacklist, english_blacklist):
    """套用黑名單，產出最終的 aliases list（去重且保序）"""
    final = []
    seen = set()

    # 1. H1 主名（永遠保留）
    for a in cats["h1_main"]:
        if a and a not in seen:
            final.append(a)
            seen.add(a)

    # 2. H1 括號內補充
    for a in cats["h1_extra"]:
        if a and a not in seen:
            final.append(a)
            seen.add(a)

    # 3. 模組（黑名單過濾）
    for a in cats["module"]:
        if a and a not in seen and a not in blacklist:
            final.append(a)
            seen.add(a)

    # 4. 用途關鍵字（黑名單過濾）
    for a in cats["keywords"]:
        if a and a not in seen and a not in blacklist:
            final.append(a)
            seen.add(a)

    # 5. 英文變體（衝突黑名單過濾）
    original_lower = cats["table_name"].lower()
    original_upper = cats["table_name"].upper()
    for a in cats["english"]:
        if not a or a in seen:
            continue
        # 原名和全大寫永遠保留
        if a.lower() == original_lower or a == original_upper:
            final.append(a)
            seen.add(a)
            continue
        # 去前綴縮寫如果衝突就剔除
        if a in english_blacklist:
            continue
        final.append(a)
        seen.add(a)

    return final


# ============ YAML 讀寫（保持順序與格式一致） ============

class Represented(dict):
    pass


def _ordered_dict_representer(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())


def _str_representer(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(OrderedDict, _ordered_dict_representer)
yaml.add_representer(str, _str_representer)


def load_yaml_ordered(path):
    """用 safe_load 讀，但用 OrderedDict 保持欄位順序（Python 3.7+ dict 已保序）"""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def dump_yaml_ordered(data, path):
    # 把 dict 轉回 OrderedDict 以用 custom representer
    def convert(obj):
        if isinstance(obj, dict):
            return OrderedDict((k, convert(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return [convert(x) for x in obj]
        return obj

    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(convert(data), f, allow_unicode=True, sort_keys=False, width=120)


# ============ main ============

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--legacy",   required=True, help="舊版 erp-schema/tables 目錄（*.md）")
    parser.add_argument("--yaml-dir", required=True, help="lion-erp-schema-docs/tables 目錄（*.yaml）")
    parser.add_argument("--threshold", type=int, default=5,
                        help="黑名單門檻：出現在幾張以上 table 的詞會被剔除（預設 5）")
    parser.add_argument("--report", default=None,
                        help="報告輸出路徑（預設：<yaml-dir>/../logs/alias_seeding_report.md）")
    parser.add_argument("--dry-run", action="store_true", help="只預覽不寫檔")
    parser.add_argument("--force", action="store_true",
                        help="連已有 aliases 的 YAML 也覆寫（預設 skip）")
    args = parser.parse_args()

    legacy_dir = Path(args.legacy)
    yaml_dir = Path(args.yaml_dir)

    if not legacy_dir.is_dir():
        print(f"錯誤：{legacy_dir} 不存在", file=sys.stderr)
        sys.exit(1)
    if not yaml_dir.is_dir():
        print(f"錯誤：{yaml_dir} 不存在", file=sys.stderr)
        sys.exit(1)

    report_path = Path(args.report) if args.report else yaml_dir.parent / "logs" / "alias_seeding_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    # Step 1：掃所有舊 md，抽 alias 候選
    print("=== Step 1: 掃舊 md 抽 alias 候選 ===")
    candidates_per_table = {}
    skip_parse = []
    for md_path in sorted(legacy_dir.glob("*.md")):
        result = extract_aliases_from_md(md_path)
        if result is None:
            skip_parse.append(md_path.name)
            continue
        candidates_per_table[result["table_name"]] = result

    print(f"  處理 {len(candidates_per_table)} 張 table（skip 解析失敗: {len(skip_parse)}）")

    # Step 2：全域頻率統計與黑名單
    print(f"\n=== Step 2: 頻率過濾（門檻 {args.threshold} 張）===")
    blacklist, freq, english_blacklist, english_freq = filter_by_frequency(
        candidates_per_table, args.threshold
    )
    print(f"  中文黑名單: {len(blacklist)}")
    if blacklist:
        print(f"  被剔除的中文泛詞（出現 ≥ {args.threshold} 張）:")
        for alias in sorted(blacklist, key=lambda a: -freq[a]):
            print(f"    {alias} ({freq[alias]} 張)")
    print(f"  英文衝突黑名單: {len(english_blacklist)}")
    if english_blacklist:
        print(f"  被剔除的英文縮寫（跨 table 衝突）:")
        for e in sorted(english_blacklist, key=lambda a: -english_freq[a]):
            print(f"    {e} ({english_freq[e]} 張)")

    # Step 3：逐張 YAML 寫入 aliases
    print(f"\n=== Step 3: 寫入 YAML ===")
    written = 0
    skipped_has_alias = 0
    skipped_no_yaml = 0
    report_rows = []

    for table_name, cats in candidates_per_table.items():
        yaml_path = yaml_dir / f"{table_name}.yaml"
        if not yaml_path.exists():
            skipped_no_yaml += 1
            continue

        data = load_yaml_ordered(yaml_path)
        existing_aliases = data.get("aliases") or []

        if existing_aliases and not args.force:
            skipped_has_alias += 1
            continue

        final_aliases = finalize_aliases(cats, blacklist, english_blacklist)

        # 記錄被剔除的
        rejected = []
        for a in cats["module"] + cats["keywords"]:
            if a in blacklist:
                rejected.append(a)

        report_rows.append({
            "table": table_name,
            "final": final_aliases,
            "rejected": rejected,
        })

        if args.dry_run:
            print(f"  [dry-run] {table_name}: {final_aliases}")
        else:
            data["aliases"] = final_aliases
            dump_yaml_ordered(data, yaml_path)
            written += 1

    # Step 4：產報告
    report_lines = ["# Alias Seeding Report", ""]
    report_lines.append(f"- 處理 table 數: {len(candidates_per_table)}")
    report_lines.append(f"- 寫入 YAML: {written}")
    report_lines.append(f"- 跳過（已有 aliases）: {skipped_has_alias}")
    report_lines.append(f"- 跳過（無對應 YAML）: {skipped_no_yaml}")
    report_lines.append(f"- 黑名單門檻: 出現 ≥ {args.threshold} 張")
    report_lines.append("")

    report_lines.append(f"## 中文黑名單（{len(blacklist)} 個詞被剔除）")
    report_lines.append("")
    if blacklist:
        report_lines.append("| 詞 | 出現張數 |")
        report_lines.append("|---|---|")
        for alias in sorted(blacklist, key=lambda a: -freq[a]):
            report_lines.append(f"| {alias} | {freq[alias]} |")
    else:
        report_lines.append("（無）")
    report_lines.append("")

    report_lines.append(f"## 英文縮寫衝突黑名單（{len(english_blacklist)} 個縮寫跨 table 衝突）")
    report_lines.append("")
    if english_blacklist:
        report_lines.append("| 縮寫 | 衝突張數 |")
        report_lines.append("|---|---|")
        for e in sorted(english_blacklist, key=lambda a: -english_freq[a]):
            report_lines.append(f"| {e} | {english_freq[e]} |")
    else:
        report_lines.append("（無）")
    report_lines.append("")

    report_lines.append("## 各 table 收錄結果")
    report_lines.append("")
    for row in report_rows:
        report_lines.append(f"### {row['table']}")
        report_lines.append(f"- 最終 aliases: `{row['final']}`")
        if row["rejected"]:
            report_lines.append(f"- 被黑名單剔除: `{row['rejected']}`")
        report_lines.append("")

    if not args.dry_run:
        report_path.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"\n=== 完成 ===")
    print(f"  寫入: {written}")
    print(f"  已有 aliases 跳過: {skipped_has_alias}")
    print(f"  無對應 YAML 跳過: {skipped_no_yaml}")
    if args.dry_run:
        print(f"  [dry-run 模式，未實際寫檔]")
    else:
        print(f"  報告: {report_path}")


if __name__ == "__main__":
    main()
