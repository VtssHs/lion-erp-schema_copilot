# tppdm57 — 團詳細設定欄位。團體層級的詳細欄位設定值，覆蓋供應商層級的預設設定（tppdm56）

**Aliases**: 團詳細設定欄位, tppdm57, PDM57, TPPDM57
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd57_prod | varchar(10) | — | PK | tppdm10.prod_prod | 團號（**PK1**） |
| pd57_prodcomp | varchar(2) | — | — | — | 團控公司 |
| pd57_local | nvarchar(12) | — | — | **PK2**, FK → 供應商主檔 | 供應商代碼（**PK2**） |
| pd57_coltype | varchar(50) | — | — | **PK3**, FK → 欄位代碼主檔 | 欄位代碼（**PK3**） |
| pd57_colval | nvarchar(500) | — | — | — | 欄位值（實際填寫的資料內容） |
