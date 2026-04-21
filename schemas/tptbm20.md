# tptbm20 — 前台旅遊地區代碼檔。多 BU 網站時，不同地區顯示不同目的地選項

**Aliases**: 前台旅遊地區代碼檔, tptbm20, TPTBM20
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tb20_webarea | varchar(2+) | — | PK | — | 目的地代碼（英數，必須足 2 碼） |
| tb20_bu | varchar | — | — | isbum00 | 網站 BU |
| tb20_name | varchar | — | — | — | 名稱 |
| tb20_type | varchar(1) | — | — | — | 團型 |
| tb20_wapdkind | varchar(1) | — | — | — | 分類 |
| tb20_order | int | — | — | — | 顯示順序 |
| tb20_sts | int | — | — | — | 已作廢 (1=作廢, 0=啟用) |
| tb20_mstfn | varchar | — | — | — | 維護者及時區（單位+姓名+空格+時區） |
| tb20_msysdate | datetime | — | — | — | 維護主機時間 |
