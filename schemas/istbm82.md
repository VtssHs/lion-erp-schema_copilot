# istbm82 — 公用標籤群組檔

**Aliases**: 公用標籤群組檔, istbm82, TBM82, ISTBM82
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tb82_no | varchar | — | PK | — | 群組代碼 |
| tb82_issingle | int | — | — | — | 群組是否為單選 (1=單選, 0=多選) |
| tb82_typecode | varchar | — | — | — | 所屬種類代碼 |
| tb82_categorycode | varchar | — | — | — | 標籤類別代碼 |
| tb82_triptypecode | varchar | — | — | — | 旅遊形式代碼 |
| tb82_sts | int | — | — | — | 標籤狀態 (1=作廢, 0=啟用) |
| tb82_expsdate | date | — | — | — | 有效起始日 (排程更新標籤狀態) |
| tb82_expedate | date | — | — | — | 有效結束日 (排程更新標籤狀態) |
| tb82_sort | int | — | — | — | 排序 |
| tb82_mstfn | varchar | — | — | — | 維護者 |
| tb82_mdate | datetime | — | — | — | 維護時間 |
