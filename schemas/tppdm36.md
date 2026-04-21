# tppdm36 — 團體上下車地點關聯檔。定義每個出發團的上下車集合地點設定；各團若未設定，則退而使用行程層級的 tppdm26 設定

**Aliases**: 團體上下車地點關聯檔, tppdm36, PDM36, TPPDM36
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd36_prod | varchar | — | — | tppdm10.prod_prod | 團號（；各團若未設定上車地點，就抓行程層級（tppdm26）的設定） |
| pd36_prodcomp | varchar | — | PK | — | 團控公司 |
| pd36_station | varchar | — | — | optbm20.tb20_station | 集合地點代碼 |
| pd36_time | varchar | — | — | — | 集合時間（格式如：07:00、08:30） |
| pd36_station1 | varchar | — | — | optbm20.tb20_station | 上車地點代碼 |
| pd36_time1 | varchar | — | — | — | 上車時間（格式如：07:15、08:45） |
| pd36_notshow | bit | — | — | — | 前台不顯示（0=顯示，1=不顯示） |
| pd36_mstfn | varchar | — | — | — | 維護者姓名及時區（格式：單位+姓名+空格+時區，例：`直團王大明 TW`） |
| pd36_mdate | datetime | — | — | — | 當地維護時間 |
| pd36_msysdate | datetime | — | — | — | 主機時間 |
