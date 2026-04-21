#!/usr/bin/env python3
"""產出人工待補清單，方便後續批次補資料"""
import argparse
import yaml
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="tables", help="YAML 目錄（預設: tables）")
    parser.add_argument("--output", default="logs/manual_todo.md", help="輸出檔路徑")
    args = parser.parse_args()

    yaml_dir = Path(args.input)
    if not yaml_dir.is_dir():
        print(f"錯誤：{yaml_dir} 不存在", file=sys.stderr)
        sys.exit(1)

    yaml_files = sorted(yaml_dir.glob("*.yaml"))

    todo = {
        "無 aliases 待補": [],
        "無 module 需補": [],
        "無 PK 標記需確認": [],
        "type 全為 unknown": [],
        "有 fk_note 需人工標準化": [],
    }

    for yf in yaml_files:
        data = yaml.safe_load(yf.read_text(encoding="utf-8"))
        table = data["table"]
        cols = data.get("columns", [])

        if not data.get("aliases"):
            todo["無 aliases 待補"].append(table)
        if not data.get("module"):
            todo["無 module 需補"].append(table)
        if not any(c.get("pk") for c in cols):
            todo["無 PK 標記需確認"].append(table)
        if cols and all(c.get("type") == "unknown" for c in cols):
            todo["type 全為 unknown"].append(table)

        fk_notes = [(c["name"], c.get("fk_note")) for c in cols if c.get("fk_note")]
        if fk_notes:
            todo["有 fk_note 需人工標準化"].append((table, fk_notes))

    lines = ["# 人工待補清單", ""]
    lines.append("此清單由 `scripts/gen_todo.py` 自動產生。")
    lines.append("")

    lines.append(f"## 待補 aliases（{len(todo['無 aliases 待補'])} 張）")
    lines.append("")
    lines.append("**這是 Copilot 檢索品質的命脈。** 每張 table 補 2-3 個中文別名到 YAML 的 `aliases:` 欄位。")
    lines.append("")
    for t in todo["無 aliases 待補"]:
        lines.append(f"- [ ] {t}")
    lines.append("")

    lines.append(f"## 無 module 需補（{len(todo['無 module 需補'])} 張）")
    lines.append("")
    lines.append("原始 md 未標註模組，請補上 `module:` 欄位。")
    lines.append("")
    for t in todo["無 module 需補"]:
        lines.append(f"- [ ] {t}")
    lines.append("")

    lines.append(f"## 無 PK 標記需確認（{len(todo['無 PK 標記需確認'])} 張）")
    lines.append("")
    lines.append("這些 table 的欄位都沒標 PK，可能是：(a) 原始 md 遺漏、(b) 真的沒有單一 PK、(c) 複合 PK 但未標註。")
    lines.append("")
    for t in todo["無 PK 標記需確認"]:
        lines.append(f"- [ ] {t}")
    lines.append("")

    lines.append(f"## type 全為 unknown（{len(todo['type 全為 unknown'])} 張）")
    lines.append("")
    lines.append("這些 table 的原始 md 用了「欄位名稱 | 中文名稱 | 資料說明 | 備註」模板，根本沒有型別欄位。需要從 DB 或其他文件補型別。")
    lines.append("")
    for t in todo["type 全為 unknown"]:
        lines.append(f"- [ ] {t}")
    lines.append("")

    lines.append(f"## 有 fk_note 需人工標準化（{len(todo['有 fk_note 需人工標準化'])} 張 table）")
    lines.append("")
    lines.append("這些 FK 格式無法自動標準化，通常是多型 FK 或條件 FK（例如 `istbm00 (ATTR)`）。可考慮保留 `fk_note` 或轉成結構化 `fk` + `fk_condition`。")
    lines.append("")
    for table, notes in todo["有 fk_note 需人工標準化"]:
        lines.append(f"### {table}")
        for col_name, fk_note in notes:
            lines.append(f"- `{col_name}`: `{fk_note}`")
        lines.append("")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"人工待補清單已產出: {output_path}")
    print(f"  無 aliases: {len(todo['無 aliases 待補'])}")
    print(f"  無 module: {len(todo['無 module 需補'])}")
    print(f"  無 PK: {len(todo['無 PK 標記需確認'])}")
    print(f"  全 unknown: {len(todo['type 全為 unknown'])}")
    print(f"  fk_note 待補: {sum(len(n) for _, n in todo['有 fk_note 需人工標準化'])} 個欄位")


if __name__ == "__main__":
    main()
