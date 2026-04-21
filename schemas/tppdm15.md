# tppdm15 — 團體活動節目關聯檔。記錄每個出發團所關聯的自費活動節目，一個團可對應多個活動節目，透過序號區分

**Aliases**: 團體活動節目關聯檔, tppdm15, PDM15, TPPDM15
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd15_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| pd15_prodcomp | varchar | — | PK | — | 團控公司 |
| pd15_seq | int | — | — | — | 序號（不可重複） |
| pd15_option | varchar | — | — | optnm00 | 活動節目（（活動節目主檔）） |
| pd15_mstfn | varchar | — | — | — | 增修者單位姓名時區（格式：單位+姓名+空格+時區，例：`直團王大明 TW`） |
| pd15_mdate | datetime | — | — | — | 當地增修日期 |
| pd15_msysdate | datetime | — | — | — | 主機增修時間（不顯示，備查用） |
