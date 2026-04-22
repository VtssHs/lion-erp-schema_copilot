# Lion ERP Schema 使用指引

本 repo 是雄獅旅遊 ERP 資料庫(LionGroupERP)的 schema 文件。

---

## 觸發時機(Copilot 參考本指引的場景)

當使用者的問題包含以下任一情境時,**優先參考本 repo 的 schemas/ 與 indexes/**:

- **欄位/結構問題**:欄位名、型別、FK、PK、schema、table
- **業務物件查詢**:團號、訂單、估價、行程、旅客、配額、售價
- **SQL 生成請求**:「幫我寫 SQL」、「查詢」、「JOIN」、「如何撈」
- **Table 名 pattern**:`tppdm*`、`tppcm*`、`ssorm*`、`wtorm*`、`bookm*`、`istbm*`、`isbum*`、`tptbm*`、`tptrm*`、`iscpm*`、`ispfm*`、`optbm18`
- **影響範圍評估**:「改 X 會影響什麼」、「誰引用 X」

---

## 查詢場景路由

### 場景 A:正向查詢(知道 table 名 → 查欄位)

1. 優先從 `schemas/{table_name}.md` 取得資料
2. 每份 schema 的 H1 是 table 英文名與中文標題
3. **Aliases 區塊**列出該 table 的中文別名
4. **Columns 表格**是權威欄位清單,包含 Column / Type / Null / Key / FK / Description
5. FK 欄位格式為 `{table}` 或 `{table}.{column}`

### 場景 B:反向查詢(不知道 table 名 → 找 table)

當使用者問「哪張 table 存 X 資料」或「X 資料在哪裡」時:

1. 先參考 `domains/*.md` 的 Business Object 映射表(目前僅 `Code.md`)
2. 若 domain 文件未覆蓋,對 `schemas/` 目錄下所有檔案進行語意搜尋,比對 H1、Aliases 和 Description 欄位
3. 若找到可能對應的 table,列出 table 名並引用相關欄位說明

### 場景 C:影響範圍查詢(跨 table)

當使用者問「改 X 會影響哪些 table」、「誰引用 X」、「X 的 downstream」時:

1. **必讀** `indexes/fk_reverse.md` 找出所有引用 X 的 table + column
2. 以具體清單回答,禁止給出「可能會影響訂單相關 table」這種模糊答案
3. 若引用來自 `fk_note`(非標準化 FK),須標示「此關聯來自非標準化 FK,建議驗證」

### 場景 D:SQL 生成(含 JOIN)

產出任何 SQL 前,**必讀** `indexes/schema_quality.md` 檢查:

1. 目標 table 是否列在「type=unknown」清單 → 若是,回答加型別警示
2. 目標 table 是否列在「無 PK 標記」清單 → 若是,INSERT/UPDATE 前須詢問 PK
3. FK JOIN 是否涉及多型 FK(istbm00) → 若是,必須加 `tabl_type` 條件
4. FK 目標是否為外部 table → 查 `indexes/external_refs.md` 確認

### 場景 E:外部 table 引用

當使用者的查詢涉及 `opagm*`、`ophtm*`、`ctom*`、`gitpcm*`、`trip00` 等 repo 外部 table 時:

1. 查 `indexes/external_refs.md` 確認該 table 是否為已知外部引用
2. 禁止 hallucinate 欄位
3. 建議使用者查對應的 skill(`erp-schema`、`pcm-schema`、`trip-composer-schema`、`cms-schema`)

---

## 檔案優先順序

| 目的 | 第一順位 | 第二順位 |
|------|---------|---------|
| 欄位定義 | `schemas/*.md` | (勿讀 `tables/*.yaml`) |
| 業務映射 | `domains/*.md` | `schemas/*.md` 的 Aliases |
| 跨 table 引用 | `indexes/fk_reverse.md` | — |
| 資料品質檢查 | `indexes/schema_quality.md` | — |
| 外部引用驗證 | `indexes/external_refs.md` | — |

---

## 常見 Copilot 失誤(預防清單)

以下是已識別的失誤模式,產出前自我檢查:

1. **把 `fk_note` 當標準 FK 用**  
   看到 `fk_note: FK → istbm00 (ATTR)`,不可直接產出 `JOIN istbm00 ON ...`,必須加 `AND istbm00.tabl_type='ATTR'`。

2. **假設 `type=unknown` 的欄位可做算術**  
   `tppcm*` 系列欄位型別標 unknown,不可產出 `SUM(tp40_tot_amt)` 而不加警示。

3. **以 table 名規律推測不存在的 table**  
   看到 `tppdm10`、`tppdm11`,不可自行推論 `tppdm12` 的欄位。必須實際查 `schemas/`。

4. **用舊 description 生成 SQL 而忽略欄位語意**  
   例如 `tppdm11` description 寫「出團行程檔」,但欄位全為人數統計(HL/HK/KK)。應優先依欄位語意作答。

5. **Copilot 對 `bookm10` 的雙重定義困惑**  
   repo 標「團體訂單主檔(CTO 元件預訂)」,erp-schema skill 標「預訂旅客資料檔」。處理涉及 `bookm10` 的查詢時,必須先跟使用者確認用途。

---

## 禁止行為

- **若 `schemas/` 查無該 table,請直接回答「schema 文件未收錄此 table」**,不要自行推測欄位
- **不要根據 table 名稱的命名規律推測不存在的 table 或欄位**
- **不要從 `tables/*.yaml` 直接讀取資料**;以 `schemas/*.md` 為唯一欄位參考
- **SQL 查詢範例須根據 `schemas/` 實際欄位組出**,不要使用中文欄位名(如「估價代號」、「檔次」)作為欄位識別
- **本 repo 不收錄 LionGroupRPM(`gitpcm*` 等)及 LionGroupCMS 的 schema**,詢問這些 table 時請告知使用者並建議查對應 skill

---

## Scope 衝突的臨時處理

以下 3 張 table 的 YAML 標註為 `LionGroupRPM`,與 README Non-Scope 宣告衝突(團隊討論中):

- `bookm10`、`iscpm00`、`istbm00`

遇到這 3 張 table 的查詢:可照常回答,但須附註:「此 table 的 database 歸屬在團隊討論中,查詢結果以實際 DB 為準。」

---

## 補充說明

- 部分 table 的 `type` 欄位為 `unknown`,表示原始文件缺失。遇到此情況請告知使用者該欄位型別未知(詳見 `indexes/schema_quality.md`)
- 部分 FK 以 `fk_note` 格式記錄(如 `FK → istbm00 (ATTR)`),表示條件 FK 或多型 FK,請參考 `indexes/schema_quality.md` 的多型 FK 規則處理
- Domain 說明文件(`domains/*.md`)包含業務 object ↔ table 映射與 SQL 範例,可輔助回答涉及多張 table 的複合查詢
