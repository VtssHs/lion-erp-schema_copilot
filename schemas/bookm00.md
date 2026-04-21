# bookm00 — 預訂主檔。OP 對供應商的預訂記錄（旅館、餐廳、車輛、景點、商店等）

**Aliases**: 預訂主檔, 預訂系統, bookm00, OKM00, BOOKM00
**Database**: LionGroupERP
**Module**: 預訂系統 (Booking)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| bk00_bookno | varchar | — | PK | — | 預訂序號（isnom00(book, 系統年度)，編碼方式: 2碼系統年+6碼流水序號） |
| bk00_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| bk00_prodcomp | varchar | — | — | — | 控團公司 |
| bk00_prof | varchar | — | — | — | 單位 |
| bk00_cto | char(1) | — | — | — | 類別（h=旅館, m=餐, b=車, v=景點活動, s=商店） |
| bk00_cto2 | char(1) | — | — | — | 類別2（餐廳時用: 1=早, 3=午餐, 5=晚餐） |
| bk00_ctokey | varchar | — | — | FK → 各類別主檔 (ophtm/opmtm/opbsm/opvim/opspm) | 元件代碼 |
| bk00_local | varchar | — | — | opagm10 | 供應商 |
| bk00_invoice | varchar | — | — | — | (供應商請款的)invoice編號 |
| bk00_fdate | date | — | — | — | 使用起日（只有旅館及車會有起訖日期） |
| bk00_tdate | date | — | — | — | 使用訖日 |
| bk00_days | int | — | — | — | 使用日數（旅館=訖-起日(隔天退房)，車=訖-起日+1天(頭尾都要用車)） |
| bk00_curr | varchar | — | — | — | 幣別 |
| bk00_amt | decimal | — | — | — | 預訂未稅總金額 |
| bk00_gst | decimal | — | — | — | GST稅金 |
| bk00_gst_rate | decimal | — | — | — | GST稅率 |
| bk00_pst | decimal | — | — | — | PST稅金 |
| bk00_pst_rate | decimal | — | — | — | PST稅率 |
| bk00_amt2 | decimal | — | — | — | 免PST稅金額（統一都要GST稅） |
| bk00_tax | bit | — | — | — | 金額已內含稅（雪梨成本均內含GST，為總計需反推未稅及各項金額） |
| bk00_tot_amt | decimal | — | — | — | 含稅總金額 |
| bk00_amt3 | decimal | — | — | — | 訂金 |
| bk00_amt3_ot | bit | — | — | — | 已產生訂金支單（0=未產生, 1=已產生） |
| bk00_paymode | char(1) | — | — | — | 付款方式（$=現金, #=支票, b=銀存轉帳, c=信用卡, v=voucher） |
| bk00_chkno | varchar | — | — | — | 支票號碼（主要由支單付款時回寫，用於budget表） |
| bk00_payfor | varchar | — | — | iscpm11 | 信用卡付款人（信用卡時用） |
| bk00_compcard | varchar | — | — | — | 公司信用卡代號 |
| bk00_bkdate | datetime | — | — | — | 預定時間 |
| bk00_cfdate | datetime | — | — | — | 確認時間 |
| bk00_cfno | varchar | — | — | — | 確認代號 |
| bk00_flow | char(1) | — | — | — | 處理狀況（空白=輸入, b=bk:已預定, c=cf:已確認, f=支:已產生支單） |
| bk00_sts | bit | — | — | — | 已作廢 |
| bk00_sts1 | bit | — | — | — | 預定後異動 |
| bk00_description | nvarchar | — | — | — | 預訂項目 |
| bk00_desc | nvarchar | — | — | — | 預定備註 |
| bk00_desc2 | nvarchar | — | — | — | 旅客姓名 |
| bk00_bus_carr | varchar | — | — | optbm70 | 車型代碼 |
| bk00_driver | varchar | — | — | — | 司機名 |
| bk00_driver_tel | varchar | — | — | — | 司機電話 |
| bk00_meatstyle | varchar | — | — | optbm30 | 餐標代碼 |
| bk00_amt_b | bit | — | — | — | booking form 印成本（0=不列印, 1=要列印） |
| bk00_amt_v | bit | — | — | — | voucher 印成本（0=不列印, 1=要列印） |
| bk00_year | int | — | — | — | FIT訂單年 |
| bk00_ordr | varchar | — | — | — | FIT訂單編號 |
| bk00_mstfn | varchar | — | — | — | 維護者姓名（單位+姓名+空格+時區 ex:資訊王大明 TW） |
| bk00_mdate | datetime | — | — | — | 當地維護時間 |
| bk00_20mstfn | varchar | — | — | — | 行程日期資料維護者姓名（單位+姓名+空格+時區 ex:資訊王大明 TW） |
| bk00_20mdate | datetime | — | — | — | 行程日期資料當地維護時間 |
