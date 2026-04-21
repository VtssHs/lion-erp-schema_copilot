# tppdm20_ez — 易遊行程主檔。易遊系統的行程範本（可供多個團體使用）

**Aliases**: 易遊行程主檔, tppdm20_ez, PDM20_EZ, TPPDM20_EZ
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| ez20_tur2 | varchar(20) | — | PK | — | 行程代號（唯一識別碼） |
| ez20_sts | bit | — | — | — | 已下架（1=不要轉匯至易遊） |
| ez20_zpsts | varchar(10) | — | — | — | ？？（用途待確認） |
| ez20_line | varchar(10) | — | — | — | 易遊線別代碼（對應易遊系統的線別分類） |
| ez20_area | varchar(10) | — | — | — | 易遊區域代碼（對應易遊系統的區域分類） |
| ez20_country | varchar(10) | — | — | — | 易遊國家代碼（對應易遊系統的國家分類） |
| ez20_city | varchar(50) | — | — | — | 易遊旅遊城市群代碼（多個城市代碼組合） |
| ez20_city_dname | nvarchar(200) | — | — | — | 易遊旅遊城市說明（城市群的說明文字） |
| ez20_mstfn | varchar(50) | — | — | — | 維護者姓名及時區（單位+姓名+空格+時區 ex:直團王大明 TW） |
| ez20_mdate | datetime | — | — | — | 維護時間（當地維護日期） |
