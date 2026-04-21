# tptrm21 — 旅遊館常用證照項目

**Aliases**: 旅遊館常用證照項目, tptrm21, TRM21, TPTRM21
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tr21_travel | varchar | — | PK | tptrm20 | 旅遊館代號（(part 1)） |
| tr21_country | varchar | — | PK | — | 發照國家代號（(part 2)） |
| tr21_vsseq | varchar | — | PK | — | 簽證流水號（(part 3)） |
| tr21_mstfn | varchar | — | — | — | 維護者姓名（單位+姓名） |
| tr21_mdate | datetime | — | — | — | 維護時間 |
