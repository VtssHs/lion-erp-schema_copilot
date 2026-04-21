# tppdm92 — 產品分銷上架設定。設定每個出發團在特定 BU 下的頻道上架細節，是 tppdm91（分銷設定）的下一層，細化到「BU × 頻道」的上架控制

**Aliases**: 產品分銷上架設定, tppdm92, PDM92, TPPDM92
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd92_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| pd92_prodcomp | varchar | — | PK | — | 團號公司 |
| pd92_bu | varchar | — | — | isbum00.bu00_bu | BU 代碼 |
| pd92_chl | varchar | — | — | isbum01.bu01_channel | 頻道 |
| pd92_istfn | varchar | — | — | — | 新增者員編 |
| pd92_idate | datetime | — | — | — | 新增時間 |
| pd92_mstfn | varchar | — | — | — | 修改者員編 |
| pd92_mdate | datetime | — | — | — | 修改時間 |
