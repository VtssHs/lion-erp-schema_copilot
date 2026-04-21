# wtorm20 — 訂位單航段檔。記錄訂位單中每個航段（含國內行程、火車/站）的詳細資訊，包含班機、出發地/抵達地、時間、艙等等

**Aliases**: 訂位單航段檔, 網位單管理系統, wtorm20, ORM20, WTORM20
**Database**: LionGroupERP
**Module**: 網位單管理系統 (Web Transaction Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| Wor20_wtordr | varchar | — | PK | wtorm00.Wor00_wtordr | 訂位單編號 |
| Wor20_wtyear | varchar | — | — | wtorm00.Wor00_wtyear | 訂位單年碼（；含國內行程火車(站)資料） |
| Wor20_seq | int | — | — | — | 序號（航段流水號） |
| Wor20_carr | varchar | — | — | — | 航空公司 |
| Wor20_flightNo | varchar | — | — | — | 班機號碼 |
| Wor20_codeshare | varchar | — | — | — | 聯營航空 |
| Wor20_equipment | varchar | — | — | — | 機型 |
| Wor20_flytime | int | — | — | — | 飛行時間（分鐘計算） |
| Wor20_comeback | varchar | — | — | — | 回程班機（0=去; 1=回（雙獅家緯需求）） |
| Wor20_seat | varchar | — | — | — | 座位（例：32A,32B） |
| Wor20_segment | varchar | — | — | — | 航段（用途待確認） |
| Wor20_sts | varchar | — | — | — | 狀況 |
| Wor20_class | varchar | — | — | — | 艙等代碼（For 雙獅 LCC 艙等為 2 碼） |
| Wor20_classname | varchar | — | — | — | 艙等名稱（ECONOMY=經濟艙; PREMIUM_ECONOMY=豪華經濟艙; BUSINESS=商務艙; FIRST=頭等艙） |
| Wor20_fairport | varchar | — | — | — | 出發地（機場代碼） |
| Wor20_fcity2 | varchar | — | — | — | 出發城市 |
| Wor20_fcountry2 | varchar | — | — | — | 出發國家（存中文字） |
| Wor20_Fterminal | varchar | — | — | — | 出發航廈 |
| Wor20_fdate | datetime | — | — | — | 出發日期 |
| Wor20_ftime | varchar | — | — | — | 出發時間 |
| Wor20_tairport | varchar | — | — | — | 抵達地（機場代碼） |
| Wor20_tcity2 | varchar | — | — | — | 抵達城市 |
| Wor20_tcountry2 | varchar | — | — | — | 抵達國家 |
| Wor20_Tterminal | varchar | — | — | — | 抵達航廈 |
| Wor20_tdate | datetime | — | — | — | 抵達日期 |
| Wor20_ttime | varchar | — | — | — | 抵達時間 |
| Wor20_service | varchar | — | — | — | 停留或轉機 |
