# tppdm60 — 郵輪團說明會資料檔。記錄郵輪團的說明會場次資料

**Aliases**: 郵輪團說明會資料檔, 郵輪相關, tppdm60, PDM60, TPPDM60
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product) - 郵輪相關

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd60_prod | varchar | — | PK | tppdm10.prod_prod | 團號（(part), ，**此欄位缺失**） |
| pd60_prodcomp | varchar | — | — | — | 團控公司（**此欄位可能缺失**） |
| pd60_meetno | varchar(6) | — | PK | — | 說明會場次編號（(part), 年度2碼 + 流水號4碼 (如: 250001)） |
| pd60_meetdate | date | — | — | — | 說明會日期（說明會舉辦日期） |
| pd60_meettime | varchar/time | — | — | — | 說明會時間（說明會舉辦時間） |
| pd60_meetplace | varchar | — | — | — | 地點（說明會舉辦地點） |
| pd60_name | varchar | — | — | — | 標準團名（郵輪團名稱） |
| pd60_year | varchar(4)/int | — | — | — | 出發年度（團體出發年度 (如: 2025)） |
| pd60_max | int | — | — | — | 開放人數（此說明會場次開放的報名人數上限） |
| pd60_mstfn | varchar | — | — | — | 維護者姓名及時區（單位+姓名+空格+時區 (如: 直團王大明 TW)） |
| pd60_mdate | datetime | — | — | — | 當地維護時間（維護者所在時區的時間） |
