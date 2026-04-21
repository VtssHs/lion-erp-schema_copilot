# iscpm00 — 公司主檔（供應商主檔）。前台公司下拉選單分類管理（如按地區/業務類型分組）

**Aliases**: 公司主檔, 供應商主檔, iscpm00, CPM00, ISCPM00
**Database**: LionGroupRPM
**Module**: ISCPM（Infrastructure System Company Master）

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| comp_comp | varchar(10) | — | PK | — | 公司代碼 |
| comp_cname | varchar(100) | — | — | — | 中文名稱（主要顯示名稱） |
| comp_ename | varchar(100) | — | — | — | 英文名稱 |
| comp_dname | varchar(100) | — | — | — | 顯示名稱（2014/7 原欄位保留，IT 設定資料用 增加多語系後角色調整） |
| comp_sname | varchar(50) | — | — | — | 報表內部簡稱（內部報表使用） |
| comp_sname2 | varchar(100) | — | — | — | 報表對外名稱（例：Booking Form） |
| comp_webname | varchar(100) | — | — | — | 網站上名稱（前台顯示名稱） |
| comp_address | varchar(200) | — | — | — | 公司地址 |
| comp_tel | varchar(50) | — | — | — | 電話 |
| comp_fax | varchar(50) | — | — | — | 傳真 |
| comp_man | varchar(50) | — | — | — | 負責人 |
| comp_invoice | varchar(20) | — | — | — | 統一編號（原 c8，澳洲稅局 inv 要印公司註冊號故加大 size） |
| comp_taxno | varchar(20) | — | — | — | 稅籍編號 |
| comp_register | varchar(50) | — | — | — | 證號（公司登記證號） |
| comp_country | varchar(10) | — | — | — | 所在國家（關聯 istbm00 國家代碼） |
| comp_city | varchar(10) | — | — | — | 所在城市（關聯 istbm00 城市代碼） |
| comp_difftime | int | — | — | — | 時差（與台北時間的時差（小時）） |
| comp_difftime2 | int | — | — | — | 當日時差（與 now() 計算當地維護時間） |
| comp_saveday | bit | — | — | — | 有日光節約日（是否實施夏令時間） |
| comp_localdate | date | — | — | — | 當地日期（日處理每整點算一次含當日時差） |
| comp_curr | varchar(3) | — | — | — | 使用幣別（如 TWD, USD, AUD） |
| comp_decimal | int | — | — | — | 小數位數（金額小數位設定） |
| comp_bu | varchar(10) | — | — | — | BU 代碼（Business Unit） |
| comp_ps | varchar(10) | — | — | — | 薪資公司（人事薪資歸屬公司） |
| comp_ship | varchar(1) | — | — | — | 關係企業（`M`=總公司, `B`=分公司, `C`=子公司, `R`=關係人） |
| comp_local | varchar(10) | — | — | — | 供應商代碼（當地供應商編號） |
| comp_agent | varchar(10) | — | — | — | 同行代號 |
| comp_sts | bit | — | — | — | 已停業（`1`=已停業, `0`=營運中） |
| comp_sts1 | bit | — | — | — | 可出團（`1`=可出團, `0`=不可出團） |
| comp_sts8 | bit | — | — | — | 門市，公司無業務（像忠孝、天母…方便在傳真表上加印實際所在地的公司資料） |
| comp_sts9 | bit | — | — | — | 限總帳(OBU)公司（在 ERP 不出現，像 OBU 公司只出現於總帳系統） |
| comp_order | int | — | — | — | 顯示順序（下拉選單排序用） |
| comp_logo | varchar(200) | — | — | — | Logo 圖檔（圖檔路徑） |
| comp_ar | date | — | — | — | 應收立帳日期（團結轉總帳完成日期/年月） |
| comp_ar_ym | varchar(6) | — | — | — | 應收立帳月（格式：YYYYMM） |
| comp_ar_date | date | — | — | — | 團訂單應收鎖帳日（結轉團應收立帳傳票月份的月底 例：結轉 2012/8，則為 20120831 訂單立帳日 <= 20120831 則訂單不能改 此公司開始結轉時就回寫此日期，結束時回寫為 null） |
| comp_ar_currym | varchar(6) | — | — | — | 應收外幣匯差月（每月結轉應收帳款外幣餘額匯差） |
| comp_ar_tk | date | — | — | — | TC 票-應收立帳日期（TC 票結轉總帳完成日期/年月） |
| comp_ar_tkym | varchar(6) | — | — | — | TC 票-應收立帳月 |
| comp_ar2 | date | — | — | — | TC 票-應收沖帳日期 |
| comp_ar2_ym | varchar(6) | — | — | — | TC 票-應收沖帳月 |
| comp_ap | date | — | — | — | 應付立帳日期 |
| comp_ap_ym | varchar(6) | — | — | — | 應付立帳月 |
| comp_ap_date | date | — | — | — | 團支單應付鎖帳日（結傳票月份的月底） |
| comp_ap_currym | varchar(6) | — | — | — | 應付外幣匯差月（每月結轉應付帳款外幣餘額匯差） |
| comp_ap_tk | date | — | — | — | TC 票-應付立帳日期 |
| comp_ap_tkym | varchar(6) | — | — | — | TC 票-應付立帳月 |
| comp_ap2 | date | — | — | — | TC 票-應付沖帳日期 |
| comp_ap2_ym | varchar(6) | — | — | — | TC 票-應付沖帳月（本頁以上欄位 for 自動結轉傳票所需 2006/11/1） |
| comp_tk_date | date | — | — | — | TC 票-應收付鎖帳日（結轉傳票月份的月底） |
| comp_io_ym | varchar(6) | — | — | — | 代轉結轉月（由台北執行，故只有台北有值） |
| comp_io_ym_t | varchar(6) | — | — | — | 旅遊雙品牌代轉結轉月（由台北執行，故只有台北有值） |
| comp_io_date | date | — | — | — | 代轉鎖帳日（出團公司開始印會計代轉時寫入 立帳月訖日，直到代轉月結印完清成 null） |
| comp_io_chk | varchar(6) | — | — | — | 代轉核對完成月（分公司代轉，若該分公司代轉年月已檢核完成就不能再改） |
| comp_io_mark | varchar(50) | — | — | — | 代轉章 |
| comp_acco_currym | varchar(6) | — | — | — | 總帳外幣匯差月（月結轉外幣會計科目餘額匯差） |
| comp_in_accdate | date | — | — | — | 收款入帳日期 |
| comp_ot_astfn | varchar(20) | — | — | — | 刷卡手續費支單負責人（日處理產生信用卡手續費支單時使用 有設定的公司才拋支單） |
| comp_fullname | varchar(200) | — | — | — | 公司全名 |
| comp_externalname | varchar(200) | — | — | — | 報表對外名稱 |
| compb_comp | varchar(10) | — | — | — | 公司代碼（FK → iscpm00） |
| compb_compbar | varchar(20) | — | — | — | 拉 Bar 類別 |
