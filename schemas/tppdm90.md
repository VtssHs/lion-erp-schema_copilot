# tppdm90 — 團體售價資料檔。團體的售價明細（多房型、多價格方式）

**Aliases**: 團體售價資料檔, 團體的售價明細, tppdm90, PDM90, TPPDM90
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd90_prod | varchar | — | — | tppdm10.prod_prod | 團號（**PK1**） |
| pd90_prodcomp | varchar | — | — | — | 團控公司（**PK2**） |
| pd90_kind | char(1) | — | — | — | 直批別（**PK3**, D=直客, W=批售） |
| pd90_pmark | char(1) | — | — | — | 價格方式（**PK4**, 1=售價, 6=TKT湊票, 7=JOIN（同訂單）） |
| pd90_act | char(1) | — | — | — | 房型（**PK5**, 見下方說明） |
| pd90_a | decimal | — | — | — | 大人售價（遊輪:第一人） |
| pd90_c1 | decimal | — | — | — | 小孩佔床售價（遊輪:第二人） |
| pd90_c2 | decimal | — | — | — | 小孩不佔床售價（遊輪:第三人） |
| pd90_c3 | decimal | — | — | — | 小孩加床售價（遊輪:第四人） |
| pd90_i | decimal | — | — | — | 嬰兒售價（遊輪:嬰兒） |
| pd90_atax | decimal | — | — | — | 成人稅金 |
| pd90_c1tax | decimal | — | — | — | 小孩佔床稅金 |
| pd90_c2tax | decimal | — | — | — | 小孩不佔床稅金 |
| pd90_c3tax | decimal | — | — | — | 小孩加床稅金 |
| pd90_itax | decimal | — | — | — | 嬰兒稅金 |
| pd90_desc | nvarchar | — | — | — | 房型/備註 |
| pd90_pd98no | varchar | — | — | tppdm98 | 房價群組序號 |
