# tppdm13 — 團體說明資料檔

**Aliases**: 團體說明資料檔, tppdm13, PDM13, TPPDM13
**Database**: LionGroupERP
**Module**: TPPDM - 團體產品管理

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd13_prod | varchar | NOT NULL | PK | — | 團號（(推測)） |
| pd13_prodcomp | varchar | NOT NULL | PK | — | 團控公司（(推測)） |
| pd13_item | varchar | NOT NULL | PK | — | 項目（(推測)，例: "Room- 分房表final / Itin"） |
| pd13_desc | text | NULL | — | — | 說明（文件內容或說明文字） |
| pd13_mdate | datetime | NULL | — | — | 當地維護日期（當地時區的維護時間） |
| pd13_mstfn | varchar(50) | NULL | — | — | 維護者單位姓名時區（格式: "單位+姓名+空格+時區"，例: "直團王大明 TW"） |
| pd13_msysdate | datetime | NULL | — | — | 主機時間（系統記錄時間（主機時區）） |
