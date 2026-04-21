#!/usr/bin/env python3
"""檢查 lion-erp-schema-docs/tables 的 YAML 品質統計"""
import argparse
import yaml
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="tables", help="YAML 目錄（預設: tables）")
    args = parser.parse_args()

    yaml_dir = Path(args.input)
    if not yaml_dir.is_dir():
        print(f"錯誤：{yaml_dir} 不存在", file=sys.stderr)
        sys.exit(1)

    yaml_files = sorted(yaml_dir.glob("*.yaml"))

    total_tables = len(yaml_files)
    total_cols = 0
    cols_unknown_type = 0
    cols_with_pk = 0
    cols_with_fk = 0
    cols_with_fk_note = 0
    cols_nullable_info = 0

    tables_no_pk = []
    tables_unknown_type_all = []
    tables_no_module = []
    tables_no_aliases = []

    for yf in yaml_files:
        data = yaml.safe_load(yf.read_text(encoding="utf-8"))
        cols = data.get("columns", [])
        total_cols += len(cols)

        has_pk = False
        all_unknown = True
        for c in cols:
            if c.get("type") == "unknown":
                cols_unknown_type += 1
            else:
                all_unknown = False
            if c.get("pk"):
                cols_with_pk += 1
                has_pk = True
            if c.get("fk"):
                cols_with_fk += 1
            if c.get("fk_note"):
                cols_with_fk_note += 1
            if "nullable" in c:
                cols_nullable_info += 1

        if not has_pk:
            tables_no_pk.append(data["table"])
        if cols and all_unknown:
            tables_unknown_type_all.append(data["table"])
        if not data.get("module"):
            tables_no_module.append(data["table"])
        if not data.get("aliases"):
            tables_no_aliases.append(data["table"])

    print(f"=== Table 層級 ===")
    print(f"總 table 數: {total_tables}")
    print(f"待補 aliases 的 table: {len(tables_no_aliases)}")
    print(f"無 PK 標記的 table: {len(tables_no_pk)}")
    print(f"type 全為 unknown 的 table: {len(tables_unknown_type_all)}")
    print(f"無 module 的 table: {len(tables_no_module)}")
    print()
    print(f"=== 欄位層級 ===")
    print(f"總欄位數: {total_cols}")
    if total_cols:
        print(f"type=unknown 的欄位: {cols_unknown_type} ({cols_unknown_type*100//total_cols}%)")
    print(f"有 pk 標記: {cols_with_pk}")
    print(f"有 fk 標準化: {cols_with_fk}")
    print(f"有 fk_note 人工待補: {cols_with_fk_note}")
    print(f"有 nullable 資訊: {cols_nullable_info}")


if __name__ == "__main__":
    main()
