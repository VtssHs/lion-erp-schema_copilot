# tppdm16 — 團體副檔。團體主檔的擴充資料，涵蓋簽證、費用包含、旅遊契約、保險、交班表等詳細設定

**Aliases**: 團體副檔, tppdm16, PDM16, TPPDM16
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd16_prod | varchar(10) | — | PK | tppdm10.prod_prod | 團號 |
| pd16_prodcomp | varchar(2) | — | — | — | 團控公司 |
| pd16_vscountry1 | varchar(3) | — | — | FK → 國家代碼表 | 團體所需簽證-國家代碼 |
| pd16_vsseq1 | varchar(3) | — | — | FK → 簽證類型表 | 團體所需簽證-代碼 |
| pd16_vsinc1 | char(1) | — | — | — | 團費是否包含簽證費（Y=包含, N=不包含） |
| pd16_vsfdate1 | datetime | — | — | — | 簽證使用起日 |
| pd16_vstdate1 | datetime | — | — | — | 簽證使用訖日 |
| pd16_vscountry2 | varchar(3) | — | — | FK → 國家代碼表 | 團體所需簽證-國家代碼 |
| pd16_vsseq2 | varchar(3) | — | — | FK → 簽證類型表 | 團體所需簽證-代碼 |
| pd16_vsinc2 | char(1) | — | — | — | 團費是否包含簽證費（Y=包含, N=不包含） |
| pd16_vsfdate2 | datetime | — | — | — | 簽證使用起日 |
| pd16_vstdate2 | datetime | — | — | — | 簽證使用訖日 |
| pd16_visa_i | varchar(500) | — | — | — | 包簽證費（前台顯示內容） |
| pd16_visa_idesc | varchar(500) | — | — | — | 包簽證費說明（詳細說明） |
| pd16_visa_n | varchar(500) | — | — | — | 不包簽證費（前台顯示內容） |
| pd16_visa_ndesc | varchar(500) | — | — | — | 不包簽證費說明（詳細說明） |
| pd16_airp_i | varchar(500) | — | — | — | 包機場稅費（前台顯示內容） |
| pd16_airp_idesc | varchar(500) | — | — | — | 包機場稅費說明（詳細說明） |
| pd16_airp_n | varchar(500) | — | — | — | 不包機場稅費（前台顯示內容） |
| pd16_airp_ndesc | varchar(500) | — | — | — | 不包機場稅費說明（詳細說明） |
| pd16_tick_n | varchar(500) | — | — | — | 湊票不包機場稅費（湊票專用） |
| pd16_tick_ndesc | varchar(500) | — | — | — | 湊票不包機場稅費說明 |
| pd16_meat_a | decimal(10,2) | — | — | — | Local團不含大人餐費（金額） |
| pd16_meat_c | decimal(10,2) | — | — | — | Local團不含小孩餐費（金額） |
| pd16_desc1 | text | — | — | — | 直客 B2C 備註（前台顯示給一般消費者） |
| pd16_desc4 | text | — | — | — | 同行 B2B 備註（顯示給旅行同業） |
| pd16_desc | text | — | — | — | 內部備註（僅內部系統可見） |
| pd16_tpdesc | text | — | — | — | 售價說明（由產品人員填寫，提供主管審核售價時參考） |
| pd16_cxl_desc | text | — | — | — | 取消說明（取消政策說明） |
| pd16_booking_desc | text | — | — | — | 預訂說明（預訂須知） |
| pd16_shiftdesc | text | — | — | — | 交班表備註（交班表專用備註） |
| pd16_n1 | char(1) | — | — | — | 護照費用（空白=未確定, Y=包含, N=不包含） |
| pd16_n2 | char(1) | — | — | — | 簽證費用（空白=未確定, Y=包含, N=不包含） |
| pd16_n3 | char(1) | — | — | — | 台灣機場稅（空白=未確定, Y=包含, N=不包含） |
| pd16_n4 | char(1) | — | — | — | 兵險及燃油費（空白=未確定, Y=包含, N=不包含） |
| pd16_n5 | char(1) | — | — | — | 中正/小港機場接送費（往返中正/小港機場之一切接送費用） |
| pd16_n6 | char(1) | — | — | — | 服務人員小費（團體=領隊, 個人=導遊及其他服務人員之服務小費） |
| pd16_n7 | char(1) | — | — | — | 機場與旅館接送費（團體=無, 個人=旅遊期間機場、港口、車站等與旅館間接送費用） |
| pd16_n8 | char(1) | — | — | — | 國外機場稅（國旅團只有 n6、n7 兩項） |
| pd16_cxl1 | bit | — | — | — | 屬包機團（1=印到契約書上） |
| pd16_cxl2 | bit | — | — | — | 屬遊輪產品（1=啟用郵輪條款） |
| pd16_cxl3 | bit | — | — | — | 含觀光列車（1=啟用鐵路條款） |
| pd16_cxl4 | bit | — | — | — | 含保證住房旅館（1=啟用住房保證條款） |
| pd16_cxl5 | bit | — | — | — | 含特殊表演門票（1=啟用表演票券條款） |
| pd16_cxl6 | bit | — | — | — | 含特殊競賽門票（1=啟用競賽票券條款） |
| pd16_cxl7 | bit | — | — | — | Club Med 契約加註（1=啟用 Club Med 專屬條款） |
| pd16_cxl8 | bit | — | — | — | 郵輪旅遊契約加註（1=啟用郵輪旅遊專屬條款） |
| pd16_pakname | varchar(50) | — | — | — | 聯合出團名稱（與其他旅行社聯營時使用） |
| pd16_pakagent | varchar(50) | — | — | — | 出團旅行社（實際出團的旅行社名稱） |
| pd16_safeno | varchar(20) | — | — | — | 保險證號（國泰保險上傳資料用） |
| pd16_safeseq | varchar(10) | — | — | — | 保險收件序號 |
| pd16_safecode | varchar(10) | — | — | FK → 保險承辦單位代碼表 | 承辦單位 |
| pd16_safedate | datetime | — | — | — | 保險起時（保險生效時間） |
| pd16_safemode | varchar(10) | — | — | FK → 交通工具代碼表 | 交通工具 |
| pd16_saferate | decimal(10,4) | — | — | — | 保險費率 |
| pd16_safedays | int | — | — | — | 保險天數 |
| pd16_SafePolicyUrl | varchar(500) | — | — | — | 保單列印及下載 URL |
| pd16_SafeInsComp | varchar(10) | — | — | FK → 保險公司代碼表 | 投保對象代碼 |
| pd16_prod2 | varchar(10) | — | — | — | 併到團號投保（合併上傳保險，設在線控團體聯結的台灣契約書裡面） |
| pd16_busline1 | varchar(20) | — | — | — | 觀巴去程路線（用於觀巴行程控車位） |
| pd16_busline2 | varchar(20) | — | — | — | 觀巴回程路線 |
| pd16_5rptno | varchar(30) | — | — | — | 出境大陸地區申報電子編號（大陸線用，向移民署申報） |
| pd16_90mstfn | varchar(50) | — | — | — | 價格維護者單位姓名時區（格式: "單位+姓名+空格+時區" ex: "直團王大明 TW"） |
| pd16_90mdate | datetime | — | — | — | 價格當地維護日期 |
| pd16_90msysdate | datetime | — | — | — | 價格主機時間 |
| pd16_snapdate | datetime | — | — | — | 解鎖時間（團控解鎖時間戳記） |
| pd16_godate | datetime | — | — | — | 成團勾選時間（確認成團的時間） |
| pd16_demandcode | varchar(20) | — | — | FK → istbm81 (DEMANDLIST) | 需求單對應代碼 |
| pd16_shiftcheck | varchar(100) | — | — | — | 交班表報到時間（前台顯示給客人的報到時間） |
| pd16_shiftmeet | varchar(200) | — | — | — | 交班表集合時間地點（詳細集合資訊） |
| pd16_checkin_no | varchar(20) | — | — | — | 報到區號碼（機場報到櫃檯區號） |
