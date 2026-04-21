# tppdm21_ez — 易遊團體日行程檔。易遊（EZ）系統的日行程明細，對應 tppdm21 的易遊版本，記錄易遊行程的每日內容

**Aliases**: 易遊團體日行程檔, 易遊子系統, 易遊系統的日行程明細, tppdm21_ez, PDM21_EZ, TPPDM21_EZ
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM) — 易遊子系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| ez21_tur2 | varchar | — | PK | tppdm20_ez.ez20_tur2 | 行程代號 |
| ez21_num | int | — | — | — | 流水號（行程內日次序號） |
| ez21_day | int | — | — | — | 天數（第幾天） |
| ez21_name | nvarchar | — | — | — | 行程點簡介（該日行程重點名稱） |
| ez21_desc | nvarchar | — | — | — | 行程說明（該日完整行程描述） |
| ez21_msysdate | datetime | — | — | — | 異動時間 |
