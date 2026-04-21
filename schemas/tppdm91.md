# tppdm91 — 產品分銷設定。設定每個出發團的分銷 BU 授權，控制哪個 BU 可以分銷此團，並記錄審核單位與組別

**Aliases**: 產品分銷設定, tppdm91, PDM91, TPPDM91
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd91_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| pd91_prodcomp | varchar | — | PK | — | 團號公司 |
| pd91_bu | varchar | — | — | isbum00.bu00_bu | BU 代碼 |
| pd91_prof | varchar | — | — | — | 審核單位 |
| pd91_team | varchar | — | — | — | 審核組別 |
| pd91_istfn | varchar | — | — | — | 新增者員編 |
| pd91_idate | datetime | — | — | — | 新增時間 |
| pd91_mstfn | varchar | — | — | — | 修改者員編 |
| pd91_mdate | datetime | — | — | — | 修改時間 |
