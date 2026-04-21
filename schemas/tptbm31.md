# tptbm31 — 海外 FIT 票統計大類代碼檔。定義海外 FIT 票的統計大類代碼，供報表統計歸類使用，是 tptbm30 地區代碼的上層分類

**Aliases**: 海外 FIT 票統計大類代碼檔, 標準團名管理, tptbm31, TBM31, TPTBM31
**Database**: LionGroupERP
**Module**: 標準團名管理 (TPTBM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tb31_rpt | varchar | — | PK | — | 代碼 |
| tb31_name | varchar | — | — | — | 名稱 |
| tb31_order | int | — | — | — | 顯示順序 |
| tb31_sts | bit/int | — | — | — | 已作廢（1=作廢, 0=啟用） |
| tb31_mstfn | varchar | — | — | — | 維護者姓名及時區（格式：單位+姓名+空格+時區，例：`北票林小鈴 TW`） |
| tb31_msysdate | datetime | — | — | — | 維護主機時間 |
