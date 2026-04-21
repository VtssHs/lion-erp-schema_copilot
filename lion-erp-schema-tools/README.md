# lion-erp-schema-tools

雄獅 ERP Schema 文件的維護工具。配合 [lion-erp-schema-docs](../lion-erp-schema-docs) 使用。

## 角色分工

```
lion-erp-schema-docs     ← 文件 repo（RD submodule 引用）
    ├── tables/          ← YAML SSOT（人類編輯這裡）
    └── schemas/         ← Copilot 友好 md（自動產生）

lion-erp-schema-tools    ← 本 repo（PM 維護，RD 不需要）
    └── scripts/
        ├── extract_from_legacy.py  ← 一次性遷移工具
        ├── yaml_to_md.py            ← 日常 build script
        ├── check_quality.py
        └── gen_todo.py
```

## 安裝

```bash
pip install -r requirements.txt
```

## 日常工作流

改 YAML → 跑 build → commit：

```bash
# 在 lion-erp-schema-docs repo 根目錄執行
python3 ../lion-erp-schema-tools/scripts/yaml_to_md.py
git add schemas/
git commit -m "Update schema: tppdm10 aliases"
```

或將本 repo clone 到 docs repo 旁邊，然後用相對路徑。

## 腳本說明

### `scripts/yaml_to_md.py`

**這是日常最常用的腳本**。從 `tables/*.yaml` 重新產出 `schemas/*.md`。

```bash
# 預設：在 docs repo 根目錄執行，讀 tables/ 寫 schemas/
python3 scripts/yaml_to_md.py

# 指定路徑
python3 scripts/yaml_to_md.py --input /path/to/tables --output /path/to/schemas

# CI 嚴格模式：FK 指向未收錄的 table 也會 fail
python3 scripts/yaml_to_md.py --strict
```

會做的驗證：
- YAML 必填欄位（table、columns）
- 檔名必須與 `table:` 欄位一致
- 重複 table 名稱
- FK 指向的 table 是否在 repo 內（warning）

### `scripts/seed_aliases.py`

**一次性自動補 aliases 工具**。從舊版 `erp-schema` md 抽出 H1 中文名、模組名、用途關鍵字和英文變體，自動寫進 YAML 的 `aliases:` 欄位。

```bash
# dry-run 預覽（推薦先跑一次）
python3 scripts/seed_aliases.py \
    --legacy   /path/to/old-erp-schema/tables \
    --yaml-dir /path/to/lion-erp-schema-docs/tables \
    --dry-run

# 實際寫入
python3 scripts/seed_aliases.py \
    --legacy   /path/to/old-erp-schema/tables \
    --yaml-dir /path/to/lion-erp-schema-docs/tables
```

內建防污染機制：
- **中文黑名單**：出現在 ≥ 5 張 table 的泛詞自動剔除（預設門檻可用 `--threshold` 調整）
- **英文衝突黑名單**：去前綴縮寫若跨 table 衝突（如 TBM00 同時指 istbm00 和 tptbm00）自動剔除
- **安全預設**：只補空 aliases 的 YAML，已有內容的 skip（可用 `--force` 覆寫）
- 會產出 `logs/alias_seeding_report.md` 記錄每張 table 的收錄結果和黑名單

### `scripts/extract_from_legacy.py`

**一次性遷移工具**。把舊版 `erp-schema` skill 的 md 檔轉成 YAML + Copilot md。遷移完成後不再使用。

```bash
python3 scripts/extract_from_legacy.py \
    --input  /path/to/old-erp-schema/tables \
    --output /path/to/lion-erp-schema-docs
```

### `scripts/check_quality.py`

統計 YAML 品質：無 aliases、無 module、無 PK、unknown type 等。

```bash
python3 scripts/check_quality.py --input /path/to/tables
```

### `scripts/gen_todo.py`

產出人工待補清單 `logs/manual_todo.md`，列出所有需要人工補資料的 table。

```bash
python3 scripts/gen_todo.py --input /path/to/tables --output logs/manual_todo.md
```

## YAML schema 規格

每份 `tables/{table}.yaml` 的格式：

```yaml
table: tppdm10                        # 必填，須與檔名一致
database: LionGroupERP                # 必填
module: 團體產品系統                  # 必填
aliases:                              # 建議填（Copilot 檢索命脈）
  - 產品主檔
  - 團體產品主檔
  - PDM10
description: 團體主檔，一個出發日的團體資料

columns:                              # 必填
  - name: prod_prod                   # 必填
    type: varchar                     # 建議填
    pk: true                          # 可選
    description: 團號                 # 建議填
  - name: prod_gpno
    type: varchar(15)
    nullable: true                    # 可選
    fk: tppcm00.gpno                  # 可選，格式：{table}.{column} 或 {table}
    description: 團號
  - name: prod_obscure
    type: varchar
    fk_note: FK → istbm00 (ATTR)     # 無法標準化的 FK，保留原文
    description: 雜項
```

必填 vs 建議：
- **必填**：table / database / module / columns / columns[].name
- **建議**：aliases（Copilot 檢索命脈）/ type / description
- **可選**：pk / fk / fk_note / nullable / default / note
