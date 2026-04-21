# istbm83 — 公用標籤檔

**Aliases**: 公用標籤檔, istbm83, TBM83, ISTBM83
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tb83_no | varchar | — | PK | — | 標籤代碼 |
| tb83_groupno | varchar | — | — | FK | 上層群組代碼（FK） |
| tb83_sts | int | — | — | — | 標籤狀態 (1=作廢, 0=啟用) |
| tb83_sort | int | — | — | — | 排序 |
| tb83_mstfn | varchar | — | — | — | 維護者 |
| tb83_mdate | datetime | — | — | — | 維護時間 |
