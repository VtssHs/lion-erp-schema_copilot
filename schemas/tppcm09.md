# tppcm09 — 估價幣別匯率檔。儲存估價單使用的各幣別匯率設定

**Aliases**: 估價幣別匯率檔, tppcm09, PCM09, TPPCM09
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp09_tpform | unknown | — | — | FK → `tppcm00.tp00_tpform` | 估價代號（`tppcm00.tp00_tpform`） |
| tp09_curr | unknown | — | — | — | 幣別（（與 tp09_tpform 組成複合鍵）） |
| tp09_erat | unknown | — | — | — | 換算匯率 |
