# tppdm24 — 團體日行程CTO資料檔。日行程的 CTO（Customer To Operator）景點、餐廳、旅館、商店資料

**Aliases**: 團體日行程CTO資料檔, tppdm24, PDM24, TPPDM24
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd24_tur2 | varchar | — | PK | tppdm20.pd20_tur2 | 行程代號 |
| pd24_num | int | — | — | — | 流水號（對應 tppdm21.pd21_num（第幾天）） |
| pd24_cto | varchar(10) | — | — | — | CTO類別（VIEW/MEAT/HOTEL/SHOP） |
| pd24_seq | int | — | — | — | 序號（同類別內的順序（1, 2, 3...）） |
| pd24_ctokey | varchar | — | — | FK → 對應的主檔（景點/餐廳/旅館/商店） | CTO資料代碼（（景點/餐廳/旅館/商店）） |
| pd24_name | nvarchar | — | — | — | 顯示名稱（覆寫原始名稱時使用） |
| pd24_web | varchar | — | — | — | 外部網站聯結網址（景點官網、餐廳訂位網站等） |
| pd24_rowversion | timestamp | — | — | — | 時間戳記（新增時會自行產生，用於併發控制） |
