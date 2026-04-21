# tppdm11 — 出團行程檔。記錄每個出團檔次的人數統計資料

**Aliases**: 出團行程檔, tppdm11, PDM11, TPPDM11
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd11_prod | varchar | — | PK | tppdm10.prod_prod | 團號 |
| pd11_prodcomp | varchar | — | — | — | 團控公司 |
| pd11_hl | int | — | — | — | HL人數（不含 join，Inf 依 tppdm10.prod_infseat 決定） |
| pd11_qhk | int | — | — | — | 排HK人數（候補人數） |
| pd11_ob | int | — | — | — | OB人數 |
| pd11_hk | int | — | — | — | HK人數 |
| pd11_kk | int | — | — | — | KK人數 |
| pd11_act1 | int | — | — | — | 大人人數(全部訂單含join)（FOR 支出審核用） |
| pd11_act2 | int | — | — | — | 小孩人數(全部訂單含join) |
| pd11_act3 | int | — | — | — | 嬰兒人數(全部訂單含join) |
| pd11_tl | int | — | — | — | 領隊人數（價格條件=2） |
| pd11_foc | int | — | — | — | FOC人數（價格條件=3, Free of Charge） |
| pd11_tkt | int | — | — | — | 湊票人數不含Inf（價格條件=6） |
| pd11_join | int | — | — | — | Join人數（價格條件=7，Inf 依 tppdm10.prod_infseat 決定） |
| pd11_off | int | — | — | — | HKKK脫隊人數（已確認但脫隊的人數） |
| pd11_visa | int | — | — | — | OP收件人數（OP已收件的人數統計） |
| pd11_hotel | bit | — | — | — | 小房子已讀（OP 旅館配房完成標記） |
