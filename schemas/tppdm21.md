# tppdm21 — 日行程檔。行程範本的每日細節（Day by Day）

**Aliases**: 日行程檔, tppdm21, PDM21, TPPDM21
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd21_tur2 | varchar | — | PK | tppdm20.pd20_tur2 | 行程代號 |
| pd21_num | int | — | — | — | 流水號（每個行程內的日次序號） |
| pd21_day | int | — | — | — | 天數（第幾天（通常 = pd21_num）） |
| pd21_data | nvarchar | — | — | — | 類別（早餐/午餐/晚餐/住宿/景點等分類） |
| pd21_name | nvarchar | — | — | — | 行程點簡介（該日行程重點名稱） |
| pd21_title | nvarchar | — | — | — | 特別說明（該日行程特別注意事項） |
| pd21_desc | nvarchar(max) | — | — | — | 行程說明（該日完整行程描述） |
| pd21_hotel_desc1 | nvarchar | — | — | — | 旅館地點（住宿地點名稱） |
| pd21_hotel_desc2 | nvarchar | — | — | — | 旅館或同級說明（住宿飯店或同級備註） |
| pd21_file | varchar | — | — | — | 照片檔名（該日行程的代表圖片檔名） |
| pd21_ctokey | varchar | — | — | FK → Ctom85 (VIEW) | 右側景點CTO資料代碼 |
| pd21_rowversion | timestamp | — | — | — | 時間戳記（新增時會自行產生，用於併發控制） |
