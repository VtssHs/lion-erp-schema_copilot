# tppdm40 — 團體班機資料。區分去程/回程/中段航班

**Aliases**: 團體班機資料, tppdm40, PDM40, TPPDM40
**Database**: LionGroupERP
**Module**: TPPDM - 團體產品管理

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd40_prod | varchar(20) | NOT NULL | PK | — | 團號 |
| pd40_prodcomp | varchar(2) | NOT NULL | PK | — | 團控公司 |
| pd40_seq | int | NOT NULL | — | — | 序號（航段序號） |
| pd40_air | varchar(10) | NULL | — | — | 班機（航空公司代碼 + 班機號碼） |
| pd40_fairport | varchar(10) | NULL | — | optbm11 | 起飛機場 |
| pd40_fdate | datetime | NULL | — | — | 起飛日期（起飛日期（當地時區）） |
| pd40_ftime | varchar(5) | NULL | — | — | 起飛時間（格式: HH:MM） |
| pd40_tairport | varchar(10) | NULL | — | optbm11 | 抵達機場 |
| pd40_tdate | datetime | NULL | — | — | 抵達日期（抵達日期（當地時區），可能跨日） |
| pd40_ttime | varchar(5) | NULL | — | — | 抵達時間（格式: HH:MM） |
| pd40_flytime | varchar(10) | NULL | — | — | 飛行時間（飛行時長，2023/05 新增） |
| pd40_max | int | NULL | — | — | 機位（基本配額機位數） |
| pd40_min | int | NULL | — | — | 追加機位（追加配額機位數） |
| pd40_tkt | char(1) | NULL | — | — | 湊票（1=去, 9=回, O=中段, X=湊票不含此段） |
| pd40_mid | char(1) | NULL | — | — | 中段 (開票名單不印)（標記中段航班是否印在開票名單） |
| pd40_sel | varchar(50) | NULL | — | — | 出團單位航段（出團單位使用的航段） |
| pd40_sel2 | varchar(50) | NULL | — | — | 非出團單位航段（非出團單位使用的航段） |
| pd40_pnr | varchar(20) | NULL | — | — | PNR電代 (等2251後再刪)（訂位代碼，與 tppdm41 無關聯） |
| pd40_desc | text | NULL | — | — | 備註（航班備註說明） |
| pd40_mdate | datetime | NULL | — | — | 當地維護時間（當地時區的維護時間） |
| pd40_mstfn | varchar(50) | NULL | — | — | 維護者姓名及時區（格式: "單位+姓名+空格+時區"） |
| pd40_msysdate | datetime | NULL | — | — | 主機時間（系統主機時間） |
