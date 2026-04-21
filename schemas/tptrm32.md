# tptrm32 — 旅遊館群組行程。前台顯示促銷標籤，吸引點擊

**Aliases**: 旅遊館群組行程, tptrm32, TRM32, TPTRM32
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tr32_travel | varchar | — | PK | tptrm30 | 旅遊館代號（(part 1)） |
| tr32_group | varchar | — | PK | tptrm30 | 旅遊館群組代號（(part 2)） |
| tr32_seq | int | — | PK | — | 序號（(part 3)） |
| tr32_name | varchar(36) | — | — | tptbm00 | 標準團名 (GUID) |
| tr32_tur2 | varchar | — | — | — | 行程代號 |
| tr32_order | int | — | — | — | 順序 |
| tr32_fdate | date | — | — | — | 出團起日 |
| tr32_tdate | date | — | — | — | 出團迄日 |
| tr32_pdhot | varchar | — | — | FK → istbm00 (PDHOT) | 搶購字樣 |
| tr32_amt_b2c | decimal | — | — | — | B2C 最低直客價 |
| tr32_amt_b2bc | decimal | — | — | — | B2BC 最低直售價 |
| tr32_amt_b2b | decimal | — | — | — | B2B 最低批售價 |
| tr32_d8_b2c | varchar | — | — | — | B2C 最近 3 團出發日期 |
| tr32_d8_b2bc | varchar | — | — | — | B2BC 出團日期 |
| tr32_d8_b2b | varchar | — | — | — | B2B 出團日期 |
| tr32_fbu | varchar | — | — | — | 產品來源 |
| tr32_mstfn2 | varchar | — | — | — | 產品維護者及時區（單位+姓名+空格+時區） |
| tr32_msysdate2 | datetime | — | — | — | 產品主機維護時間 |
| tr32_mdate2 | datetime | — | — | — | 產品維護當地時間（依 tptrm30 負責單位時區） |
