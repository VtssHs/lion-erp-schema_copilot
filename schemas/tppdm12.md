# tppdm12 — 說明會副檔。記錄每個出發團的說明會作業資料、領隊建議與核派流程、交班設定、報帳狀態，以及 AI 導領腳本/影片等補充設定

**Aliases**: 說明會副檔, tppdm12, PDM12, TPPDM12
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd12_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| pd12_prodcomp | varchar | — | — | — | 團控公司 |
| pd12_rc | varchar | — | — | — | 指派者姓名（例：王大明） |
| pd12_rcdate | datetime | — | — | — | 指派日期 |
| pd12_op | varchar | — | — | — | 接團 OP 員編 |
| pd12_opdate | datetime | — | — | — | OP 接團確認日期 |
| pd12_meet | varchar | — | — | — | 要辦理說明會（0=不辦理，1=要辦理） |
| pd12_meetname | varchar | — | — | — | 說明會文件用行程內部名稱（0=tptbm00_b2cname，1=tppdm20.pd20_dname 用行程內部名） |
| pd12_meetdate | datetime | — | — | — | 說明會時間 |
| pd12_meetplace | varchar | — | — | FK → Istbm00 (MEET) | 說明會地點 |
| pd12_meetshowblock | varchar | — | — | — | 顯示區塊（多值設定，見代碼說明） |
| pd12_meetdesc | varchar | — | — | — | 備註 & 視訊連結 |
| pd12_rop | varchar | — | — | — | 說明會文件送審者姓名（例：王大明） |
| pd12_rdate | datetime | — | — | — | 說明會文件送審日 |
| pd12_frc | varchar | — | — | — | 說明會審查者姓名（例：王大明） |
| pd12_fdate | datetime | — | — | — | 說明會審查日期 |
| pd12_fop | varchar | — | — | — | 說明會資料產生 HTML |
| pd12_fcnt | int | — | — | — | 說明會資料重送審次數 |
| pd12_pdf | varchar | — | — | — | 說資產生 pdf 檔 |
| pd12_sugg | varchar | — | — | — | 建議領隊者員編 |
| pd12_suggstfn | varchar | — | — | — | 建議領隊者姓名（例：王大明） |
| pd12_suggdate | datetime | — | — | — | 建議日期 |
| pd12_suggtl | varchar | — | — | — | 建議領隊編號 |
| pd12_suggtlsta | varchar | — | — | — | 建議領隊身份（空白=專業，1=員工，2=同行借調） |
| pd12_suggtlname | varchar | — | — | — | 建議領隊姓名 |
| pd12_suggdesc | varchar | — | — | — | 建議備註說明 |
| pd12_tl_sex | varchar | — | — | — | 建議領隊性別（空白=不限，M=男，F=女） |
| pd12_tl_tg | varchar | — | — | — | T/G（Through Guide） |
| pd12_tl_sg | varchar | — | — | — | S/G（Shopping Guide） |
| pd12_app | varchar | — | — | — | 核派領隊者員編 |
| pd12_appstfn | varchar | — | — | — | 核派領隊者姓名（例：王大明） |
| pd12_appdate | datetime | — | — | — | 核派日期 |
| pd12_apptl | varchar | — | — | — | 核派領隊編號 |
| pd12_apptlsta | varchar | — | — | — | 核派領隊身份（空白=專業，1=員工，2=同行借調） |
| pd12_apptlname | varchar | — | — | — | 核派領隊姓名 |
| pd12_appdesc | varchar | — | — | — | 核派備註說明 |
| pd12_year | varchar | — | — | — | 核派領隊訂單年 |
| pd12_order | varchar | — | — | — | 核派領隊訂單編號 |
| pd12_agent_year | varchar | — | — | — | 同行派領隊的訂單年（因同行訂單人數較多故派其領隊，尚未有查詢功能） |
| pd12_agent_order | varchar | — | — | — | 同行派領隊的訂單編號 |
| pd12_agent_tlname | varchar | — | — | — | 同行派領隊姓名 |
| pd12_shift | varchar | — | — | — | 交班 |
| pd12_shift_stfn | varchar | — | — | — | (交班) 代理者員編 |
| pd12_color | varchar | — | — | — | 識別證顏色 |
| pd12_godate1 | datetime | — | — | — | 日期時間（出團單位的集合資料） |
| pd12_airport1 | varchar | — | — | — | 機場代號 |
| pd12_gocarr1 | varchar | — | — | — | 航空公司櫃台 |
| pd12_tel1 | varchar | — | — | — | 聯絡電話 |
| pd12_godesc | varchar | — | — | — | 備註說明 |
| pd12_telmemo | varchar | — | — | — | 舊版領電話說明 |
| pd12_reim | varchar | — | — | — | 需領隊報帳（依線別+單位預設，亦可由會計設定） |
| pd12_reim_fdate | datetime | — | — | — | 結帳完成日 |
| pd12_reim_ac | varchar | — | — | — | 結帳維護者單位姓名時區（格式：單位+姓名+空格+時區） |
| pd12_reim_mdate | datetime | — | — | — | 結帳維護時間 |
| pd12_reim52 | varchar | — | — | — | 52 支單需領隊報帳（52 支單由日處理判斷是否領隊結帳） |
| pd12_reim52_fdate | datetime | — | — | — | 52 支單結帳完成日 |
| pd12_assistant_script | varchar | — | — | — | 導領腳本代碼 |
| pd12_assistant_video | varchar | — | — | — | 說資影片檔名 |
| pd12_assistant_url | varchar | — | — | — | 說資 Q&A 網址 |
| pd12_assistant_stfn | varchar | — | — | — | 發送通知人 |
| pd12_assistant_date | datetime | — | — | — | 發送通知時間 |
| pd12_assistant_pstfn | varchar | — | — | — | 送出影片人 |
| pd12_assistant_pdate | datetime | — | — | — | 送出影片時間 |
| pd12_assistant_psts | varchar | — | — | — | 送出影片狀態 |
| pd12_mstfn | varchar | — | — | — | 說明會資料維護者單位姓名時區（格式：單位+姓名+空格+時區，例：`直團王大明 TW`） |
| pd12_mdate | datetime | — | — | — | 當地維護日期 |
| pd12_msysdate | datetime | — | — | — | 主機時間 |
| pd12_tlmstfn | varchar | — | — | — | 設定領隊資料維護者單位姓名時區（格式同上） |
| pd12_tlmdate | datetime | — | — | — | 設定領隊維護日期 |
