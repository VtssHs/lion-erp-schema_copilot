# tppdm19a — 團體滿意度調查統計副檔。記錄團體滿意度調查的統計分類資料（職業、報名方式、參團來源等）

**Aliases**: 團體滿意度調查統計副檔, 說明會相關, tppdm19a, PDM19A, TPPDM19A
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product) - 說明會相關

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| p19a_prod | varchar | — | PK | tppdm10.prod_prod | 團號（(part)） |
| p19a_prodcomp | varchar | — | — | — | 團控公司 |
| p19a_type | varchar | — | PK | FK → ISTBM00 (TPPD19_代碼) | 統計類別（(part), , 1=職業, 2=報名方式, 3=參團來源, 4=再參團原因, 5=下次旅遊時間, 6=下次旅遊地點, 7=訂購雜誌類別） |
| p19a_kind | varchar | — | PK | — | 統計次類別（(part), 各統計類別下的細分項目） |
| p19a_man | int | — | — | — | 累計人數（此類別/次類別的人數統計） |
