# ssorm10 — 訂單明細檔。記錄訂單中每位旅客的詳細資料，包含姓名、護照、房型、費用明細等核心資訊

**Aliases**: 訂單明細檔, ssorm10, SSORM10
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| orer_ordr | varchar | — | PK | ssorm00.ordr_ordr | 訂單編號 |
| orer_year | varchar | — | — | ssorm00.ordr_year | 訂單年度 |
| orer_seq | int | — | — | — | 訂單明細序號（旅客流水號） |
| orer_sts | bit | — | — | — | 已取消（1=已取消） |
| orer_cname | varchar | — | — | — | 中文姓名（中/英文名必 key 其一） |
| orer_ename | varchar | — | — | — | 英文名（First Name） |
| orer_enamel | varchar | — | — | — | 英文姓（Last Name） |
| orer_etit | varchar | — | — | — | 稱謂（M=大人, C=CHD 12歲以下, I=INF 2歲以下） |
| orer_sex | varchar | — | — | — | 性別（M/F） |
| orer_bdate | datetime | — | — | — | 出生日期 |
| orer_country | varchar | — | — | — | 國籍別 |
| orer_idno | varchar | — | — | — | 身份證字號 |
| orer_visa | varchar | — | — | — | OP PPT收件（_=未收, Y=OP收件, X=自帶, S=送機, C=影本） |
| orer_visa_cn | varchar | — | — | — | OP台胞收件（_=未收, Y=OP收件, X=自帶, S=送機） |
| orer_draftee | bit | — | — | — | 役男（是役男，已提醒客人去蓋章後再點掉） |
| orer_ename_err | bit | — | — | — | 英文姓名不符規則（空白、姓及名都低於(含)兩個字母，且字母都相同；取消 set 0） |
| orer_room | varchar | — | — | — | 團體分房 |
| orer_room_desc | varchar | — | — | — | 房型 |
| orer_amark | varchar | — | — | — | 佔床（1=佔床, 2=不佔, 3=加床） |
| orer_act | varchar | — | — | — | 房型（出團: local團依團價可挑, 其他固定=2） |
| orer_amt1 | decimal | — | — | — | 團費（團費已不含 Ecash） |
| orer_amt2 | decimal | — | — | — | 特別行程 |
| orer_amt3 | decimal | — | — | — | 證照 |
| orer_amt4 | decimal | — | — | — | 手續費機場稅 |
| orer_amt5 | decimal | — | — | — | 產品部成本 |
| orer_amt6 | decimal | — | — | — | Local團餐費 |
| orer_amt7 | decimal | — | — | — | Local團自費活動節目費 |
| orer_tot_amt | decimal | — | — | — | 總團費(含GST 不含退佣) |
| orer_gst | decimal | — | — | — | GST稅額（以上費用 * 訂單GST% 金額, Invoice時用） |
| orer_ecash | decimal | — | — | — | 抵用Ecash金額 |
| orer_kb1 | decimal | — | — | — | 同業退佣金額（原 agentcomm） |
| orer_addgst | varchar | — | — | — | 加稅（A=其他券... (9=只剩舊資料)） |
| orer_pmark | varchar | — | — | — | 價格（1=團, 2=TL, 3=FOC, 4=房, 5=自由行, 6=TKT, 7=JOIN/證照, 9=雄獅） |
| orer_pmarkdesc | varchar | — | — | — | ??（（欄位用途待確認）） |
| orer_pnr0 | varchar | — | — | — | 國際段Pnr（每個客人最多2個PNR，勾選完上傳=TL/FOC必須馬上上傳） |
| orer_pnr1 | varchar | — | — | — | 中段Pnr（因欄位不是1對多，不立即處理怕User弄錯，而造成上傳名單不對） |
| orer_pnr_tl | bit | — | — | — | 上傳名單是TL |
| orer_pnr_foc | bit | — | — | — | 上傳名單是FOC |
| orer_tairline | varchar | — | — | FK → Istbm00 (TAIRLINE) | 代訂北高 |
| orer_tpnr | varchar | — | — | — | 電代 |
| orer_tdesc | varchar | — | — | — | 開票備註 |
| orer_station1 | varchar | — | — | — | 上車地點代碼（沒輸入時，以訂單head為主） |
| orer_station1_desc | varchar | — | — | — | 特殊上車地點（由OP輸入印到報表） |
| orer_station2 | varchar | — | — | — | 下車地點代碼 |
| orer_station2_desc | varchar | — | — | — | 特殊下車地點 |
| orer_off | bit | — | — | — | 是否脫隊（1=脫隊） |
| orer_nmark | varchar | — | — | — | 不宜參團註記（Null=無, 1=比對(ID)是, 2=模糊比對(姓名+電話)是） |
| orer_chgname | varchar | — | — | — | 入名單資料異動 |
| orer_chgnamedate | datetime | — | — | — | 資料異動(最後)時間（當團體入名單日更新時，則清除本團所有這2個欄位，重新記錄） |
| orer_max | int | — | — | — | INB人數（Inbound團直接輸入人數（海外ERP）） |
