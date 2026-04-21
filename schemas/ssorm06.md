# ssorm06 — 訂單保險資料副檔。記錄訂單的旅遊保險資料，包含國泰保險上傳資料、保單號碼、航班資訊與投保明細

**Aliases**: 訂單保險資料副檔, 航班資訊與投保明細, ssorm06, ORM06, SSORM06
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or06_ordr | varchar | — | PK | ssorm00.ordr_ordr | 訂單編號 |
| or06_year | varchar | — | — | ssorm00.ordr_year | 訂單年度 |
| or06_safeno | varchar | — | — | — | 保險證號（保單號碼） |
| or06_safeseq | varchar | — | — | — | 保險收件序號 |
| or06_SafeInsComp | varchar | — | — | — | 投保對象代碼（保險公司代碼） |
| or06_safecode | varchar | — | — | — | 承辦單位 |
| or06_safefair | varchar | — | — | — | 出發航班（國泰保險上傳資料） |
| or06_safetair | varchar | — | — | — | 回程航班 |
| or06_days | int | — | — | — | 投保天數 |
| or06_safedate | datetime | — | — | — | 保險起時（保險生效時間） |
| or06_safemode | varchar | — | — | — | 交通工具（如：飛機、火車、遊輪） |
| or06_saferate | decimal | — | — | — | 費率 |
| or06_safepay | varchar | — | — | — | 送金單號（保險費用繳納單號） |
| 1 | varchar/bit | — | — | — | 保單列印及下載（申請單號：19122268） |
| or06_mstfn | varchar | — | — | — | 增修人（2011後都沒有 update 本欄） |
| or06_mdate | datetime | — | — | — | 增修時間（2011後都沒有 update 本欄） |
