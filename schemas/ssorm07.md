# ssorm07 — 訂單業務自檢項目。記錄訂單處理過程中業務人員的自檢項目確認狀態，確保訂單作業品質與完整性

**Aliases**: 訂單業務自檢項目, ssorm07, ORM07, SSORM07
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or07_ordr | varchar | — | — | ssorm00.ordr_ordr | 訂單號 |
| or07_year | varchar | — | — | ssorm00.ordr_year | 訂單年 |
| or07_code | varchar | — | — | FK → istbm81 (CHECKLIST) | 檢核類別 |
| or07_item | varchar | — | PK | — | 檢核項目 |
| or07_sts | varchar | — | — | — | 已確認（0=未確認, 1=已確認） |
| or07_desc | varchar | — | — | — | 備註說明（補充說明或異常記錄） |
| or07_mstfn | varchar | — | — | — | 維護人（最後確認的業務人員） |
| or07_mdate | datetime | — | — | — | 維護日（最後確認時間） |
