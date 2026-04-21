# tptbm10 — 團體銷售資訊說明檔 (注意事項主檔)

**Aliases**: 團體銷售資訊說明檔, 注意事項主檔, 標準團名管理, tptbm10, TPTBM10
**Database**: LionGroupERP
**Module**: TPTBM (標準團名管理)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| note_area | varchar | — | PK | — | 地區。各說明分析資料，依地區別建立 |
| note_darea | varchar | — | PK | — | 細地區 |
| note_note | varchar | — | PK | FK → Istbm00 (NOTE) | 說明項目。注意事項類別代碼 |
| note_carr | varchar | — | PK | — | 航空公司/序號。脫隊資訊=各航空公司；非脫隊時，主要用在食衣住行資訊上，為序號欄位(01,02..) |
| note_country | varchar | — | PK | — | 出團雄獅國家。非脫隊時，主要用在食衣住行資訊上，為序號欄位(01,02..) |
| note_dname | nvarchar | — | — | — | 內容名稱。注意事項的標題或摘要 |
| note_desc | nvarchar(max) | — | — | — | 內容。注意事項的詳細內容 |
| note_usts | char(1) | — | — | — | 要上架行程網頁。1=要秀在行程網頁上 |
| note_mstfn | varchar | — | — | — | 維護者及時區。單位+姓名+空格+時區，例：直團王大明 TW |
| note_msysdate | datetime | — | — | — | 維護主機時間。系統記錄時間 |
| note_mdate | datetime | — | — | — | 當地維護時間。維護者當地時間 |
