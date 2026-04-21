# tppdm67 — 團體郵輪設定。記錄每個出發團的郵輪銷售設定，包含指定船隻、航期、艙等、艙房，以及線上選房、加購截止天數、鐵道路線等進階控制參數

**Aliases**: 團體郵輪設定, tppdm67, PDM67, TPPDM67
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM) — 郵輪子系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd67_prod | varchar | — | — | tppdm10.prod_prod | 團號 |
| pd67_prodcomp | varchar | — | PK | — | 團控公司 |
| pd67_cruiseno | varchar | — | — | — | 指定銷售 - 船 |
| pd67_sailing | varchar | — | — | — | 指定銷售 - 航期 |
| pd67_cabinid | varchar | — | — | — | 指定銷售 - 艙等 |
| pd67_crs20idno | varchar | — | — | — | 指定銷售 - 艙房明細 |
| pd67_liveqty | int | — | — | — | 指定銷售 - 可入住人數 |
| pd67_onlinebooking | varchar/bit | — | — | — | 指定銷售 - 開放線上選房（前台） |
| pd67_onlinebooking1 | varchar/bit | — | — | — | 指定銷售 - 開放線上選房（後台） |
| pd67_pakagtno | varchar | — | — | — | 指定郵輪 PAK 中心 |
| pd67_identify | varchar | — | — | — | 郵輪識別碼 |
| pd67_lastAddDayNum | int | — | — | — | 最晚加購天數（非獨包）（含出發當天，最大值 999） |
| pd67_AddTabManagement | varchar/bit | — | — | — | 是否管理自選頁簽（0=否，1=顯示/管理） |
| pd67_themedays | int | — | — | — | 主題鎖定天數（前台）（出發前 N 天鎖定） |
| pd67_themedays1 | int | — | — | — | 主題鎖定天數（後台）（出發前 N 天鎖定） |
| pd67_rtno | varchar | — | — | tppdm72.pd72_rtno | 鐵道路線代碼 |
| pd67_isenable | bit | — | — | — | 是否啟動 RPA（2024/06 新增） |
| pd67_mstfn | varchar | — | — | — | 維護者姓名（格式：單位+姓名） |
| pd67_msysdate | datetime | — | — | — | 維護時間 |
