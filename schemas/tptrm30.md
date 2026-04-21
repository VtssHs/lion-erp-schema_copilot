# tptrm30 — 旅遊館群組。FOR 產生自由行館搜尋引擎

**Aliases**: 旅遊館群組, tptrm30, TRM30, TPTRM30
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tr30_travel | varchar | — | PK | tptrm20 | 旅遊館代號（(part 1)） |
| tr30_group | varchar | — | PK | — | 旅遊館群組代號（(part 2)） |
| tr30_name | varchar | — | — | — | 群組名稱 |
| tr30_desc | text | — | — | — | 特色描述 |
| tr30_freegroup | varchar | — | — | — | 系列代碼 |
| tr30_name2 | varchar | — | — | — | 系列名稱/國家城市名 |
| tr30_desc2 | text | — | — | — | 產品目的地（格式化） |
| tr30_tcountry | varchar | — | — | — | 目的地國家 |
| tr30_tcity | varchar | — | — | — | 目的地城市 |
| tr30_fdate | date | — | — | — | 產品效期起日 |
| tr30_tdate | date | — | — | — | 產品效期迄日 |
| tr30_left_pic | varchar | — | — | — | 左圖檔名 |
| tr30_more | int | — | — | — | 加顯示 More 聯結 |
| tr30_prof | varchar | — | — | — | 負責單位 |
| tr30_sts | int | — | — | — | 已停用 (1=停用, 0=啟用) |
| tr30_mstfn | varchar | — | — | — | 維護者及時區（單位+姓名+空格+時區） |
| tr30_msysdate | datetime | — | — | — | 維護主機時間 |
| tr30_mdate | datetime | — | — | — | 當地維護時間（負責單位時區時間） |
| tr30_mstfn2 | varchar | — | — | — | 產品維護者及時區 |
| tr30_mdate2 | datetime | — | — | — | 產品維護當地時間 |
| tr30_pstfn | varchar | — | — | — | 結轉者及時區（單位+姓名+空格+時區） |
| tr30_pdate | datetime | — | — | — | 結轉當地時間 |
