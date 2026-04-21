# tppdm17 — 團體關連檔。記錄團與團之間的關聯關係（主團/子團、導領/接團/JOIN）

**Aliases**: 團體關連檔, tppdm17, PDM17, TPPDM17
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd17_prod | varchar | — | PK | tppdm10.prod_prod | 主團號（(part)） |
| pd17_prodcomp | varchar | — | — | — | 主團控公司 |
| pd17_chdprod | varchar | — | PK | tppdm10.prod_prod | 子團號（(part)） |
| pd17_chdprodcomp | varchar | — | — | — | 子團號公司 |
| pd17_type | char(1) | — | PK | — | 關聯型態（(part), **1**=導領(預設), **2**=接團, **3**=JOIN） |
| pd17_memo | varchar/text | — | — | — | 說明（關聯關係的補充說明） |
| pd17_idate | datetime | — | — | — | 新增日期（記錄建立時間） |
| pd17_istfn | varchar | — | — | — | 新增者員編（建立此關聯的員工代號） |
| pd17_mdate | datetime | — | — | — | 修改日期（最後修改時間） |
| pd17_mstfn | varchar | — | — | — | 修改者員編（最後修改者員工代號） |
