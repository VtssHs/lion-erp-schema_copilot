# tppdm26 — 行程上下車地點關聯檔。定義行程範本的上下車集合地點（各團若未設定，就抓該團行程的設定）

**Aliases**: 行程上下車地點關聯檔, tppdm26, PDM26, TPPDM26
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd26_tur2 | varchar(20) | — | PK | tppdm20.pd20_tur2 | 行程代號（**PK1**） |
| pd26_station | varchar(20) | — | — | optbm20.tb20_station | 集合地點代碼（**PK2**） |
| pd26_time | varchar(10) | — | — | — | 集合時間（格式如：07:00、08:30） |
| pd26_station1 | varchar(20) | — | — | optbm20.tb20_station | 上車地點代碼 |
| pd26_time1 | varchar(10) | — | — | — | 上車時間（格式如：07:15、08:45） |
| pd26_notshow | bit | — | — | — | 前台不顯示（0=顯示, 1=不顯示） |
| pd26_mstfn | varchar(50) | — | — | — | 維護者姓名及時區（單位+姓名+空格+時區 ex:直團王大明 TW） |
| pd26_mdate | datetime | — | — | — | 當地維護時間（維護者當地時間） |
| pd26_msysdate | datetime | — | — | — | 主機時間（系統伺服器時間） |
