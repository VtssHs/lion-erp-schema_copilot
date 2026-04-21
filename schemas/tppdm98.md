# tppdm98 — 團多房價群組檔。管理同一團號下的多種房型價格方案，支援不同旅館組合與銷售方案

**Aliases**: 團多房價群組檔, tppdm98, PDM98, TPPDM98
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd98_prod | varchar(10) | — | PK | tppdm10.prod_prod | 團號（**PK1**） |
| pd98_prodcomp | varchar(2) | — | — | — | 團控公司 |
| pd98_no | int | — | — | — | 序號（**PK2**, 同一團號下的房價方案編號） |
| pd98_hotel | varchar(10) | — | — | FK → 旅館主檔，該方案主要使用的旅館 | 旅館代碼（該方案主要使用的旅館） |
| pd98_salename | nvarchar(100) | — | — | — | 銷售方案名稱（前台顯示名稱，例如：「五星尊榮」「經典商務」） |
| pd98_sort | int | — | — | — | 排序（前台顯示順序，數字越小越前面） |
| pd98_sts | bit | — | — | — | 是否滿位（1=已滿位, 0=尚有空位） |
| pd98_mstfn | varchar(20) | — | — | FK → 員工主檔 | 維護人員編 |
| pd98_mdate | datetime | — | — | — | 維護時間（最後修改時間） |
