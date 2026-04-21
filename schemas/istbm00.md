# istbm00 — 基礎代碼主檔

**Aliases**: 基礎代碼主檔, istbm00, ISTBM00
**Database**: LionGroupRPM
**Module**: ISTBM（Infrastructure System Table Basic Master）

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| __tabl_type__ | varchar(50) | — | PK | — | 代碼類別（統一大寫（如 `ORDER_STATUS`, `PRODUCT_CATEGORY`）） |
| __tabl_code__ | varchar(50) | — | — | — | 代碼（空字串 `''` 表示類別名稱註記用（類別本身的說明）） |
| __tabl_cname__ | varchar(100) | — | — | — | 中文名稱（主要顯示名稱） |
| __tabl_ename__ | varchar(100) | — | — | — | 英文名稱（`*` 表示可於 opag29 自行授權） |
| __tabl_dname__ | varchar(100) | — | — | — | 顯示名稱（可能為簡稱或前台顯示名） |
| __tabl_desc__ | text | — | — | — | 備註（詳細說明） |
| __tabl_order__ | int | — | — | — | 顯示順序（同類別內的排序） |
| __tabl_sts__ | bit | — | — | — | 已停用（`1` = 已停用，`0` = 啟用中） |
| __tabl_sts1__ | bit | — | — | — | 系統專用（`1` = 系統專用，不提供使用者修改） |
| __tabl_stfn__ | varchar(500) | — | — | — | 授權建檔名單（格式：`,008013,008079,`（員工編號清單） 若類別有設定名單，則提供該 user 增修權限） |
| __tabl_typekind__ | varchar(50) | — | — | — | 使用範圍（類別太多時，用 `kind` 作為上層分類 例：`ORDER` kind 下有多個 type） |
| __tabl_use__ | varchar(200) | — | — | — | 其他使用（特殊用途欄位 例：`__tabl_type__ = 'UPLOAD'` 時存「合約;其他文件」） |
| __tabl_mdate__ | datetime | — | — | — | 增修主機時間（最後異動時間） |
| __tabl_mstfn__ | varchar(50) | — | — | — | 增修者姓名（格式：`直團王大明`） |
