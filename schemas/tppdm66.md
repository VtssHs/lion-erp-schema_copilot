# tppdm66 — 郵輪相關檔案（岸上觀光訂單關聯）。記錄郵輪岸上觀光車次與訂單旅客的關聯，將訂單明細（ordr + year + seq）掛載到特定岸上觀光車次

**Aliases**: 郵輪相關檔案, 岸上觀光訂單關聯, tppdm66, PDM66, TPPDM66
**Database**: LionGroupERP
**Module**: 團體產品管理 (TPPDM) — 郵輪子系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd66_localtour | varchar | — | PK | tppdm62.pd62_localtour | 岸上觀光編號 |
| pd66_date | datetime | — | — | tppdm64.pd64_date | 岸上觀光日期 |
| pd66_bus | varchar | — | — | tppdm64.pd64_bus | 車次 |
| pd66_ordr | varchar | — | — | ssorm00.ordr_ordr | 訂單號 |
| pd66_year | varchar | — | — | ssorm00.ordr_year | 訂單年 |
| pd66_seq | int | — | — | ssorm10.orer_seq | 訂單序號 |
| pd66_mstfn | varchar | — | — | — | 維護者姓名及時區（格式：單位+姓名+空格+時區，例：`直團王大明 TW`） |
| pd66_msysdate | datetime | — | — | — | 當地維護時間 |
