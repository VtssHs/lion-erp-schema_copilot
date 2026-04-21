# istbm10 — 線別代碼檔

**Aliases**: 線別代碼檔, istbm10, ISTBM10
**Database**: LionGroupERP
**Module**: 

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| line_line | varchar | — | PK | — | 線別代號 |
| line_dline | varchar | — | — | — | 副線別 |
| line_dname | varchar | — | — | — | 名稱 |
| line_base | int | — | — | — | 出團成團人數 |
| line_opamt | decimal | — | — | — | 出團公司操作費 |
| line_order | int | — | — | — | 順序 |
| line_sts | int | — | — | — | 已停用 (1=停用, 0=啟用) |
