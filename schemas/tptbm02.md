# tptbm02 — 標準團名關鍵字檔

**Aliases**: 標準團名關鍵字檔, tptbm02, TBM02, TPTBM02
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tbm2_line | varchar | — | PK | istbm10 | 線別（(part 1)） |
| tbm2_dline | varchar | — | PK | — | 副線別（(part 2)） |
| tbm2_area | varchar | — | PK | — | 地區（(part 3)） |
| tbm2_darea | varchar | — | PK | — | 細地區（(part 4)） |
| tbm2_keyword | varchar | — | PK | — | 關鍵字（(part 5)） |
| tbm2_sameword | text | — | — | — | 相似字（逗號分隔） |
| tbm2_mstfn | varchar | — | — | — | 維護者及時區（單位+姓名+空格+時區） |
| tbm2_msysdate | datetime | — | — | — | 維護主機時間 |
| tbm2_mdate | datetime | — | — | — | 當地維護時間 |
