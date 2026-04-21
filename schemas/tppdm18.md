# tppdm18 — 團體預訂數量檔。記錄團體各類資源的預訂數量（房型、餐食、門票、行李等）

**Aliases**: 團體預訂數量檔, tppdm18, PDM18, TPPDM18
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd18_prod | varchar | — | PK | tppdm10.prod_prod | 團號 |
| pd18_prodcomp | varchar | — | — | — | 團控公司 |
| pd18_r1 | int | — | — | — | 單人房（Single Room 數量） |
| pd18_r2 | int | — | — | — | 雙人房Twin（Twin Room 數量（兩張單人床）） |
| pd18_r22 | int | — | — | — | 雙人房Double（Double Room 數量（一張雙人床）） |
| pd18_r3 | int | — | — | — | 三人房（Triple Room 數量） |
| pd18_r4 | int | — | — | — | 四人房（Quad Room 數量） |
| pd18_r9 | int | — | — | — | 司機房（Driver Room 數量） |
| pd18_rfoc | int | — | — | — | FOC 房（Free of Charge 房間數量） |
| pd18_ma | int | — | — | — | 旅館含早 A（大人早餐數量） |
| pd18_mc | int | — | — | — | 旅館含早 C（小孩早餐數量） |
| pd18_mi | int | — | — | — | 旅館含早 I（嬰兒早餐數量） |
| pd18_mfoc | int | — | — | — | 旅館含早 FOC（FOC 早餐數量） |
| pd18_a | int | — | — | — | A（大人餐食數量） |
| pd18_c | int | — | — | — | C（小孩餐食數量） |
| pd18_i | int | — | — | — | 嬰兒（嬰兒餐食數量） |
| pd18_foc | int | — | — | — | FOC（FOC 餐食數量） |
| pd18_lg | int | — | — | — | GL（Local Guide 餐食數量） |
| pd18_tl | int | — | — | — | TL（Tour Leader 餐食數量） |
| pd18_ta | int | — | — | — | A（大人門票數量） |
| pd18_tc | int | — | — | — | C（小孩門票數量） |
| pd18_ti | int | — | — | — | 嬰兒（嬰兒門票數量） |
| pd18_tfoc | int | — | — | — | FOC（FOC 門票數量） |
| pd18_to | int | — | — | — | 老人（老人門票數量） |
| pd18_ts | int | — | — | — | 學生（學生門票數量） |
| pd18_tlg | int | — | — | — | LG（Local Guide 門票數量） |
| pd18_ttl | int | — | — | — | TL（Tour Leader 門票數量） |
| pd18_bag | int | — | — | — | 旅館行李（行李件數（可能是旅館寄存或運送）） |
| pd18_mstfn | varchar | — | — | — | 維護者單位姓名時區（單位+姓名+空格+時區 (如: 直團王大明 TW)） |
| pd18_mdate | datetime | — | — | — | 維護日當地時間（維護者所在時區的時間） |
| pd18_msysdate | datetime | — | — | — | 維護日主機時間（系統主機的時間戳記） |
