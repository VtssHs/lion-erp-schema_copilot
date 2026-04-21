# tptbm15 — 台灣說明會提醒文字。- 說明會時告知旅客航班資訊

**Aliases**: 台灣說明會提醒文字, tptbm15, TBM15, TPTBM15
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tb15_line | varchar | — | PK | istbm10 | 線別（(part 1)） |
| tb15_dline | varchar | — | PK | — | 副線別（(part 2)） |
| tb15_kind | varchar(1) | — | PK | — | 提醒類別（(part 3)） |
| tb15_fdate | date | — | PK | — | 出團起日（(part 4)） |
| tb15_tdate | date | — | — | — | 出團迄日 |
| tb15_desc | text | — | — | — | 提醒內容 |
| tb15_carr | varchar | — | — | — | 航空公司 |
| tb15_flightno | varchar | — | — | — | 航班號碼 |
| tb15_fairport | varchar | — | — | — | 起飛機場 |
| tb15_tbm0fit | varchar(1) | — | — | — | 團類型 |
| tb15_mstfn | varchar | — | — | — | 維護者姓名（單位+姓名） |
| tb15_mdate | datetime | — | — | — | 維護時間 |
