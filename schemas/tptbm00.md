# tptbm00 — 標準團名資料檔。旅遊館網頁上的搜尋引擎（改在各旅遊館設定）

**Aliases**: 標準團名資料檔, tptbm00, TPTBM00
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tbm0_code | varchar(36) | — | PK | — | 標準團名代碼（GUID） |
| tbm0_name | varchar | — | — | — | 標準團名 |
| tbm0_b2cname | varchar | — | — | — | B2C 標準團名 |
| tbm0_webname | varchar | — | — | — | 旅遊館網上名稱（短版） |
| tbm0_namemain | varchar | — | — | — | 標准團名：主團名 |
| tbm0_namelvl | varchar(1) | — | — | — | 標准團名：分級 |
| tbm0_namemkt | varchar | — | — | — | 標准團名：行銷說明 |
| tbm0_sts | int | — | — | — | 已停用 (1=停用, 0=啟用) |
| tbm0_inb | varchar | — | — | — | INB 行程 |
| tbm0_fit | varchar(1) | — | — | — | 團型為自由行 |
| tbm0_country | varchar | — | — | — | 出團雄獅國家 |
| tbm0_line | varchar | — | — | istbm10 | 線別 |
| tbm0_dline | varchar | — | — | — | 副線別 |
| tbm0_area | varchar | — | — | — | 地區 |
| tbm0_darea | varchar | — | — | — | 細地區 |
| tbm0_days | int | — | — | — | 天數 |
| tbm0_nameattr | varchar | — | — | — | 產品屬性（一般/皇家...） |
| tbm0_amtlvl | varchar(1) | — | — | — | 價格等級 |
| tbm0_webarea | varchar | — | — | tptbm20 | 目的地代碼（團搜尋 bar3） |
| tbm0_attr1 | varchar | — | — | FK → istbm00 (ATTR) | 團體屬性 1 |
| tbm0_attr2 | varchar | — | — | FK → istbm00 (ATTR) | 團體屬性 2 |
| tbm0_attr3 | varchar | — | — | FK → istbm00 (ATTR) | 團體屬性 3 |
| tbm0_psubject1 | varchar | — | — | FK → istbm00 (PSUBJECT) | 主題旅遊 1 |
| tbm0_psubject2 | varchar | — | — | FK → istbm00 (PSUBJECT) | 主題旅遊 2 |
| tbm0_psubject3 | varchar | — | — | FK → istbm00 (PSUBJECT) | 主題旅遊 3 |
| tbm0_keyword | varchar | — | — | — | 關鍵字（,峇里島,烏布,） |
| tbm0_usp | varchar | — | — | — | USP 網頁網址 |
| tbm0_picno | varchar | — | — | — | CMS 圖片 NO |
| tbm0_planticket | varchar | — | — | — | 產品種類：是否為計劃旅遊票 |
| tbm0_feature_src | varchar | — | — | — | 特色來源 |
| tbm0_triptype | varchar | — | — | — | 旅遊型態 |
| tbm0_prof | varchar | — | — | — | 單位 |
| tbm0_mstfn | varchar | — | — | — | 維護者姓名（單位+姓名） |
| tbm0_msysdate | datetime | — | — | — | 維護主機時間 |
| tbm0_mstfn2 | varchar | — | — | — | 主題旅遊維護者姓名 |
| tbm0_msysdate2 | datetime | — | — | — | 主題旅遊維護主機時間 |
