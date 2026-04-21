# wtorm00 — 訂位單主檔。網位單（網路訂位單）的主檔，涵蓋機票、自由行、訂房、票券、高鐵等多種訂單型態的共用主檔結構

**Aliases**: 訂位單主檔, 網位單管理系統, 網位單的主檔, wtorm00, WTORM00
**Database**: LionGroupERP
**Module**: 網位單管理系統 (Web Transaction Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| Wor00_ordr | varchar | — | PK | — | ERP訂位單編號 |
| Wor00_year | varchar | — | PK | — | ERP訂位單年碼 |
| Wor00_wtordr | varchar | — | — | — | 訂位單編號 |
| Wor00_wtyear | varchar | — | — | — | 訂位單年碼（＊每種訂單不同使用） |
| Wor00_oldsn | varchar | — | — | — | 舊訂單編號 |
| Wor00_fsts | varchar | — | — | — | 訂單型態（空白=訂位; 2=B2B開票; 3=自由行; 7=新自由行; 4=訂房; 8=券; 9=搶購單; 6=估價; A=高鐵票） |
| Wor00_fsts2 | varchar | — | — | — | 訂單次型態/付款方式（機票: 1=立即網刷並開票 2=客人自行開票 3=業務自行開票; 自由行: T=B2B有Pnr請雄獅代開票; 訂房: 0=保證住房 1=保留房（有值=應立即付款，滿1hr無網刷則自動cxl）） |
| Wor00_sts | bit | — | — | — | 已取消 |
| Wor00_sts1 | varchar | — | — | — | 人工需求單 |
| Wor00_flow | varchar | — | — | — | 處理進度（空白=未處理; 1=處理中; F=處理完成; G=開票） |
| Wor00_opsts | varchar | — | — | — | OP處理進度（Null=業務可改; F=產品部處理中（產品資料不可改）） |
| Wor00_close | bit | — | — | — | 已關閉前台查詢（因客戶要求關閉前台訂單查詢） |
| Wor00_date | datetime | — | — | — | 下單時間 |
| Wor00_fdate | datetime | — | — | — | 出發日 / 入住日 |
| Wor00_sdate | datetime | — | — | — | 出發日（機票/訂房 sdate=fdate; 自由行 sdate=交通段出發日） |
| Wor00_tdate | datetime | — | — | — | 回程日 / 退房日 |
| Wor00_chkdate | datetime | — | — | — | 機票開票期限（依下單及出發日計算最晚應開票日；出發-下單日 0~7天=下單日+3天；8~30天=下單日+7天；31天以上=出發日-20天；超期未完成由日處理自動CXL單及PNR） |
| wor00_cxldate | datetime | — | — | — | 取消時間 |
| Wor00_con_name | varchar | — | — | — | 聯絡人姓名 |
| Wor00_idno | varchar | — | — | — | 聯絡人身份證 |
| Wor00_con_email | varchar | — | — | — | E-mail |
| Wor00_con_mtel | varchar | — | — | — | 行動電話 |
| Wor00_con_tel | varchar | — | — | — | 公司電話-電話號碼 |
| Wor00_con_tel_1 | varchar | — | — | — | 公司電話-城市區碼 |
| Wor00_con_tel_3 | varchar | — | — | — | 公司電話-分機 |
| Wor00_con_tel_country | varchar | — | — | — | 電話國碼（全球訂單時使用） |
| Wor00_con_tel2 | varchar | — | — | — | 住家電話-電話號碼 |
| Wor00_con_tel2_1 | varchar | — | — | — | 住家電話-城市區碼 |
| wor00_con_fax | varchar | — | — | — | 傳真 |
| Wor00_act1 | int | — | — | — | 大人人數 ＊（訂房: night數×房數=總RN） |
| Wor00_act2 | int | — | — | — | 小孩人數 ＊（訂房: night數） |
| Wor00_act3 | int | — | — | — | 嬰兒人數（訂房: 以下欄位皆無用） |
| Wor00_act4 | int | — | — | — | 老人人數 |
| Wor00_foc | int | — | — | — | FOC人數 |
| wor00_qty | varchar | — | — | — | 數量（格式各產品前後台統一即可；Ex: 訂房「2間1晚」；也可存入產品名） |
| Wor00_amt | decimal | — | — | — | 未含稅及加價金額（自由行: 訂單小計（未扣退佣）） |
| Wor00_tot_amt | decimal | — | — | — | 總金額（自由行: 總金額 = amt – discount – add_amt1） |
| wor00_tot_amt2 | decimal | — | — | — | 設定網刷金額（高鐵: 總金額 = amt – discount） |
| Wor00_discount | decimal | — | — | — | 折扣（自由行: 同行退佣；高鐵: 刷卡折扣金額（折扣1應為明細檔加總）） |
| wor00_discount2 | decimal | — | — | — | 折扣 2（整張訂單行銷折扣，只記錄在 head，總金額再減折扣2） |
| wor00_ecash | decimal | — | — | — | 抵用 ecash 金額（自由行使用，總金額不含 ecash） |
| Wor00_tax1 | decimal | — | — | — | 機場稅金 |
| Wor00_tax2 | decimal | — | — | — | 兵險稅金 / 高鐵折扣（高鐵專案兆豐卡9折優惠價） |
| Wor00_tax3 | decimal | — | — | — | 燃料稅金 |
| Wor00_add_amt1 | decimal | — | — | — | 週末加價（自由行: 其他加價小計） |
| Wor00_add_amt2 | decimal | — | — | — | 月票加價 |
| Wor00_add_amt3 | decimal | — | — | — | 年票加價 |
| Wor00_add_amt4 | decimal | — | — | — | 期間加價 |
| Wor00_cost | decimal | — | — | — | 成本（票單轉線8時有值） |
| Wor00_cost2 | decimal | — | — | — | 成本2（用途待確認） |
| Wor00_cost2_curr | varchar | — | — | — | 成本2幣別（用途待確認） |
| Wor00_paykind | varchar | — | — | — | 付款方式（A=ATM; B=收到切結書; D=線上切結; C=線上刷卡; F=傳真刷卡; 4=分期; T=匯款（目前只有B2B For經案有假的）; P=到店付款） |
| wor00_payment_desc | varchar | — | — | — | 設定網刷金額說明（業務開放前台網刷金額不同時給 B2C 看的說明） |
| Wor00_getticket | varchar | — | — | — | 取票方式（M=掛號; P=親自; D=快遞; R=到站自取） |
| Wor00_etkt | varchar | — | — | — | 電子機票（1=開） |
| wor00_name | varchar | — | — | — | 產品名稱（名稱及數量供前後台訂單查詢用，不再 JOIN 產品檔；轉線8要存入） |
| Wor00_op | varchar | — | — | — | 產品OP |
| Wor00_prodprof | varchar | — | — | — | 產品單位 |
| Wor00_prof | varchar | — | — | — | 單位 |
| wor00_key1 | unknown | — | — | — | 對應其他檔KEY |
| wor00_key2 | unknown | — | — | — | 對應其他檔KEY |
| wor00_key3 | unknown | — | — | — | 對應其他檔KEY |
| wor00_key4 | unknown | — | — | — | 對應其他檔KEY |
| wor00_key5 | unknown | — | — | — | 對應其他檔KEY |
| Wor00_webcode | varchar | — | — | — | 來源（null=ERP後台/電話單） |
| Wor00_ordrin1 | varchar | — | — | FK → Istbm00 (ORDRIN1) | 報名方式（；app下單時記錄手機廠牌） |
| Wor00_ordrin2 | varchar | — | — | FK → Istbm00 (ORDRIN2) | 客人來源 |
| Wor00_tourist_origin | varchar | — | — | — | 客源地（2024/03/29 新增（申請單 24031627）） |
| Wor00_ip | varchar | — | — | — | 下單IP（過陣子可清除） |
| wor00_member_uid | varchar | — | — | — | 會員UID |
| wor00_b2bpoint | decimal | — | — | — | B2B點數 |
| Wor00_agent | varchar | — | — | — | 同行代碼（非B2B、B2E 時使用 U20083） |
| wor00_bu | varchar | — | — | isbum00 | 雄獅BU訂單 |
| Wor00_comp | varchar | — | — | — | 公司 |
| Wor00_comp2 | varchar | — | — | — | 物流公司（當自取時可設定） |
| Wor00_pcc | varchar | — | — | — | 區域號碼 |
| Wor00_sales | varchar | — | — | — | 業務人員 |
| Wor00_crs | varchar | — | — | FK → Istbm00 (CRSKIND) | 訂位系統 |
| Wor00_pnr | varchar | — | — | — | PNR代號 |
| Wor00_carr | varchar | — | — | — | 航空公司 |
| Wor00_open | varchar | — | — | — | 回程OPEN（1=開OPEN） |
| Wor00_table | varchar | — | — | — | 票價編號（機票訂單已改用 wor00_key2） |
| Wor00_tyear | varchar | — | — | — | 票價年碼（機票訂單已改用 wor00_key1） |
| wor00_jordr | varchar | — | — | — | 對接平台商代號 |
| wor00_jsts | varchar | — | — | — | 預訂狀態（GTA/HC用代碼；德比用英文敘述） |
| wor00_jtime | datetime | — | — | — | 預訂時間（Log記錄） |
| wor00_pordr | varchar | — | — | — | 供應商訂單編號 / 預訂單號（訂房對接；null=尚未對接；空白=開始預訂；其他值=預訂完成；GTA/HC 用 int；德比為英數夾雜） |
| Wor00_tkproj | varchar | — | — | — | 專案代碼（機票專案/訂房行銷活動/高鐵刷卡專案代碼；0030000=兆豐卡） |
| Wor00_tkproj_sts | varchar | — | — | — | 機票狀況 / 訂房保留房通知（訂房: 若有保留房於時限內網刷後以 mail 通知供應商時上 mark） |
| Wor00_tkproj2 | varchar | — | — | — | 專案代碼2（訂房: 網站下單為對接房時 set「對接」；會員訂單則不 show 付款連結） |
| Wor00_usp | varchar | — | — | — | USP註記（訂房: 由 usp 折扣活動頁進入；自由行住宿券: 0=未確認; 1=已確認） |
| wor00_cxldesc | varchar | — | — | FK → istbm00 (CXLDESC) | 取消原因代碼 |
| wor00_cxldesc2 | varchar | — | — | FK → istbm00 (CXLDESC2) | 未執行自行開票原因 |
| wor00_cxlstfn | varchar | — | — | — | 取消人（因開放B2B可作廢，故增加記錄） |
| wor00_apis | unknown | — | — | — | 已無用 |
| wor00_chktime | unknown | — | — | — | 已無用 |
| wor00_seat | unknown | — | — | — | 已無用 |
| xWor00_tkproj_desc | unknown | — | — | — | 機票說明（已無用） |
| xWor00_tkproj_item | unknown | — | — | — | 機票項目（已無用） |
