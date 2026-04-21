# ispfm00 — 單位主檔。控制該單位在系統中可見的功能模組

**Aliases**: 單位主檔, ispfm00, PFM00, ISPFM00
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| prof_prof | varchar | — | PK | — | 單位代號 |
| prof_cname | varchar | — | — | — | 名稱 |
| prof_dname | varchar | — | — | — | 簡稱 |
| prof_bu | varchar | — | — | isbum00 | 雄獅 BU 代碼 |
| prof_comp | varchar | — | — | — | 帳務公司代碼 |
| prof_comp2 | varchar | — | — | — | 對外公司代碼 |
| prof_sts | int | — | — | — | 已作廢 (1=作廢, 0=啟用) |
| prof_sts1 | varchar(1) | — | — | — | 產銷別 |
| prof_sts2 | varchar(1) | — | — | — | 團票別 |
| prof_order | int | — | — | — | 顯示順序 |
| prof_webname | varchar | — | — | — | 雄獅網上顯示名稱 |
| prof_weborder | int | — | — | — | 網上顯示順序 |
| prof_webcode | varchar | — | — | — | 訂房單位網站號 |
| prof_kind | varchar | — | — | — | 權限拉 Bar |
| prof_b2c | int | — | — | — | 網站 B2C 接單 |
| prof_b2c_day0 | int | — | — | — | 業務接網單數每日歸 0 |
| prof_b2b | int | — | — | — | 網站 B2B 團接單 |
| prof_b2b_stfn | varchar | — | — | — | 窗口人員（B2B 團） |
| prof_b2btk | int | — | — | — | 網站 B2B 票接單 |
| prof_b2btk_stfn | varchar | — | — | — | 窗口人員（B2B 票） |
| prof_b2btk_tel | varchar | — | — | — | TC 票購證電話 |
| prof_b2btk_fax | varchar | — | — | — | TC 票購證傳真 |
| prof_b2e | int | — | — | — | 網站 B2E 接單 |
| prof_b2e_stfn | varchar | — | — | — | 團窗口人員（B2E） |
| prof_b2etk_stfn | varchar | — | — | — | 票窗口人員（B2E） |
| prof_tkissue | varchar | — | — | — | 自動開票 TC 單位 |
| prof_qbox | varchar | — | — | — | 網路訂位 ABACUS Q 信箱代號 |
| prof_tl | varchar | — | — | — | 最後留言/企業加盟/需求單核派者 |
| prof_email | varchar | — | — | — | 代表 E-MAIL |
| prof_rec99_4 | varchar | — | — | — | 派車單逾期還車排候補截止日 |
| prof_mstfn | varchar | — | — | — | 維護者姓名（單位+姓名） |
| prof_mdate | datetime | — | — | — | 維護時間 |
| prof_idate | datetime | — | — | — | 新增時間 |
