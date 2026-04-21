# tppdm25 — 團體行程副檔。行程補充資訊（特色、備註、銀行資訊、TDH設定）

**Aliases**: 團體行程副檔, tppdm25, PDM25, TPPDM25
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd25_tur2 | varchar(20) | — | PK | **PK1**, FK to tppdm20.pd20_tur2 | 行程代號（**PK1**, FK to tppdm20.pd20_tur2） |
| pd25_type | char(1) | — | — | — | 類別（**PK2**, B=銀行, D=備註, S=特色, T=TDH設定） |
| pd25_seq | int | — | — | — | 序號（**PK3**, 目前特色可以新增多筆） |
| pd25_desc | nvarchar(max) | — | — | — | 內容（依 pd25_type 存放不同類型內容） |
| pd25_rowversion | timestamp | — | — | — | 時間戳記（SQL Server 自動維護） |
