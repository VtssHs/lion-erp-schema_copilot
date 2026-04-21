# tppdm61 — 郵輪接駁車。記錄郵輪團的接駁車輛資訊，包含車輛基本資料、司機資訊、分車狀態與領隊指派

**Aliases**: 郵輪接駁車, tppdm61, PDM61, TPPDM61
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM) — 郵輪子系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd61_bus | varchar | — | — | — | 系統編號（格式：年度 2 碼 + 流水號 4 碼） |
| pd61_name | varchar | — | — | — | 標準團名 |
| pd61_d8 | datetime | — | — | — | 出團日期 |
| pd61_bus_name | varchar | — | — | — | 車號 |
| pd61_car_licence | varchar | — | — | — | 車牌號碼 |
| pd61_seat | int | — | — | — | 座位數 |
| pd61_type | varchar | — | — | — | 用車別（0=去，1=回，2=觀光(參加)，3=觀光(不參加)） |
| pd61_station | varchar | — | — | — | 上下車地 |
| pd61_time | varchar | — | — | — | 出發時間 |
| pd61_dr_cname | varchar | — | — | — | 司機姓名 |
| pd61_dr_mtel | varchar | — | — | — | 司機手機 |
| pd61_tl | varchar | — | — | — | 領隊員編 |
| pd61_tl_cname | varchar | — | — | — | 領隊姓名 |
| pd61_ok | varchar | — | — | — | 分車完成（0=未分車，1=開始分車，2=分車完成） |
| pd61_mstfn | varchar | — | — | — | 維護者姓名（格式：單位+姓名，例：`直團王大明`（無時區）） |
| pd61_msysdate | datetime | — | — | — | 維護時間 |
