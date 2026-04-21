# tptbm30 — 海外 FIT 票地區代碼檔。定義海外 FIT（Free Independent Travel）票使用的地區代碼，供票務系統分類與統計報表使用

**Aliases**: 海外 FIT 票地區代碼檔, 標準團名管理, tptbm30, TBM30, TPTBM30
**Database**: LionGroupERP
**Module**: 標準團名管理 (TPTBM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tb30_area | varchar | — | PK | — | 代碼 |
| tb30_name | varchar | — | — | — | 名稱 |
| tb30_rpt | varchar | — | — | — | 統計大類 |
| tb30_order | int | — | — | — | 顯示順序 |
| tb30_sts | bit/int | — | — | — | 已作廢（1=作廢, 0=啟用） |
| tb30_mstfn | varchar | — | — | — | 維護者姓名及時區（格式：單位+姓名+空格+時區，例：`北票林小鈴 TW`） |
| tb30_msysdate | datetime | — | — | — | 維護主機時間 |
