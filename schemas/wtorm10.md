# wtorm10 — 訂位單旅客資料檔。記錄網位單（訂位單）中每位旅客的個人資料，包含基本資料、證件、聯絡方式、費用明細、航空會員等

**Aliases**: 訂位單旅客資料檔, 網位單管理系統, 費用明細, wtorm10, WTORM10
**Database**: LionGroupERP
**Module**: 網位單管理系統 (Web Transaction Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| Wor10_wtordr | varchar | — | PK | wtorm00.Wor00_wtordr | 訂位單編號 |
| Wor10_wtyear | varchar | — | — | wtorm00.Wor00_wtyear | 訂位單年碼 |
| Wor10_seq | int | — | — | — | 序號（旅客流水號） |
| Wor10_cname | varchar | — | — | — | 中文姓名 |
| Wor10_ename | varchar | — | — | — | 英文名（First Name） |
| Wor10_enamel | varchar | — | — | — | 英文姓（Last Name） |
| Wor10_etit | varchar | — | — | — | 稱謂（A/M=大人; C=小孩; I=嬰兒; O=老人; P=殘障; Q=金門籍（特殊用）） |
| Wor10_sex | varchar | — | — | — | 性別（M=男; F=女） |
| Wor10_birth | datetime | — | — | — | 生日 |
| Wor10_country | varchar | — | — | — | 國籍 |
| Wor10_idno | varchar | — | — | — | 身份證字號 |
| Wor10_email | varchar | — | — | — | E-Mail |
| Wor10_htel | varchar | — | — | — | 聯絡電話-家裡 |
| Wor10_mtel | varchar | — | — | — | 聯絡電話-手機 |
| Wor10_otel | varchar | — | — | — | 聯絡電話-公司 |
| wor10_addr | varchar | — | — | — | 居住地址 |
| wor10_city | varchar | — | — | — | 居住城市 |
| wor10_state | varchar | — | — | — | 居住州別 |
| wor10_country2 | varchar | — | — | — | 居住國家 |
| wor10_world | varchar | — | — | — | 居住洲別 |
| wor10_postcode | varchar | — | — | — | 郵遞區號 |
| wor10_addr2 | varchar | — | — | — | 加入會員的地址 |
| Wor10_pssprt | varchar | — | — | — | 護照號碼 |
| wor10_pssprt_country | varchar | — | — | — | 發照國家 |
| wor10_pssprt_tdate | datetime | — | — | — | 證照效期 |
| wor10_pssprt_type | varchar | — | — | — | 證照型式（0=護照; 1=台胞證; 2=港澳回鄉證; 3=大陸地區往來人民通行證） |
| wor10_pssprt2 | varchar | — | — | — | 加入會員的證照號碼 |
| wor10_pssprt2_type | varchar | — | — | — | 加入會員的證照型式（0=護照; 1=台胞證; 2=港澳回鄉證; 3=大陸地區往來人民通行證） |
| wor10_pssprt3 | varchar | — | — | — | 易行證照號碼（0=身份; 1=护照; 2=军人证; 3=台胞证; 4=回乡证; 5=文职证） |
| wor10_pssprt3_type | varchar | — | — | — | 易行證照類型 |
| Wor10_tkno | varchar | — | — | — | 票號 |
| Wor10_tkseq | varchar | — | — | — | 機票號碼 |
| wor10_tkperiod | varchar | — | — | FK → Istbm00 (TKPERIOD) | 票期 |
| wor10_segment | varchar | — | — | — | 開票航段（多航段以 `/` 區隔） |
| wor10_pnr | varchar | — | — | — | PNR |
| wor10_carr | varchar | — | — | — | 航空公司（用途待確認） |
| Wor10_carr1 | varchar | — | — | — | 航空公司會員卡1 |
| Wor10_carr2 | varchar | — | — | — | 航空公司會員卡2 |
| Wor10_al_card1 | varchar | — | — | — | 航空公司卡號1 |
| Wor10_al_card2 | varchar | — | — | — | 航空公司卡號2 |
| wor10_carr_member | varchar | — | — | — | 同意加入航空會員（1=同意） |
| Wor10_amt | decimal | — | — | — | 未含稅及加價金額 |
| Wor10_tot_amt | decimal | — | — | — | 總金額 |
| Wor10_discount | decimal | — | — | — | 折扣 |
| wor10_ecash | decimal | — | — | — | 抵用 ecash 金額（自由行使用，總金額不含 ecash） |
| Wor10_cost | decimal | — | — | — | 票價成本 |
| Wor10_tax1 | decimal | — | — | — | 機場稅金 |
| Wor10_tax2 | decimal | — | — | — | 兵險稅金 |
| Wor10_tax3 | decimal | — | — | — | 燃料稅金 |
| Wor10_add_amt1 | decimal | — | — | — | 週末加價 |
| Wor10_add_amt2 | decimal | — | — | — | 月票加價 |
| Wor10_add_amt3 | decimal | — | — | — | 年票加價 |
| Wor10_add_amt4 | decimal | — | — | — | 期間加價 |
| wor10_b2bpoint | decimal | — | — | — | B2B點數 |
| Wor10_pmark | varchar | — | — | — | 價格方式（1=一般; 3=FOC） |
| wor10_amtkind | varchar | — | — | — | 房價類別 |
| Wor10_hotelseq | varchar | — | — | — | 房型 |
| wor10_room | varchar | — | — | — | 分房 |
| wor10_room_dist | varchar | — | — | — | 分房用途待確認 |
| wor10_hor31descseq | varchar | — | — | — | 用途待確認 |
| Wor10_ssr1 | varchar | — | — | — | 特殊需求1 |
| Wor10_ssr2 | varchar | — | — | — | 特殊需求2 |
| wor10_trans_us | varchar | — | — | — | 在美國轉機前往第三地（1=在美國轉機） |
| wor10_us | varchar | — | — | — | 美國身份種類（0=非公民也沒居留證; 1=是公民; 2=有居留證） |
| Wor10_YXSts | varchar | — | — | — | 易行狀態 |
| wor10_add | varchar | — | — | — | 用途待確認 |
