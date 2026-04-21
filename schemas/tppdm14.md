# tppdm14 — 團體領隊建議核派名單檔。區分同一團的多位候選人

**Aliases**: 團體領隊建議核派名單檔, tppdm14, PDM14, TPPDM14
**Database**: LionGroupERP
**Module**: TPPDM - 團體產品管理

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd14_prod | varchar(20) | NOT NULL | PK | — | 團號 |
| pd14_prodcomp | varchar(2) | NOT NULL | PK | — | 團控公司 |
| pd14_seq | int | NOT NULL | — | — | 序號（同一團可有多位候選領隊） |
| pd14_tl | varchar(10) | NULL | — | opagm20 | 員編（領隊員工編號） |
| pd14_name | varchar(50) | NULL | — | — | 姓名（領隊姓名） |
| pd14_sts | char(1) | NULL | — | — | 建議/核派/自薦（0-建議, 1-核派, 2-自薦（滑雪教練）） |
| pd14_tlsta | char(1) | NULL | — | — | 身份（空白-專業, 1-員工, 2-同行借調） |
| pd14_main | char(1) | NULL | — | — | 主領隊（主領隊標記，回寫到 tppdm12） |
