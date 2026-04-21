# tptbm11 — 標準團名對應銷售資訊檔

**Aliases**: 標準團名對應銷售資訊檔, tptbm11, TPTBM11
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tb11_name | varchar(36) | — | PK | tptbm00 | 標準團名 (GUID)（(part 1)） |
| tb11_note | varchar | — | PK | tptbm10 | 說明項目（(part 2)） |
| tb11_country | varchar | — | PK | tptbm10 | 出團雄獅國家（(part 3)） |
| tb11_area | varchar | — | PK | tptbm10 | 地區（(part 4)） |
| tb11_darea | varchar | — | PK | tptbm10 | 細地區（(part 5)） |
| tb11_seq | varchar | — | PK | tptbm10 | 序號（同 tptbm10 的 note_carr）（(part 6)） |
| tb11_mstfn | varchar | — | — | — | 維護者及時區（單位+姓名+空格+時區） |
| tb11_msysdate | datetime | — | — | — | 維護主機時間 |
| tb11_mdate | datetime | — | — | — | 當地維護時間 |
