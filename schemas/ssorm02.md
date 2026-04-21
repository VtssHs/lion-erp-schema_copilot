# ssorm02 — 訂單副檔。訂單關聯產品、訂位系統（CRS）、PNR 與通知事項管理

**Aliases**: 訂單副檔, ssorm02, ORM02, SSORM02
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or02_ordr | varchar | — | PK | ssorm00.ordr_ordr | 訂單編號 |
| or02_year | varchar | — | — | ssorm00.ordr_year | 訂單年度（ssorm00 left join 線8訂單有額外處理時才有） |
| or02_crs | varchar | — | — | FK → Istbm00 (CRSKIND) | 訂位系統 |
| or02_pnr | varchar | — | — | — | PNR（Passenger Name Record） |
| or02_kind | varchar | — | — | — | 關聯類別（TK=Tc開票, FM=因跨國/Bu的主產品訂單） |
| or02_wtordr | varchar | — | — | — | 關聯TC訂單流水號 / 源頭訂單（FM時為主產品訂單） |
| or02_wtyear | varchar | — | — | — | 關聯TC訂單訂單年 / 源頭訂單（FM時為主產品訂單） |
| or02_key1 | varchar | — | — | — | 對應產品編號KEY1（票價代號, 系列, 票券編號, 團號公司） |
| or02_key2 | varchar | — | — | — | 對應產品編號KEY2（票產代碼, 產品） |
| or02_key3 | varchar | — | — | — | 對應產品編號KEY3（行程代號, 團號） |
| or02_prof | varchar | — | — | — | 處理單位 |
| or02_pstfn | varchar | — | — | — | 處理人員 |
| or02_stfn | varchar | — | — | — | 通知處理人員 |
| or02_desc | varchar | — | — | — | 通知事項（5=Eterm, 9=其他） |
| or02_date | datetime | — | — | — | 建檔時間（第一次上處理單位的時間，因為網單轉入FIT時就 INSERT 本筆） |
