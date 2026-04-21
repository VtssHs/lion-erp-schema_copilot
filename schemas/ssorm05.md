# ssorm05 — 各產品網單同意記錄檔。記錄客戶於網路下單時對報名需知、旅遊契約書、個資同意等項目的確認記錄

**Aliases**: 各產品網單同意記錄檔, ssorm05, ORM05, SSORM05
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or05_ordr | varchar | — | — | ssorm00.ordr_ordr | 訂單(網位單)編號（團單 ; 非團單產品） |
| or05_year | varchar | — | PK | — | 訂單(網位單)年度 |
| or05_type | varchar | — | — | — | 同意項目（空白=報名需知&旅遊契約書, 1=個資確認） |
| or05_time | datetime | — | — | — | 同意時間（記錄客人同意須知時間） |
