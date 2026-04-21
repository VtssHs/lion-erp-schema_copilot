# ssorm00 — 訂單主檔。團體旅遊正式訂單主檔

**Aliases**: 訂單主檔, 團體旅遊正式訂單主檔, ssorm00, SSORM00
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| ordr_ordr | varchar | — | PK | — | 訂單號 |
| ordr_year | varchar | — | — | — | 訂單年度 |
| ordr_bu | varchar | — | — | — | BU (事業體) |
| ordr_code | varchar | — | — | — | 環境碼 |
| ordr_exordr | varchar | — | — | — | 外部訂單（外部系統訂單編號（新增 2025/02/26）） |
| ordr_wtordr | varchar | — | — | — | 關聯訂單流水號（關聯到其他訂單） |
| ordr_wtyear | varchar | — | — | — | 關聯訂單年 |
| ordr_wtbu | varchar | — | — | — | 關聯訂單BU（新增 2025/02/26） |
| ordr_wtcode | varchar | — | — | — | 關聯訂單環境碼（新增 2025/02/26） |
| ordr_wtsts | varchar | — | — | — | 關聯訂單來源或去處（0=團, 8=FIT 開TC票訂單） |
| ordr_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| ordr_line | varchar | — | — | — | 線別 |
| ordr_area | varchar | — | — | — | 地區 |
| ordr_name | varchar | — | — | — | 團名 |
| ordr_days | int | — | — | — | 天數 |
| ordr_adt | int | — | — | — | 大人人數 |
| ordr_chd | int | — | — | — | 小孩人數 |
| ordr_inf | int | — | — | — | 嬰兒人數 |
| ordr_tkt | int | — | — | — | 湊票人數 (不含Inf)（僅計算需票券的旅客） |
| ordr_tl | int | — | — | — | 領隊人數 |
| ordr_visa | int | — | — | — | 收件人數（目前含收件/自帶/送機） |
| ordr_amt | decimal | — | — | — | 訂單總金額 |
| ordr_tot_amt | decimal | — | — | — | 不含退佣總團費(票務總售價)（實際收款金額） |
| ordr_pay | decimal | — | — | — | 訂金 |
| ordr_balance | decimal | — | — | — | 尾款 |
| ordr_discount | decimal | — | — | — | 折扣金額 |
| ordr_cust | varchar | — | — | customer | 客戶代號 |
| ordr_custname | varchar | — | — | — | 客戶名稱 |
| ordr_custtel | varchar | — | — | — | 客戶電話 |
| ordr_custemail | varchar | — | — | — | 客戶Email |
| ordr_sales | varchar | — | — | FK → opagm20 (員工主檔) | 業務代號 |
| ordr_agent | varchar | — | — | FK → opagm00 (法人資料主檔) | 法人代號 |
| ordr_agentname | varchar | — | — | — | 法人名稱 |
| ordr_webcode | varchar | — | — | — | 網站來源（空白=非網上下單, B2C, B2E, B2B(z000), W007...） |
| ordr_source | varchar | — | — | — | 訂單來源（如：官網、門市、電話、APP） |
| ordr_channel | varchar | — | — | — | 銷售通路 |
| ordr_sts | varchar | — | — | — | 訂單狀態（N=新訂單, C=確認, X=取消, F=完成） |
| ordr_cancel | bit | — | — | — | 是否取消（1=已取消） |
| ordr_canceldate | datetime | — | — | — | 取消日期 |
| ordr_cancelreason | varchar | — | — | — | 取消原因 |
| ordr_paytype | varchar | — | — | — | 付款方式（C=信用卡, T=匯款, S=現金） |
| ordr_paydate | datetime | — | — | — | 付款日期 |
| ordr_paysts | varchar | — | — | — | 付款狀態（P=部分付款, F=全額付款, N=未付款） |
| ordr_cdate | datetime | — | — | — | 建立日期 |
| ordr_cuser | varchar | — | — | — | 建立人員 |
| ordr_mdate | datetime | — | — | — | 修改日期 |
| ordr_muser | varchar | — | — | — | 修改人員 |
