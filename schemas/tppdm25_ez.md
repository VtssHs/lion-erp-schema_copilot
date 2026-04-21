# tppdm25_ez — 易遊團體行程副檔。易遊系統的行程補充資訊（特色、備註等）

**Aliases**: 易遊團體行程副檔, tppdm25_ez, PDM25_EZ, TPPDM25_EZ
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| ez25_tur2 | varchar(20) | — | PK | **PK1**, FK to tppdm20_ez.ez20_tur2 | 行程代號（**PK1**, FK to tppdm20_ez.ez20_tur2） |
| ez25_type | char(1) | — | — | — | 類別（**PK2**, 類別代碼（與雄獅系統類似）） |
| ez25_desc | nvarchar(max) | — | — | — | 內容（依 ez25_type 存放不同類型內容） |
| ez25_msysdate | datetime | — | — | — | 異動日期（系統時間，記錄最後更新時間） |
