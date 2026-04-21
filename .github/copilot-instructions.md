# Lion ERP Schema 使用指引

本 repo 是雄獅旅遊 ERP 資料庫（LionGroupERP）的 schema 文件。

## 目錄結構

- `tables/` — YAML 單一真相來源（SSOT）。**此目錄不作為 Copilot Chat 的參考來源**，請使用 `schemas/`。
- `schemas/` — Copilot 索引友好的 Markdown 檔，每張 table 一份。
- `domains/` — Domain 說明文件（業務 object ↔ table 映射、跨 table 關聯、SQL 範例）。

## 正向查詢（知道 table 名 → 查欄位）

1. 優先從 `schemas/{table_name}.md` 取得資料。
2. 每份 schema 的 H1 是 table 英文名與中文標題。
3. **Aliases 區塊**列出該 table 的中文別名。當使用者以中文別名稱呼 table 時，從各檔案的 Aliases 反查對應的 table 名。
4. **Columns 表格**是該 table 的權威欄位清單，包含 Column / Type / Null / Key / FK / Description。
5. FK 欄位格式為 `{table}` 或 `{table}.{column}`。

## 反向查詢（不知道 table 名 → 找 table）

當使用者詢問「哪張 table 存 X 資料」或「X 資料在哪裡」時：

1. 先參考 `domains/Code.md`（目前唯一的 domain 文件）的 Business Object 映射表。
2. 若 domain 文件未覆蓋，對 `schemas/` 目錄下所有檔案進行語意搜尋，比對 H1、Aliases 和 Description 欄位。
3. 若找到可能對應的 table，列出 table 名並引用相關欄位說明。

## 禁止行為

- **若 `schemas/` 查無該 table，請直接回答「schema 文件未收錄此 table」，不要自行推測欄位。**
- 不要根據 table 名稱的命名規律（如 `tppdm10`、`tppdm11`）推測不存在的 table 或欄位。
- 不要從 `tables/*.yaml` 直接讀取資料；以 `schemas/*.md` 為唯一欄位參考。
- SQL 查詢範例請根據 `schemas/` 實際欄位組出，不要使用中文欄位名（如「估價代號」、「檔次」）作為欄位識別。
- 本 repo 不收錄 LionGroupRPM（`gitpcm*`）及 LionGroupCMS 的 schema，詢問這些 table 時請告知使用者。

## 補充說明

- 部分 table 的 `type` 欄位為 `unknown`，表示原始文件缺失。遇到此情況請告知使用者該欄位型別未知。
- 部分 FK 以 `fk_note` 格式記錄（如 `FK → istbm00 (ATTR)`），表示是條件 FK 或多型 FK，請保留原文說明。
- Domain 說明文件（`domains/*.md`）包含業務 object ↔ table 映射與 SQL 範例，可輔助回答涉及多張 table 的複合查詢。
