# tppdm20 — 團體行程代號主檔。儲存可重複使用的標準行程範本，作為建立團號的基礎資料

**Aliases**: 團體行程代號主檔, tppdm20, PDM20, TPPDM20
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd20_tur2 | varchar(20) | NOT NULL | — | — | 行程代號（主鍵，僅允許英數字） |
| pd20_sts | char(1) | NULL | — | — | 已作廢（Y=已作廢 N=有效） |
| pd20_html | text | NULL | — | — | 自訂HTML（標準團名非一般者可自訂網頁內容） |
| pd20_type | char(1) | NULL | — | — | 行程類別（空白=團體 F=自由行 I=INB） |
| pd20_tur2_outb | varchar(20) | NULL | — | — | 對應OUTB行程代號（用於 INB/OUTB 行程對照） |
| pd20_line | varchar(10) | NOT NULL | — | tptbm | 線別（與標準團名須一致） |
| pd20_dline | varchar(10) | NULL | — | tptbm | 副線別（與標準團名須一致） |
| pd20_area | varchar(10) | NOT NULL | — | tptbm | 地區（與標準團名須一致） |
| pd20_darea | varchar(10) | NULL | — | tptbm | 細地區（與標準團名須一致） |
| pd20_prodname | varchar(50) | NULL | — | FK → 標準團名檔，有值時行程名稱=NULL | 標準團名（有值時行程名稱=NULL） |
| pd20_dname | varchar(200) | NULL | — | — | 內部顯示名稱（系統內部使用的行程名稱） |
| pd20_name | varchar(200) | NULL | — | — | 網頁名稱（B2C 網站顯示的行程名稱） |
| pd20_days | int | NOT NULL | — | — | 天數（行程總天數） |
| pd20_normal | char(1) | NOT NULL | — | — | 標準行程（Y=標準 N=非標準，產品部才可設定，INB 一律=標準） |
| pd20_country | varchar(10) | NULL | — | — | 雄獅國家代碼（主要用於自費活動帶價格） |
| pd20_prof | varchar(10) | NOT NULL | — | — | 建檔/負責單位（權限控管，業務建立非標準行程需 copy 成自己單位） |
| pd20_html_date | datetime | NULL | — | — | 網頁更新時間（NULL=尚未產生行程網頁） |
| pd20_mstfn | varchar(50) | NULL | — | — | 維護者單位姓名時區（格式：單位+姓名+空格+時區 (ex: 直團王大明 TW)） |
| pd20_mdate | datetime | NULL | — | — | 當地維護日期（維護者時區的日期時間） |
| pd20_msysdate | datetime | NULL | — | — | 主機時間（系統時間戳記） |
| pd20_tripidno | varchar(20) | NULL | — | PCM.dbo | 行程組合器序號 |
| pd20_salememo | text | NULL | — | — | 銷售說明（行程銷售重點、特色說明） |
| pd20_voltage | varchar(50) | NULL | — | — | 電壓（說明會資料顯示，格式: 110,210,120） |
| pd20_socket | varchar(50) | NULL | — | — | 插座（說明會資料顯示，格式: 1,3,5,6,7 (代碼)） |
| pd20_feature_src | char(1) | NULL | — | — | 特色來源（S=團體行程 C=站長平台） |
| pd20_bus | char(1) | NULL | — | — | 是否有綁定中控巴士路線（0=無 1=有） |
| pd20_tra | char(1) | NULL | — | — | 是否有綁定中控火車路線（0=無 1=有） |
| pd20_marketing_oimg | varchar(500) | NULL | — | — | 直客行銷圖片網址（桌面版行銷圖） |
| pd20_marketing_mimg | varchar(500) | NULL | — | — | 直客行銷圖片網址(M版)（手機版行銷圖） |
| pd20_marketing_url | varchar(500) | NULL | — | — | 直客行銷圖片跳轉連結（行銷圖點擊後的導向 URL） |
| pd20_marketing_content | text | NULL | — | — | 直客行銷文案（行銷活動說明文字） |
| pd20_passcountry | varchar(500) | NULL | — | — | 行程所經國家（多國行程的國家清單） |
| pd20_passcity | varchar(500) | NULL | — | — | 行程所經城市（行程途經的主要城市） |
