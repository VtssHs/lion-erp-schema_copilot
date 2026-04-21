# tppcm20 — 估價明細檔。儲存估價單的明細資料，用於計算 `tppcm30` 團分攤成本

**Aliases**: 估價明細檔, tppcm20, PCM20, TPPCM20
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp20_tpform | unknown | — | — | FK → `tppcm00.tp00_tpform` | 估價代號（`tppcm00.tp00_tpform`） |
| tp20_ncost | unknown | — | — | — | 估價幣別成本。畫面 show 這欄（已換算為估價幣別） |
| tp20_cost | unknown | — | — | — | 成本。★要估算 `tppcm30` 團分攤成本，已換算成估價幣別的金額（用於檔次成本計算） |
| tp20_profit | unknown | — | — | — | 毛利 % |
| tp20_seat | unknown | — | — | — | 車型（座位數） |
