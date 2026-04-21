# tppdm93 — 多渠道自動上架設定。定義「產品 BU × 團單位」對應「渠道 BU × 渠道」的自動上架規則，當新團建立時自動套用分銷設定，不需逐團手動設定

**Aliases**: 多渠道自動上架設定, tppdm93, PDM93, TPPDM93
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd93_chlbu | varchar | — | — | isbum00.bu00_bu | 渠道 BU |
| pd93_chl | varchar | — | — | isbum01.bu01_channel | 渠道 |
| pd93_prodbu | varchar | — | — | isbum00.bu00_bu | 產品 BU |
| pd93_prodprof | varchar | — | PK | — | 團單位 |
| pd93_chltype | varchar | — | — | — | 自動上架設定值 |
| pd93_istfn | varchar | — | — | — | 建檔人 |
| pd93_idate | datetime | — | — | — | 建檔日期 |
| pd93_mstfn | varchar | — | — | — | 維護人 |
| pd93_mdate | datetime | — | — | — | 維護日 |
