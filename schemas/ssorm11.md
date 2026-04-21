# ssorm11 — 訂單明細副檔。記錄訂單旅客的詳細聯絡資訊、護照資料、緊急聯絡人、補助金申請等附加資料

**Aliases**: 訂單明細副檔, ssorm11, ORM11, SSORM11
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or11_ordr | varchar | — | PK | ssorm10.orer_ordr | 訂單編號 |
| or11_year | varchar | — | — | ssorm10.orer_year | 訂單年度 |
| or11_seq | int | — | — | ssorm10.orer_seq | 訂單明細序號 |
| or11_htel | varchar | — | — | — | 聯絡電話-住家 |
| or11_mtel | varchar | — | — | — | 聯絡電話-行動 |
| or11_otel | varchar | — | — | — | 聯絡電話-公司 |
| or11_email | varchar | — | — | — | E-MAIL |
| or11_email_send | bit | — | — | — | 接受電子報（(0) 1=接受） |
| or11_address | varchar | — | — | — | 地址 |
| or11_postcode | varchar | — | — | — | 郵遞區號 |
| or11_urgent_name | varchar | — | — | — | 緊急聯絡人 |
| or11_urgent_relman | varchar | — | — | FK → Istbm00 (RELMAN) | 與緊急聯絡人關係 |
| or11_urgent_htel | varchar | — | — | — | 緊急聯絡人聯絡電話-住家 |
| or11_urgent_mtel | varchar | — | — | — | 緊急聯絡人聯絡電話-行動 |
| or11_urgent_otel | varchar | — | — | — | 緊急聯絡人聯絡電話-公司 |
| or11_pssprt | varchar | — | — | — | 護照號碼 |
| or11_pidate | datetime | — | — | — | 護照生效日期 |
| or11_pvdate | datetime | — | — | — | 護照到期日期 |
| or11_pplace | varchar | — | — | — | 發照地 |
| or11_visa_cn | varchar | — | — | — | 台胞證號碼 |
| or11_date_cn | datetime | — | — | — | 台胞證效期 |
| or11_visa_cntimes | varchar | — | — | — | 台胞證次數（新增 2024/05/02） |
| or11_visa2_cn | varchar | — | — | — | 入台證號 |
| or11_meat | varchar | — | — | FK → Istbm00 (MEAT) | 特殊飲食 |
| or11_al_card | varchar | — | — | — | 航空公司會員卡號 |
| or11_room | varchar | — | — | — | 業務分房 |
| or11_op_desc | varchar | — | — | — | OP分房表備註說明 |
| or11_desc | varchar | — | — | — | 業務備註說明 |
| or11_tkseq | varchar | — | — | — | 機票號碼（For 長榮點券記錄每位客人的票號） |
| or11_helpstfn | varchar | — | — | — | 補助金申請員工碼（B2E訂單才要用，資料很少） |
| or11_helpname | varchar | — | — | — | 補助金申請員工姓名 |
| or11_helpamt | decimal | — | — | — | 補助金金額 |
| or11_help | bit | — | — | — | 補助金核准狀況（1=核准，尚未：累計到主檔，cxl旅客後累計要扣除） |
| or11_helpfamt | decimal | — | — | — | 補助金核准金額（For 雄獅員工團申請補助，helpamt=null，要申請set on） |
| or11_helpman | varchar | — | — | — | 補助金審核人員 |
| or11_helpdate | datetime | — | — | — | 補助金審核日期 |
| or11_helpdesc | varchar | — | — | — | 補助金審核備註 |
