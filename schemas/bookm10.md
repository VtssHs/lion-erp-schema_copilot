# bookm10 — 團體訂單主檔（CTO元件預訂）

**Aliases**: 團體訂單主檔, CTO元件預訂, 預訂管理, 團體預訂主檔, 團體預訂明細, bookm10, OKM10, BOOKM10
**Database**: LionGroupRPM
**Module**: BOOKM（預訂管理）

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| __bk10_prod__ | varchar | — | PK | — | 團號（關聯 tppdm10（團體主檔）） |
| __bk10_fdate__ | date | — | — | — | 行程日期（該元件服務的日期） |
| __bk10_seq__ | int | — | — | — | 序號（同一天內的元件排序） |
| __bk10_cto__ | varchar(1) | — | — | — | 類別（`H`=旅館, `M`=餐, `B`=車, `V`=景點, `S`=商店） |
| __bk10_cto2__ | varchar(1) | — | — | — | 類別2（餐廳專用）（`1`=早餐, `3`=午餐, `5`=晚餐 （僅餐廳類別使用）） |
| __bk10_ctokey__ | varchar | — | — | — | 元件代碼（關聯供應商主檔（opagm/ophtm/opmtm等）） |
| __bk10_desc__ | text | — | — | — | 行程說明（該元件的詳細說明） |
| __bk10_ftime__ | time | — | — | — | 時間（服務發生時間（如用餐時間、接車時間）） |
| __bk10_prodcomp__ | varchar | — | — | — | 控團公司（負責該團的公司別） |
| __bk10_prof__ | varchar | — | — | — | 控團單位（For itin 判斷用（行程表生成時的單位判斷）） |
| __bk10_mdate__ | datetime | — | — | — | 當地維護時間（最後異動時間） |
| __bk10_mstfn__ | varchar | — | — | — | 維護者姓名及時區（格式：`單位+姓名+空格+時區` 例：`資訊王大明 TW`） |
