# ssorm03 — 訂單帳款副檔。訂單業績計算、應收帳款管理與匯率處理

**Aliases**: 訂單帳款副檔, ssorm03, ORM03, SSORM03
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or03_ordr | varchar | — | PK | ssorm00.ordr_ordr | 訂單編號 |
| or03_year | varchar | — | — | ssorm00.ordr_year | 訂單年度 |
| or03_amt | decimal | — | — | — | 交易金額（由訂單功能設定3個欄位） |
| or03_curr | varchar | — | — | — | 交易幣別（訂單新增依 opagm93 預設幣別） |
| or03_erat | decimal | — | — | — | 報價匯率 |
| or03_countym | varchar | — | — | — | 業績年月（NULL=訂單新增待計算, 0=修改待計算, 1=已計算, F=由財會手動設定） |
| or03_prof | varchar | — | — | — | 業績單位 |
| or03_sales | varchar | — | — | — | 業績業務 |
| or03_team | varchar | — | — | — | 業績組別（記錄第一次計算訂單業績的業務，之後的異動都算該名業務） |
| or03_rdate | datetime | — | — | — | 應收帳款日 |
| or03_rdate_tran | datetime | — | — | — | 已計算應收帳款日 |
| or03_rpct | decimal | — | — | — | 應收帳款尾款百分比（預設100; 若為NULL也是100; 例：尾款10則表示90%在出發日收足，10%是在 or03_rdate 才要收。新增 2021/04/28） |
