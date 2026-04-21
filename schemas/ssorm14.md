# ssorm14 — 商務部旅客機票航段資料。記錄商務部機票的詳細航段資訊，補充 ssorm13 的航班資料，提供每個航段的機場、日期、哩程等明細

**Aliases**: 商務部旅客機票航段資料, 哩程等明細, ssorm14, ORM14, SSORM14
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or14_ordr | varchar | — | PK | ssorm13.or13_ordr | 訂單編號 |
| or14_year | varchar | — | — | ssorm13.or13_year | 訂單年度（用結團為產銷可修改權限的切點） |
| or14_seq | int | — | — | ssorm13.or13_seq | 序號 |
| or14_segment | int | — | — | — | 航段編號（航段流水號（1, 2, 3...）） |
| or14_fairport | varchar | — | — | — | 出發機場（機場代碼（如：TPE, HKG, NRT）） |
| or14_fdate | datetime | — | — | — | 出發日期（該航段出發時間） |
| or14_tairport | varchar | — | — | — | 目的機場（機場代碼） |
| or14_tdate | datetime | — | — | — | 抵達日期（該航段抵達時間） |
| or14_mileage | int | — | — | — | 哩程數（該航段的飛行哩程） |
