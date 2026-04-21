# tppdm65 — 郵輪岸上觀光車次團體。記錄郵輪岸上觀光特定車次與出發團的關聯，即哪些出發團在哪個日期搭乘哪個岸上觀光車次

**Aliases**: 郵輪岸上觀光車次團體, tppdm65, PDM65, TPPDM65
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM) — 郵輪子系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd65_localtour | varchar | — | — | — | 編號（關聯 tppdm62 岸上觀光主檔） |
| pd65_date | datetime | — | PK | — | 日期 |
| pd65_bus | varchar | — | — | — | 車次（關聯 tppdm64 岸上觀光車次） |
| pd65_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| pd65_prodcomp | varchar | — | PK | — | 團號公司 |
| pd65_group | varchar | — | — | — | 多選一群組代碼（同群組代碼的車次為互斥選項） |
| pd65_mstfn | varchar | — | — | — | 維護者姓名及時區（格式：單位+姓名+空格+時區，例：`資訊王大明 TW`；此資料未存當地時間，目前只用於台灣故未有異常） |
| pd65_msysdate | datetime | — | — | — | 維護主機時間 |
