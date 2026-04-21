# bookm01 — 預訂明細。預訂的明細項目（房型、餐別、活動項目等細項）

**Aliases**: 預訂明細, 預訂系統, bookm01, OKM01, BOOKM01
**Database**: LionGroupERP
**Module**: 預訂系統 (Booking)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| bk01_bookno | varchar | — | — | bookm00.bk00_bookno | 預定序號（**PK1**） |
| bk01_seq | int | — | — | — | 序號（**PK2**, 明細流水號） |
| bk01_cto | varchar(2) | — | — | — | 類別（H=房, M1=早餐, M3=午餐, M5=晚餐, V=活動, B=車, T=其他） |
| bk01_item | nvarchar | — | — | — | 預訂明細 |
| bk01_description | nvarchar | — | — | — | 預訂項目（記錄旅館內booking餐的資料） |
| bk01_fdate | date | — | — | — | 日期 |
| bk01_days | decimal | — | — | — | 使用天/時 |
| bk01_qty | int | — | — | — | 數量 |
| bk01_act | varchar | — | — | — | 計算單位（例如: 間、人、車、天） |
| bk01_amt | decimal | — | — | — | 單價 |
| bk01_meatstyle | varchar | — | — | optbm30 | 餐標（記錄旅館內booking餐的資料） |
| bk01_foc | int | — | — | — | FOC（Free of Charge 免費數量） |
| bk01_freepst | bit | — | — | — | 免PST稅（打勾金額累計到免PST稅金額；沒打勾則累計到未稅金額） |
