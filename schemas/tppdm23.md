# tppdm23 — 行程自費活動關聯檔。關聯行程與自費活動節目（Optional Tour）

**Aliases**: 行程自費活動關聯檔, tppdm23, PDM23, TPPDM23
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd23_tur2 | varchar(20) | — | PK | tppdm20.pd20_tur2 | 行程代號（**PK1**, , 複製不copy本檔） |
| pd23_seq | int | — | — | — | 序號（**PK2**, 不可重覆） |
| pd23_option | varchar(20) | — | — | optnm00 | 活動節目（（活動節目主檔）） |
| pd23_mstfn | varchar(50) | — | — | — | 維護者姓名及時區（單位+姓名+空格+時區 ex:直團王大明 TW） |
| pd23_mdate | datetime | — | — | — | 當地維護時間（維護者當地時間） |
| pd23_msysdate | datetime | — | — | — | 主機時間（系統伺服器時間） |
