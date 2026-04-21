# tppcm30 — 檔次估價成本主檔。儲存不同出團人數檔次的分攤成本計算結果

**Aliases**: 檔次估價成本主檔, tppcm30, PCM30, TPPCM30
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp30_tpform | unknown | — | — | FK → `tppcm00.tp00_tpform` | 估價代號。同檔次換算成估價幣別金額累計到 tppcm40（`tppcm00.tp00_tpform`） |
| tp30_no | unknown | — | PK | — | 流水號。單房間差同樣計算，存到 tppcm00（的一部分） |
| tp30_cost1 | unknown | — | — | — | 成本 1。6 檔人次的成本（第一檔人數的分攤成本） |
| tp30_cost2 | unknown | — | — | — | 成本 2（第二檔人數的分攤成本） |
| tp30_cost3 | unknown | — | — | — | 成本 3（第三檔人數的分攤成本） |
| tp30_cost4 | unknown | — | — | — | 成本 4（第四檔人數的分攤成本） |
| tp30_cost5 | unknown | — | — | — | 成本 5（第五檔人數的分攤成本） |
| tp30_cost6 | unknown | — | — | — | 成本 6（第六檔人數的分攤成本） |
| tp30_curr | unknown | — | — | — | 幣別（統一為估價幣別） |
| tp30_profit | unknown | — | — | — | 毛利 %（目標毛利率） |
| tp30_room | unknown | — | — | — | 單房間差（單房補價金額） |
| tp30_local | unknown | — | — | — | Local 代碼（地接社或當地供應商代碼） |
| tp30_desc | unknown | — | — | — | 備註 |
