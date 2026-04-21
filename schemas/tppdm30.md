# tppdm30 — 團體產品行程異動記錄檔。記錄團體產品行程的異動狀態與備註

**Aliases**: 團體產品行程異動記錄檔, tppdm30, PDM30, TPPDM30
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd30_prod | varchar(12) | NOT NULL | — | tppdm10.tpdm10_geno | 團號 |
| pd30_prodcomp | varchar(2) | NOT NULL | — | — | 團號公司（雄獅/易遊識別碼） |
| pd30_chg_sts | varchar(10) | NOT NULL | — | — | 異動狀態（代碼待確認（tptbm/tptrm）） |
| pd30_chg_d8 | varchar(8) | NULL | — | — | 異動出團日（YYYYMMDD 格式） |
| pd30_desc | varchar(500) | NULL | — | — | 異動備註（自由文字說明） |
