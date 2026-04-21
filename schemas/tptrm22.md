# tptrm22 — 旅遊館對應旅遊地區代碼檔

**Aliases**: 旅遊館對應旅遊地區代碼檔, tptrm22, TRM22, TPTRM22
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tr22_travel | varchar | — | PK | tptrm20 | 旅遊館代號（(part 1)） |
| tr22_webarea | varchar | — | PK | tptbm20 | 目的地代碼（(part 2)） |
| tr22_mstfn | varchar | — | — | — | 維護者及時區（單位+姓名+空格+時區） |
| tr22_mdate | datetime | — | — | — | 維護時間 |
