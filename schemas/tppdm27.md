# tppdm27 — 團體行程修改自動留言檔。記錄行程修改時的自動通知留言（異動追蹤與通知機制）

**Aliases**: 團體行程修改自動留言檔, tppdm27, PDM27, TPPDM27
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd27_tur2 | varchar(20) | — | — | tppdm20.pd20_tur2 | 行程代號 |
| pd27_tur22 | varchar(20) | — | — | — | 行程代號（用途待確認（可能為修改前/後行程代號）） |
| pd27_desc | nvarchar(max) | — | — | — | 通知備註說明（自動產生的異動說明） |
| pd27_stfn | varchar(20) | — | — | — | 通知者員編（觸發異動的員工編號） |
| pd27_mstfn | varchar(50) | — | — | — | 維護者姓名及時區（單位+姓名+空格+時區 ex:直團王大明 TW） |
| pd27_mdate | datetime | — | — | — | 當地維護時間（維護者當地時間） |
| pd27_msysdate | datetime | — | — | — | 主機時間（系統伺服器時間，異動發生時間） |
