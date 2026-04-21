# ssorm04 — 訂單副檔。訂單刷卡期限管理、契約書回收與說明會文件追蹤

**Aliases**: 訂單副檔, ssorm04, ORM04, SSORM04
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or04_ordr | varchar | — | PK | ssorm00.ordr_ordr | 訂單編號 |
| or04_year | varchar | — | — | ssorm00.ordr_year | 訂單年度 |
| or04_carddate | datetime | — | — | — | 刷卡期限（要換卡刷刷） |
| or04_mdate | datetime | — | — | — | 刷卡日期維護日 |
| or04_mstfn | varchar | — | — | — | 刷卡日期維護人 |
| or04_form | bit | — | — | — | 已收回契約書（1=已收回, 0=未收回） |
| or04_meet_read | bit | — | — | — | 已讀說明會文件（1=已讀, 0=未讀） |
| or04_meet_readtime | datetime | — | — | — | 說明會已讀時間 |
