# tppdm64 — 郵輪岸上觀光車次。記錄郵輪岸上觀光的每個車次（班次）資料，包含日期、座位、領隊、司機、用餐等出團執行資訊

**Aliases**: 郵輪岸上觀光車次, tppdm64, PDM64, TPPDM64
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM) — 郵輪子系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd64_localtour | varchar | — | — | tppdm62.pd62_localtour | 編號 |
| pd64_date | datetime | — | PK | — | 日期 |
| pd64_bus | varchar | — | PK | — | 車次 |
| pd64_sts | bit/int | — | — | — | 已停售 |
| pd64_seat | int | — | — | — | 座位數 |
| pd64_ac | int | — | — | — | 加購人數（國內郵輪＝大人+小孩+INF；國外郵輪＝大人+小孩） |
| pd64_infseat | bit/int | — | — | — | 嬰兒佔位（預設值=0（不佔位）） |
| pd64_place | varchar | — | — | — | 集合地點 |
| pd64_time | varchar | — | — | — | 集合時間 |
| pd64_meal | varchar | — | — | — | 用餐餐廳 |
| pd64_meal_time | varchar | — | — | — | 用餐時間 |
| pd64_tl | varchar | — | — | — | 領隊 |
| pd64_dr_cname | varchar | — | — | — | 司機 |
| pd64_dr_mtel | varchar | — | — | — | 司機手機 |
| pd64_car_licence | varchar | — | — | — | 車牌號碼 |
| pd64_busCode | varchar | — | — | — | 標籤 |
| pd64_mstfn | varchar | — | — | — | 維護者姓名及時區（格式：單位+姓名+空格+時區，例：`資訊王大明 TW`；此資料未存當地時間，目前只用於台灣故無異常） |
| pd64_msysdate | datetime | — | — | — | 維護主機時間 |
