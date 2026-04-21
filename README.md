# lion-erp-schema-docs

雄獅旅遊 ERP 資料庫 schema 文件。供 GitHub Copilot Chat 索引使用。

---

## 這個 Repo 是什麼（Primary Artifact）

**主要產出物**：`schemas/` 目錄下的 Markdown 檔案。

每個檔案描述 ERP 資料庫中的一張 table，格式固定、Copilot 可索引。  
RD 在開發過程中引用這些檔案，讓 Copilot Chat 能根據 table 的欄位定義、FK 關聯、業務說明，給出準確的 SQL 建議與欄位查詢。

---

## Scope / Non-Scope

### ✅ 在 Scope 內
- **LionGroupERP** 資料庫的 table schema（欄位定義、型別、FK、業務說明）
- 每張 table 的中文別名（供自然語言查詢命中用）
- Domain 說明文件（`domains/` 目錄）：business object ↔ table 映射、跨 table 關聯、常用 SQL 範例
- 自動 CI 流程：改 `tables/*.yaml` → 自動重生 `schemas/*.md`

### ❌ 不在 Scope 內
- **LionGroupRPM**（`gitpcm*` 系列）— 屬於獨立 repo，本 repo 不收錄
- **LionGroupCMS**（`cms-schema`）— 屬於獨立 repo
- API spec、ExAPI / INAPI 介面定義
- 應用程式商業邏輯（這裡只記 schema，不記程式流程）
- 已停用的 PCM 資料庫（PCM DB 已下線，`gitpcm*` 已遷移至 LionGroupRPM）

---

## 目錄結構

```
lion-erp-schema-docs/
├── tables/                 # YAML SSOT（人類編輯這裡）
│   ├── tppdm10.yaml
│   └── ... (106 份)
├── schemas/                # Copilot 索引友好 md（自動產生，勿手改）
│   ├── tppdm10.md
│   └── ... (106 份)
├── domains/                # Domain 說明（人類維護）
│   └── Code.md             # Code domain canonical 範例
├── logs/
│   ├── manual_todo.md      # 人工待補清單
│   └── alias_seeding_report.md
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/build.yml
└── README.md
```

---

## Domain 地圖

ERP 內的 table 依業務職責分為四個 domain：

| Domain | 主要 Tables | 說明 |
|---|---|---|
| **Code**（出發日管理） | `tppdm*`, `tppcm*` | 出發日建立、售價、配額、估價單 |
| **Itin**（行程管理） | `tptrm*`, `tptbm*` | 旅館群組、旅遊館、行程備註 |
| **Order**（訂單管理） | `ssorm*`, `bookm*` | 訂單主檔、旅客名單、收款 |
| **Cost**（財務/立帳） | `wtorm*` | 財務科目、立帳、結匯 |

基礎代碼/主檔（`istbm*`, `isbum*`, `iscpm*`, `ispfm*`, `optbm*`）為橫跨所有 domain 的公用參照表。

詳見 `domains/Code.md` 的 canonical 範例，其他 domain 文件陸續補充。

---

## 給 RD 的使用方式

在你的專案 repo 加入 submodule：

```bash
git submodule add git@github.com:VtssHs/lion-erp-schema-docs.git docs/erp-schema
git submodule update --init --recursive
```

在 GitHub Copilot Chat：

- 直接問問題，Copilot 會從 workspace 索引找到 `docs/erp-schema/schemas/` 下的檔案
- 需要精準引用單表：`#file:docs/erp-schema/schemas/tppdm10.md`
- 需要整個 schema 目錄：`#folder:docs/erp-schema/schemas`
- 需要 domain 說明與 table 關聯：`#file:docs/erp-schema/domains/Code.md`

**查詢範例**

```
Q: 產品主檔的 gpno 是什麼型別？          ← 正向查詢（知道 table 名）
Q: tppdm10 有哪些 FK？                    ← FK 關聯查詢
Q: 哪張 table 存出團日期？                ← 反向查詢（不知道 table 名）
Q: 配額扣減會動到哪些 tables？            ← 跨 table 影響查詢
Q: 幫我寫查某條線出發日清單的 SQL         ← SQL 生成（搭配 domains/Code.md）
```

更新最新版：

```bash
git submodule update --remote docs/erp-schema
```

---

## 工作流

```
改 tables/xxx.yaml  →  push  →  CI 自動重生 schemas/xxx.md  →  RD submodule update 拿到最新
```

### 本地預覽

```bash
python3 ../lion-erp-schema-tools/scripts/yaml_to_md.py
git diff schemas/
```

工具 repo：[lion-erp-schema-tools](https://github.com/VtssHs/lion-erp-schema-tools)

---

## YAML 編輯指引

### 必填欄位

```yaml
table: tppdm10
database: LionGroupERP
module: 團體產品系統
columns:
  - name: prod_prod
    type: varchar
    pk: true
    description: 團號
```

### aliases（Copilot 檢索命中率的命脈）

每張 table 至少補 2–3 個中文別名：

```yaml
aliases:
  - 產品主檔
  - 團體主檔
  - PDM10
```

### FK 格式

```yaml
fk: tppcm00.tp00_tpform        # 標準：指向 table.column
fk: tppcm00                    # 只指 table，不指欄位
fk_note: FK → istbm00 (ATTR)   # 條件 FK / 多型 FK
```

---

## 禁止事項

- 不要直接改 `schemas/*.md` — 會被 CI 覆寫
- 不要手動新增 `schemas/` 下沒有對應 YAML 的孤兒 md — CI 會清掉
- 不要把 `domains/*.md` 放入 `schemas/` — domains 是 domain 說明文件，不是 table schema

---

## 統計

- 106 張 table（LionGroupERP）
- 1861 個欄位
- 134 個 FK 已標準化
- 60 個 FK 保留原文待人工標準化

詳見 `logs/manual_todo.md`。
