# tppcm21 — 估價明細暫存計算檔。多幣別成本計算暫存檔，按天數累加成本後匯入 `tppcm20

**Aliases**: 估價明細暫存計算檔, 多幣別成本計算暫存檔, tppcm21, PCM21, TPPCM21
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp21_tpform | unknown | — | — | FK → `tppcm00.tp00_tpform` | 估價代號。換算幣別匯率，同檔次每天累加，按檔次放到 tppcm20（`tppcm00.tp00_tpform`） |
| tp21_no | unknown | — | PK | — | 流水號（的一部分） |
| tp21_day | unknown | — | — | — | 日數（行程天數） |
| tp21_cost1 | unknown | — | — | — | 成本 1（第一組成本金額） |
| tp21_curr1 | unknown | — | — | — | 幣別 1（第一組成本幣別） |
| tp21_cost2 | unknown | — | — | — | 成本 2（第二組成本金額） |
| tp21_curr2 | unknown | — | — | — | 幣別 2（第二組成本幣別） |
| tp21_cost3 | unknown | — | — | — | 成本 3（第三組成本金額） |
| tp21_curr3 | unknown | — | — | — | 幣別 3（第三組成本幣別） |
| tp21_cost4 | unknown | — | — | — | 成本 4（第四組成本金額） |
| tp21_curr4 | unknown | — | — | — | 幣別 4（第四組成本幣別） |
| tp21_cost5 | unknown | — | — | — | 成本 5（第五組成本金額） |
| tp21_curr5 | unknown | — | — | — | 幣別 5（第五組成本幣別） |
| tp21_cost6 | unknown | — | — | — | 成本 6（第六組成本金額） |
| tp21_curr6 | unknown | — | — | — | 幣別 6（第六組成本幣別） |
| tp21_desc | unknown | — | — | — | 備註 |
