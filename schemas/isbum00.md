# isbum00 — Bu 事業體主檔。定義雄獅集團各 BU（Business Unit）事業體的基本資料，是整個系統 BU 分類的根基，被訂單、產品、分銷等多個模組參照

**Aliases**: Bu 事業體主檔, 財務結算, isbum00, BUM00, ISBUM00
**Database**: LionGroupERP
**Module**: 財務結算 (ISBUM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| bu00_bu | varchar | — | PK | — | 雄獅 BU 代碼 |
| bu00_cname | varchar | — | — | — | 中文名稱 |
| bu00_ename | varchar | — | — | — | 英文名稱 |
| bu00_dname | varchar | — | — | — | 顯示名稱 |
| bu00_desc | varchar | — | — | — | 備註 |
| bu00_industry | varchar | — | — | — | 行業別代碼 |
| bu00_logo | varchar | — | — | — | logo 圖檔檔名（固定放 `iis-erp\images`，命名規則：`logo_bu_代碼.jpg`） |
| bu00_order | int | — | — | — | 顯示順序 |
| bu00_sts | bit/int | — | — | — | 已作廢（1=作廢, 0=啟用） |
| bu00_mstfn | varchar | — | — | — | 增修人員 |
| bu00_mdate | datetime | — | — | — | 增修系統時間 |
