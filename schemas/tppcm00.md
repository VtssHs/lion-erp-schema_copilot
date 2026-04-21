# tppcm00 — 團體產品估價主檔。儲存團體產品的估價單主檔資料

**Aliases**: 團體產品估價主檔, tppcm00, PCM00, TPPCM00
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp00_tpform | unknown | — | PK | — | 估價代號。估價單唯一識別碼 |
| tp00_name | unknown | — | — | — | 估價名稱 |
| tp00_prodname | unknown | — | — | — | 標準團名 |
| tp00_kind | unknown | — | — | — | 類別。0-原估價 1-新估價 |
| tp00_fsts | unknown | — | — | — | 進度。空白-建置 F-估價完成 V-估價待核准尚未生效 |
| tp00_sts | unknown | — | — | — | 已作廢 |
| tp00_cxl | unknown | — | — | — | 報價結果無效。1-無效 |
| tp00_cxldesc | unknown | — | — | — | 報價無效原因 |
| tp00_prof | unknown | — | — | — | 團控單位 |
| tp00_rprof | unknown | — | — | — | 需求單位 |
| tp00_rstfn | unknown | — | — | — | 需求者員編 |
| tp00_tpstfn | unknown | — | — | — | 維護者員編。估價審核完成時留言通知的對象 |
| tp00_ffstfn | unknown | — | — | — | 報價者單位姓名時區。單位+姓名+空格+時區 ex:直團王大明 TW |
| tp00_astfn | unknown | — | — | — | 審核者單位姓名時區。單位+姓名+空格+時區 ex:直團王大明 TW |
| tp00_mstfn | unknown | — | — | — | 維護者單位姓名時區。單位+姓名+空格+時區 ex:直團王大明 TW |
| tp00_line | unknown | — | — | — | 線別 |
| tp00_dline | unknown | — | — | — | 副線別 |
| tp00_area | unknown | — | — | — | 地區 |
| tp00_darea | unknown | — | — | — | 細地區。可空白 |
| tp00_days | unknown | — | — | — | 天數 |
| tp00_prodsts | unknown | — | — | — | 團型 |
| tp00_tl | unknown | — | — | — | 領隊人數。畫面def: 1 |
| tp00_agent | unknown | — | — | — | 包團同行 |
| tp00_fdate | unknown | — | — | — | 出發起日 |
| tp00_tdate | unknown | — | — | — | 出發訖日 |
| tp00_ffdate | unknown | — | — | — | 報價日期 |
| tp00_adate | unknown | — | — | — | 審核日期。當地時間 |
| tp00_mdate | unknown | — | — | — | 當地維護日期 |
| tp00_msysdate | unknown | — | — | — | 主機維護日期 |
| tp00_curr | unknown | — | — | — | 估價幣別 |
| tp00_mult | unknown | — | — | — | 估價單位報價乘數% |
| tp00_profit_d | unknown | — | — | — | 直客毛利% |
| tp00_profit_w | unknown | — | — | — | 同業毛利% |
| tp00_rpt | unknown | — | — | — | 報表小數位數。For 報表金額統一小數位數 |
| tp00_room_cto | unknown | — | — | — | 旅館單人價。有key旅館成本（國旅, InBound才會有）只參考不估價用 |
| tp00_room_cto_qty | unknown | — | — | — | 旅館單房差數量-人。★有上才有此欄 |
| tp00_room_local | unknown | — | — | — | Local報價總房間差。★有key Local單房間差（國旅, OutBound才會有）己換算好匯率 |
| tp00_room_local_qty | unknown | — | — | — | Local報價單房差數量-人。★有上才有此欄 |
| tp00_desc | unknown | — | — | — | 估價單位備註 |
| tp00_desc2 | unknown | — | — | — | 估價說明。當估價毛利低於標準時,需填寫 |
