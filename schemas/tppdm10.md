# tppdm10 — 團體主檔。一個出發日的團體資料（核心主檔）

**Aliases**: 團體主檔, tppdm10, PDM10, TPPDM10
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| prod_prod | varchar | — | PK | — | 團號 |
| prod_prodcomp | varchar | — | — | — | 團控公司 |
| prod_line | varchar | — | — | — | 線別 |
| prod_dline | varchar | — | — | — | 副線別 |
| prod_days | int | — | — | — | 天數 |
| prod_0hotel | bit | — | — | — | 夜未眠（1=夜未眠行程，前台等同1天local行程，應無旅館檔資料） |
| prod_area | varchar | — | — | — | 地區 |
| prod_darea | varchar | — | — | — | 細地區 |
| prod_name | varchar | — | — | — | 標準團名 |
| prod_b2pname | varchar | — | — | — | 企業(B2P)團名（給內部看如:景文美東; 國旅9z 加show前台） |
| prod_project | varchar | — | — | istbm00 | 專案代號 |
| prod_tur2 | varchar | — | — | — | 行程編號 |
| prod_html_date | datetime | — | — | — | 行程更新異動時間（Null=表示尚未產生行程網頁） |
| prod_sts | char(1) | — | — | — | 團型（1=outb團, 2=票團, 3=外丟, 4=商務, 5=Inb, 6=Local） |
| prod_full | char(1) | — | — | — | 團控狀況（C=結, L=鎖, M=挪, V=取消） |
| prod_ctrl | varchar | — | — | — | 團控說明（U=急, G=必走（存檔以中文存入）） |
| prod_go | bit | — | — | — | 保證出團（1=保證出團） |
| prod_packairp | bit | — | — | — | 包機團（當包機時等同保證出團，故設保證出團=1） |
| prod_grouptype | char(1) | — | — | — | 團類別（S=系列團, C=客製團） |
| prod_down | bit | — | — | — | 直客可降售價（不能down價時，前台show特惠） |
| prod_downa | bit | — | — | — | 同業可降售價 |
| prod_amt_w | decimal | — | — | — | 大人批售價（由tppdm90 io存入，以便search少join） |
| prod_amt_d | decimal | — | — | — | 大人直售價 |
| prod_minamt_w | decimal | — | — | — | 最低大人批售價 |
| prod_minamt_d | decimal | — | — | — | 最低大人直客價 |
| prod_fsts | bit | — | — | — | 售價審核（0=系統審核, 1=主管審核（主管審核過的不可複製）） |
| prod_unpriced | bit | — | — | — | 售價未定（售價未定時後台顯示「未定」，前台顯示「近期上架」） |
| prod_pay | decimal | — | — | — | 訂金（由tppdm90搬過來 pd90_pay） |
| prod_payfull | bit | — | — | — | 需全額付清(才能kk)（由tppdm90搬過來 pd90_payfull） |
| prod_payment | bit | — | — | — | 可信用卡分期付款（show ╳:不可分期） |
| prod_gmode3 | bit | — | — | — | 須立即付款（由pd16_gmode3 move，海外本次改show！:須立即付款，4Hr拉hk） |
| prod_isnotax | bit | — | — | — | 為未稅價格 |
| prod_gst_rate | decimal | — | — | — | 團GST稅率 |
| prod_gst_mdate | datetime | — | — | — | 團GST稅率更新日 |
| prod_viporigprice | decimal | — | — | — | 會員限購原價 |
| prod_groupvisa | bit | — | — | — | 辦團簽 |
| prod_option | bit | — | — | — | 有自費活動（Local團用，可選擇出發前選購） |
| prod_d0 | date | — | — | — | 實際成團日（FOR RC check報名人數，MSG TO業務收訂，當空白時未收款） |
| prod_d1 | date | — | — | — | 報名截止 |
| prod_d2 | date | — | — | — | 團簽截止 |
| prod_d4 | date | — | — | — | 預計開票日 |
| prod_d5 | date | — | — | — | 實際開票日 |
| prod_paydate1 | date | — | — | — | 付訂提醒日期1 |
| prod_paydate2 | date | — | — | — | 付訂提醒日期2 |
| prod_d6 | date | — | — | — | 訂團日 |
| prod_d62 | date | — | — | — | 訂團日2 |
| prod_d7 | date | — | — | — | 海外公司接團日（當台灣上訂團日，海外就可select到，同時在團旅館資料上接團日） |
| prod_d72 | date | — | — | — | 海外公司接團日2（海外接團開團時自動回寫） |
| prod_d8 | date | — | — | — | 出團日期 |
| prod_d9 | date | — | — | — | 回國日期 |
| prod_taxdate | date | — | — | — | 立帳日期（日處理凌晨撈當日回國的團寫入稅帳日=d9 (2012/05/31前為D8)；有對應outb團的inb團立帳日與outb團同；由台北會計副理級以上可做修改） |
| prod_obj1 | bit | — | — | — | 不可銷售（1=團費不符合估價，不可銷售） |
| prod_obj2 | bit | — | — | — | 銷售對象-會員 |
| prod_obj3 | bit | — | — | — | 銷售對象-企業b2p |
| prod_obj4 | bit | — | — | — | 銷售對象-同行b2b |
| prod_obj5 | bit | — | — | — | 銷售對象-內部 |
| prod_obj6 | bit | — | — | — | 銷售渠道BBC |
| prod_obj7 | bit | — | — | — | 銷售-會員限購 |
| prod_sfcountry | varchar | — | — | — | 前台搜尋-出發國家代碼（Inb團交付的agent所在國城，提供經營分析用） |
| prod_sfcity1 | varchar | — | — | — | 前台搜尋-出發城市代碼1 |
| prod_sfcity2 | varchar | — | — | — | 前台搜尋-出發城市代碼2 |
| prod_sfcity3 | varchar | — | — | — | 前台搜尋-出發城市代碼3 |
| prod_sfcity4 | varchar | — | — | — | 前台搜尋-出發城市代碼4 |
| prod_sfcity5 | varchar | — | — | — | 前台搜尋-出發城市代碼5 |
| prod_webarea | varchar | — | — | Tptbm20.tb20_webarea | 前台目的地（BI分析用） |
| prod_form | varchar | — | — | FK → Istbm00 (FORM) | 旅遊契約書 |
| prod_cform | varchar | — | — | — | 艙房訂購合約書代碼 |
| prod_bu | varchar | — | — | — | 團控集團 |
| prod_country | varchar | — | — | — | 團控雄獅 |
| prod_prof | varchar | — | — | — | 團控單位 |
| prod_tprof | varchar | — | — | — | 機票單位 |
| prod_tagent | varchar | — | — | — | 機票外調法人代碼 |
| prod_carr | varchar | — | — | — | 機票航空公司 |
| prod_njprof | varchar | — | — | — | 包團單位 |
| prod_njhagent | varchar | — | — | — | 包團法人代碼（現在是agent-code opagm00，原本是opagm05） |
| prod_bprof | varchar | — | — | — | 接團單位 |
| prod_bprof2 | varchar | — | — | — | 接團單位2 |
| prod_local1 | varchar | — | — | — | LOCAL代號1 |
| prod_local2 | varchar | — | — | — | LOCAL代號2 |
| prod_max | int | — | — | — | 團位 |
| prod_min | int | — | — | — | 追加機位 |
| prod_qhk | int | — | — | — | 可候補（額滿有候補數，排HK<可候補人數時，前台出現【候補】可下單） |
| prod_tl | int | — | — | — | 領隊人數（出團至少要一人） |
| prod_base | int | — | — | — | 成團機位數（For團票最低開票機位量，檢核時不含join，再配合成團日） |
| prod_pak | int | — | — | — | PAK團人數 |
| prod_keep | int | — | — | — | 保留團人數 |
| prod_infseat | bit | — | — | — | 嬰兒佔團位 |
| prod_offrate | decimal | — | — | — | 脫隊成團人數%（for機位控管用） |
| prod_offmax | int | — | — | — | 脫隊最多人數 |
| prod_tp | varchar | — | — | — | TP員編 |
| prod_rc | varchar | — | — | — | RC員編（開團者，可修改，主要接MSG） |
| prod_team | varchar | — | — | — | 團體組別（售價審核完成時留言通知的對象） |
| prod_tpstfn | varchar | — | — | — | 異動者員編（基本資料及售價增修時寫入，審核售價時不可審核自己增修的團） |
| prod_stopq | bit | — | — | — | OP鎖Q |
| prod_qop | bit | — | — | — | Q信箱提醒OP |
| prod_lock | bit | — | — | — | 財務鎖團帳 |
| prod_okname | date | — | — | — | 入名單日（當重入名單日後，訂單明細旅客的異動欄會清空，重新再記異動項；異動的記錄logssorm10） |
| prod_okroom | date | — | — | — | 分房完成日 |
| prod_itin | bit | — | — | — | itin表維護（itin備註存檔回寫） |
| prod_okitin | bit | — | — | — | itin表完成（itin備註勾完成回寫，勾完成或完成取消皆會通知outB OP） |
| prod_opairfg | varchar | — | — | — | OP面交送機人員勾選信息 |
| prod_ok19 | bit | — | — | — | 完成滿意度計算（計算完成後回寫 true） |
| prod_re19 | bit | — | — | — | 重新計算滿意度（1=本團意調表有更新存檔；當1時日處理須重新計算本團滿意度，計算後歸0） |
| prod_mstfn | varchar | — | — | — | 增修者單位姓名時區（單位+姓名+空格+時區 ex:直團王大明 TW） |
| prod_mdate | datetime | — | — | — | 當地增修日期 |
| prod_msysdate | datetime | — | — | — | 主機增修時間 |
| prod_tpform | varchar | — | — | tppcm40 | 估價代號 |
| prod_size | varchar | — | — | tppcm40 | 估價檔次 |
| prod_requ | varchar | — | — | — | 需求代碼（關聯需求單號） |
