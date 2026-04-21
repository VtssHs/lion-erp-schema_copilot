# tppdm41 — 團體 PNR 資料。記錄團體訂位記錄 (PNR - Passenger Name Record) 的詳細資料

**Aliases**: 團體 PNR 資料, tppdm41, PDM41, TPPDM41
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd41_prod | varchar | — | PK | tppdm10.prod_prod | 團號（(part)） |
| pd41_prodcomp | varchar | — | — | — | 團控公司 |
| pd41_pnr | varchar | — | PK | — | PNR（(part?), Passenger Name Record 訂位代號） |
| pd41_carr | varchar | — | — | — | 航空公司（航空公司代碼 (如 CI, BR, CX)） |
| pd41_mid | bit | — | — | — | 中段（**1**=是中段, 0 或 NULL=非中段） |
| pd41_max | int | — | — | — | 本團機位（此 PNR 配置給本團的機位數） |
| pd41_nmax | int | — | — | — | 名單人數（已挑選進名單的人數） |
| pd41_ndate | datetime | — | — | — | 挑名單時間（名單挑選的時間戳記） |
| pd41_nstfn | varchar | — | — | — | 挑名單者姓名（如: 王大明） |
| pd41_update | datetime | — | — | — | 上傳名單時間（名單上傳至航空公司系統的時間） |
| pd41_desc | varchar/text | — | — | — | 備註（PNR 相關備註或特殊說明） |
| pd41_mstfn | varchar | — | — | — | 維護者姓名及時區（Pdrc02_pnr 才 save，單位+姓名+空格+時區 (如: 直團王大明 TW)） |
| pd41_mdate | datetime | — | — | — | 當地維護時間（維護者所在時區的時間） |
| pd41_msysdate | datetime | — | — | — | 主機時間（系統主機的時間戳記） |
