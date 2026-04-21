# tppdm62 — 郵輪岸上觀光主檔。定義郵輪行程可選購的岸上觀光項目主檔，涵蓋岸上觀光、船上活動、機票、酒店四大類別，記錄售價、成本、集合資訊等完整資料

**Aliases**: 郵輪岸上觀光主檔, tppdm62, PDM62, TPPDM62
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM) — 郵輪子系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd62_localtour | varchar | — | PK | — | 編號 |
| pd62_sts | bit/int | — | — | — | 已停用（1=停用，0=啟用） |
| pd62_type | varchar | — | — | — | 類別（1=岸上觀光，2=船上活動，3=機票，4=酒店） |
| pd62_name | varchar | — | — | — | 名稱 |
| pd62_country | varchar | — | — | — | 國家 |
| pd62_city | varchar | — | — | — | 城市 |
| pd62_desc | nvarchar | — | — | — | 說明 |
| pd62_pic | varchar | — | — | — | 岸上觀光圖片 |
| pd62_seat | int | — | — | — | 人數 |
| pd62_meal | varchar | — | — | — | 含餐（1=含餐） |
| pd62_cguide | varchar | — | — | — | 華語導遊（1=華語導遊） |
| pd62_tour_time | varchar | — | — | — | 行程時間 |
| pd62_place | varchar | — | — | — | 集合地點 |
| pd62_time | varchar | — | — | — | 集合時間 |
| pd62_amt_curr | varchar | — | — | — | 售價幣別 |
| pd62_amt_a | decimal | — | — | — | 大人小孩售價 |
| pd62_amt_c | decimal | — | — | — | 小孩售價 |
| pd62_amt_i | decimal | — | — | — | 嬰兒售價 |
| pd62_cost_curr | varchar | — | — | — | 成本幣別 |
| pd62_cost_a | decimal | — | — | — | 大人小孩成本 |
| pd62_cost_c | decimal | — | — | — | 小孩成本 |
| pd62_cost_i | decimal | — | — | — | 嬰兒成本 |
| pd62_infseat | varchar | — | — | — | 嬰兒佔位（1=佔位，0=不佔位（預設）） |
| pd62_matchname | varchar | — | — | — | 比對標準團名（多值用分號區隔） |
| pd62_matchline | varchar | — | — | — | 比對線別（多值用分號區隔） |
| pd62_notshow | bit | — | — | — | 前台不顯示（0=顯示，1=不顯示） |
| pd62_mstfn | varchar | — | — | — | 維護者姓名及時區（格式：單位+姓名+空格+時區，例：`資訊王大明 TW`；此資料未存當地時間，目前只用於台灣故無異常） |
| pd62_msysdate | datetime | — | — | — | 維護主機時間 |
