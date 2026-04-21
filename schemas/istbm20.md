# istbm20 — 地區代碼檔

**Aliases**: 地區代碼檔, istbm20, ISTBM20
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| area_area | varchar | — | PK | — | 地區代號（(Part 1)） |
| area_darea | varchar | — | PK | — | 細地區代號（(Part 2)） |
| area_line | varchar | — | — | — | 線別 |
| area_dline | varchar | — | — | — | 副線別 |
| area_dname | varchar | — | — | — | 中文名稱 |
| area_prod | varchar(2) | — | — | — | 團號2碼 |
| area_fbacode | varchar | — | — | — | 富邦旅遊地區代碼 |
| area_fbaname | varchar | — | — | — | 富邦旅遊地區中文 |
| area_ordr_gst2 | varchar | — | — | — | 國外同業GST稅率 |
| area_sts | int | — | — | — | 已作廢 (1=作廢, 0=啟用) |
| area_desc | text | — | — | — | 說明 |
| area_desc2 | text | — | — | — | 備註 (作廢必填) |
| area_mstfn | varchar | — | — | — | 維護者姓名 (單位+姓名) |
| area_msysdate | datetime | — | — | — | 維護當地時間 |
