# istbm12 — 各單位線別毛利率與日售價資料

**Aliases**: 各單位線別毛利率與日售價資料, istbm12, TBM12, ISTBM12
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tb12_key | varchar(6) | — | PK | — | 序號 (2碼年+4碼流水) |
| tb12_kind | int | — | — | — | 類別 (0=負責人設定, 1=財務長設定) |
| tb12_line | varchar | — | — | — | 線別 |
| tb12_dline | varchar | — | — | — | 副線別 |
| tb12_prof | varchar | — | — | — | 單位 (負責人依單位設定) |
| tb12_country | varchar | — | — | — | 雄獅國家 (財務長依國家設定) |
| tb12_prodsts | int | — | — | — | 團型 (2=票團) |
| tb12_profit_w | decimal(5,2) | — | — | — | 同業毛利% (5%→5.00) |
| tb12_profit_d | decimal(5,2) | — | — | — | 直客毛利% |
| tb12_fdate | date | — | — | — | 出發效期-起 |
| tb12_tdate | date | — | — | — | 出發效期-訖 |
| tb12_sts | int | — | — | — | 已作廢/未生效 |
| tb12_fsts | int | — | — | — | 已審核處理 |
| tb12_desc | text | — | — | — | 審核記錄 |
| tb12_mstfn | varchar | — | — | — | 維護者姓名 (單位+姓名) |
| tb12_msysdate | datetime | — | — | — | 維護主機時間 |
