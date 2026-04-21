# tppdm56 — 供應商詳細欄位設定檔。針對不同 B2P 供應商設定其需要填寫的詳細欄位與必填狀態

**Aliases**: 供應商詳細欄位設定檔, tppdm56, PDM56, TPPDM56
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd56_local | nvarchar(12) | — | PK | **PK1**, FK → 供應商主檔，配合 B2P 系統型態 | 供應商代碼（**PK1**, ，配合 B2P 系統型態） |
| pd56_seq | int | — | — | — | 流水號（**PK2**, 欄位設定的順序編號） |
| pd56_code | varchar(50) | — | — | FK → 欄位代碼主檔 | 欄位代號 |
| pd56_required | bit | — | — | — | 必填狀態（1=必填, 0=選填） |
