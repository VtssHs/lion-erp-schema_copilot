# tptrm20 — 旅遊館。- 多國營運時區分不同市場的旅遊館

**Aliases**: 旅遊館, tptrm20, TRM20, TPTRM20
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tr20_travel | varchar | — | PK | — | 旅遊館代號 |
| tr20_name | varchar | — | — | — | 旅遊館名稱 |
| tr20_country | varchar | — | — | — | 雄獅國家 |
| tr20_prod | varchar(1) | — | — | — | 產品別 |
| tr20_freekind | varchar | — | — | FK → istbm00 (FREEKIND) | 自由行類別 |
| tr20_carr | varchar | — | — | — | 自由行航空公司（多個以分號分隔） |
| tr20_order | int | — | — | — | 順序 |
| tr20_hide | int | — | — | — | 搜尋引擎不顯示 |
| tr20_html | datetime | — | — | — | 產生網頁時間 |
| tr20_sts | int | — | — | — | 已停用 (1=停用, 0=啟用) |
| tr20_mstfn | varchar | — | — | — | 維護者及時區（單位+姓名+空格+時區） |
| tr20_msysdate | datetime | — | — | — | 維護主機時間 |
| tr20_mdate | datetime | — | — | — | 當地維護時間 |
