# lion-erp-schema-docs

雄獅旅遊 ERP 資料庫 schema 文件。供 GitHub Copilot Chat 索引使用。

## 給 RD 的使用方式

在你的專案 repo 裡加入 submodule：

```bash
git submodule add git@github.com:YOUR_ORG/lion-erp-schema-docs.git docs/erp-schema
git submodule update --init --recursive
```

之後在 GitHub Copilot Chat 裡：

- 直接問問題，Copilot 會從 workspace 索引找到 `docs/erp-schema/schemas/` 下的檔案。
- 需要精準引用時用：`#file:docs/erp-schema/schemas/tppdm10.md`
- 需要整個 schema 目錄：`#folder:docs/erp-schema/schemas`

查詢範例：

```
Q: 產品主檔的 gpno 是什麼型別？
Q: tppdm10 有哪些 FK？
Q: 哪張 table 存出團日期？
```

更新最新版：

```bash
git submodule update --remote docs/erp-schema
```

## 目錄結構

```
lion-erp-schema-docs/
├── tables/                 # YAML SSOT（人類編輯這裡）
│   ├── tppdm10.yaml
│   └── ... (106 份)
├── schemas/                # Copilot 索引友好 md（自動產生，勿手改）
│   ├── tppdm10.md
│   └── ... (106 份)
├── logs/
│   └── manual_todo.md      # 人工待補清單
├── .github/
│   ├── copilot-instructions.md  # Copilot 觸發指令
│   └── workflows/
│       └── build.yml       # CI：改 YAML 自動重生 md
└── README.md
```

## 工作流

```
改 tables/xxx.yaml  →  push  →  CI 自動重生 schemas/xxx.md  →  RD 的 submodule update 拿到最新
```

### 本地預覽

若要在 push 前預覽產出：

```bash
# 假設 lion-erp-schema-tools 在同一個父目錄
python3 ../lion-erp-schema-tools/scripts/yaml_to_md.py
git diff schemas/
```

工具 repo 在 [lion-erp-schema-tools](https://github.com/YOUR_ORG/lion-erp-schema-tools)。

## YAML 編輯指引

### 必填欄位

```yaml
table: tppdm10                # 必須與檔名一致
database: LionGroupERP
module: 團體產品系統
columns:
  - name: prod_prod           # 每個 column 至少要有 name
    type: varchar
    pk: true
    description: 團號
```

### 建議欄位：aliases

**這是 Copilot 檢索品質的命脈**，每張 table 至少補 2-3 個中文別名：

```yaml
aliases:
  - 產品主檔
  - 團體產品主檔
  - PDM10
```

當 RD 在 Copilot 問「產品主檔的 gpno 是什麼」，embedding 要能從「產品主檔」反查到 `tppdm10.md`，靠的就是 aliases。

### FK 格式

```yaml
# 標準：指向特定 table.column
fk: tppcm00.gpno

# 只指 table、不指欄位
fk: tppcm00

# 條件 FK / 多型 FK（自動標準化失敗時保留原文）
fk_note: FK → istbm00 (ATTR)
```

### 其他可選欄位

```yaml
columns:
  - name: prod_status
    type: char(1)
    nullable: false           # 可選
    default: 'A'              # 可選
    description: 狀態
    note: A=啟用 I=停用 D=刪除  # 可選，補充說明
```

## 驗證規則

CI 會檢查：

1. YAML 必填欄位（table、columns）
2. 檔名與 `table:` 欄位一致
3. 重複 table 名稱
4. FK 指向的 table 是否在 repo 內（嚴格模式下為 error，否則 warning）

本地驗證：

```bash
python3 ../lion-erp-schema-tools/scripts/yaml_to_md.py --strict
```

## 統計

- 106 張 table
- 1861 個欄位
- 134 個 FK 已標準化
- 60 個 FK 保留原文待人工標準化

詳見 `logs/manual_todo.md`。

## 禁止事項

- 不要直接改 `schemas/*.md` — 它會被 CI 覆寫。請改 `tables/*.yaml`。
- 不要手動新增 `schemas/` 下不對應 YAML 的孤兒 md — CI 會清掉。
- 不要把這個 repo 和 `lion-erp-schema-tools` 合併。SSOT 和工具分開維護是刻意的設計。
