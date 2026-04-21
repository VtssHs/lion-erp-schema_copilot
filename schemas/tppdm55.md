# tppdm55 — 交付 B2P 供應商處理團。團體交由 B2P 供應商處理的訂團記錄與確認狀態

**Aliases**: 交付 B2P 供應商處理團, tppdm55, PDM55, TPPDM55
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd55_prod | varchar(10) | — | PK | tppdm10.prod_prod | 團號 |
| pd55_prodcomp | varchar(2) | — | — | — | 團控公司 |
| pd55_local | nvarchar(12) | — | — | B2P供應商主檔 | 供應商代碼（型態配合B2P系統） |
| pd55_bkk | datetime | — | — | — | 訂團日期（首次訂團時間） |
| pd55_bkstfn | varchar(20) | — | — | 只存第一次設定者，FK → 員工主檔 | 訂團者員編（只存第一次設定者） |
| pd55_lcount | int | — | — | — | 訂團次數（追蹤修改訂單的次數） |
| pd55_bkdesc | nvarchar(500) | — | — | — | (給供應商的)說明（供應商已確認後取消訂團時必須寫說明） |
| pd55_bkconman | nvarchar(50) | — | — | — | 訂購聯絡人 |
| pd55_bkcontel | varchar(20) | — | — | — | 訂購聯絡電話 |
| pd55_ldate | datetime | — | — | — | 供應商確認時間（供應商登入系統確認訂單的時間） |
| pd55_lid | varchar(20) | — | — | — | 供應商確認帳號（供應商登入帳號，用於留言功能） |
| pd55_lname | nvarchar(20) | — | — | — | 供應商確認人（供應商確認人員姓名） |
| pd55_ltel | varchar(20) | — | — | — | 領隊電話（提供給供應商的領隊聯絡電話） |
| pd55_lteltotal | int | — | — | — | 使用量（領隊電話號碼的使用次數統計） |
| pd55_mstfn | varchar(20) | — | — | — | 維護者姓名（例如: "王大明"） |
| pd55_mdate | datetime | — | — | — | 維護時間（最後修改時間） |
