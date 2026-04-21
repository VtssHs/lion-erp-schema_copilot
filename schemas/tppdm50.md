# tppdm50 — 出團旅館檔。記錄團體行程中每日住宿旅館的詳細資料

**Aliases**: 出團旅館檔, tppdm50, PDM50, TPPDM50
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd50_prod | varchar | — | PK | tppdm10.prod_prod | 團號（(part)） |
| pd50_prodcomp | varchar | — | — | — | 團控公司 |
| pd50_seq | int | — | PK | — | 序號（(part), 用於區分同一團的多筆旅館記錄） |
| pd50_sts | varchar/char | — | — | — | 確認狀況（旅館訂房確認狀態） |
| pd50_date | date | — | — | — | 日期（入住日期） |
| pd50_hotel | varchar | — | — | FK → 旅館主檔 (ophtm*) | 旅館代號（*)） |
| pd50_lvl | varchar | — | — | — | 等級(艙等)（主要 for 自由行參考，但未結合價格 (2003/01/07)） |
| pd50_max | int | — | — | — | 人數（入住人數） |
| pd50_room | int | — | — | — | 房數（訂房數量） |
| pd50_price | decimal | — | — | — | 報價金額（旅館報價） |
| pd50_curr | varchar | — | — | — | 報價幣別（幣別代碼 (如 USD, TWD)） |
| pd50_unit | char(1) | — | — | — | 報價單位（**R**=房, **P**=人） |
| pd50_hotel_idno | varchar | — | — | — | 自採房使用序號（關聯自採房系統的識別碼） |
| pd50_audit | char(1) | — | — | — | 審核狀態（空白=不需審核(預設), 1=待審核, 2=審核中, 3=退件, 9=審核通過） |
| pd50_desc | varchar/text | — | — | — | 備註（房型及數量說明 (如: 15 Twin + 1 Double), 旅館名稱=備註(尚未確認)） |
| pd50_mstfn | varchar | — | — | — | 維護者姓名及時區（單位+姓名+空格+時區 (如: 直團王大明 TW), 只要 save 一筆） |
| pd50_mdate | datetime | — | — | — | 當地維護時間（維護者所在時區的時間） |
| pd50_msysdate | datetime | — | — | — | 主機時間（系統主機的時間戳記） |
