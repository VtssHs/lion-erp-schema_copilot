# tppdm81 — 設定滑雪團各級教練人數。設定滑雪團各類別（類別）各等級（等級）所需的教練人數上限

**Aliases**: 設定滑雪團各級教練人數, tppdm81, PDM81, TPPDM81
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd81_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| pd81_prodcomp | varchar | — | PK | — | 團號公司 |
| pd81_kind | varchar | — | — | — | 類別（教練類別） |
| pd81_level | varchar | — | — | — | 等級（滑雪等級） |
| pd81_max | int | — | — | — | 人數（該類別+等級的教練人數上限） |
| pd81_mstfn | varchar | — | — | — | 維護者姓名（格式：單位+姓名，只存第一筆） |
| pd81_mdate | datetime | — | — | — | 維護時間 |
