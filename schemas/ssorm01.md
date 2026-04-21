# ssorm01 — 訂單副檔。訂單處理流程、會計入帳、授權控管與作業進度追蹤

**Aliases**: 訂單副檔, ssorm01, ORM01, SSORM01
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or01_ordr | varchar | — | PK | ssorm00.ordr_ordr | 訂單編號 |
| or01_year | varchar | — | — | ssorm00.ordr_year | 訂單年度 |
| or01_sts | varchar | — | — | — | 處理狀況（A=會計延時HK時間, R=RC, S=業務暫停拉HK處理） |
| or01_desc | varchar | — | — | — | 處理備註 |
| or01_prof | varchar | — | — | — | 處理單位 |
| or01_kk_time | datetime | — | — | — | 原訂單HK時間（處理時，將原訂單 Ordr_hk_time 欄記錄到本欄） |
| or01_kk_accdate | datetime | — | — | — | 出納入帳kk日期（會計延HK及線控授權KK記錄，及訂單KK日期） |
| or01_autorec | bit | — | — | — | HK訂單自動入帳（付款方式為信用卡且為HK團單，業務可勾選，日處理固定跑自動入帳） |
| or01_ename_err | int | — | — | — | 團單未入名單累計不合格人次（(含)8人以下，出納KK日+2工作日的1800計數） |
| or01_pd98no | varchar | — | — | — | 團單房價群組代號（新增 2023/06/21） |
| or01_pd98nomstfn | varchar | — | — | — | 房價群組代號維護人（新增 2023/06/21） |
| or01_pd98nomdate | datetime | — | — | — | 房價群組代號維護日（新增 2023/06/21） |
| or01_tdate | datetime | — | — | — | 訂單修改期限日（新增 2025/09/26） |
| or01_vstfn | varchar | — | — | — | 訂單取消者（新增 2023/03/23） |
| or01_vdate | datetime | — | — | — | 訂單取消日（新增 2023/03/23） |
| or01_prodlock | bit | — | — | — | 訂單作業鎖定（新增 2023/06/21） |
| or01_prodlockmstfn | varchar | — | — | — | 作業鎖定維護人（新增 2023/06/21） |
| or01_prodlockmdate | datetime | — | — | — | 作業鎖定維護日（新增 2023/06/21） |
| or01_bookflow | varchar | — | — | — | 訂單作業進度（新增 2023/06/21） |
| or01_bookflowmstfn | varchar | — | — | — | 作業進度維護人（新增 2023/06/21） |
| or01_bookflowmdate | datetime | — | — | — | 作業進度維護日（新增 2023/06/21） |
| or01_mdate | datetime | — | — | — | 處理(當地)時間 |
| or01_msysdate | datetime | — | — | — | 主機時間 |
| or01_mstfn | varchar | — | — | — | 處理者單位姓名+時區（格式：單位+姓名+空格+時區 ex: 直團王大明 TW） |
