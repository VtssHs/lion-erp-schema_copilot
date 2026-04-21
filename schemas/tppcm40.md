# tppcm40 — 檔次報價總表。儲存各檔次的成本匯總與定價計算結果（同業價、直客價）

**Aliases**: 檔次報價總表, tppcm40, PCM40, TPPCM40
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp40_tpform | unknown | — | — | FK → `tppcm00.tp00_tpform` | 估價代號（`tppcm00.tp00_tpform`） |
| tp40_size | unknown | — | — | — | 檔次（值為 1~6，對應 tppcm30 的 cost1~6） |
| tp40_tot_amt | unknown | — | — | — | 總成本。原估價：總成本 = Local 總成本 + 其他總成本 新估價：總成本由產品人員自行輸入（每人總成本） |
| tp40_cost | unknown | — | — | — | 其他各項累計總成本/人。計算估價時，計算後回寫（非 Local 的其他成本） |
| tp40_local | unknown | — | — | — | Local 報價(含毛利)總成本。幣別為估價幣別 ★由 tppcm31 累計，已換算好匯率（地接社報價總額） |
| tp40_amt_w | unknown | — | — | — | 同業定價。總成本 × (1+(同業毛利%/(1-同業毛利%))) Ex: 總成本 10000 元，同業毛利 5%，直客毛利 8% 同業定價 = 10000 × (1+(0.05/1-0.05)) = 10526（賣給旅行社同業的價格） |
| tp40_amt_d | unknown | — | — | — | 直客定價。同業定價 × (1+(直客毛利%/(1-直客毛利%))) 直客定價 = 10526 × (1+(0.08/1-0.08)) = 11442（賣給終端消費者的價格） |
| tp40_price | unknown | — | — | — | 估價單位報價（實際對外報價（可能基於同業價或直客價）） |
| tp40_git | unknown | — | — | — | 團員不含 Foc/TL（實際付費旅客人數） |
| tp40_foc | unknown | — | — | — | Foc（Free of Charge，免費招待名額） |
| tp40_seat | unknown | — | — | — | 車型（座位數）（配車參考） |
