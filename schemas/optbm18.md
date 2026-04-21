# optbm18 — 城市區域檔。CTO 元件的城市區域分類主檔，用於城市區域的三階結構管理（國家-城市-區域）

**Aliases**: 城市區域檔, 景點與旅遊地點管理, 元件的城市區域分類主檔, optbm18, TBM18, OPTBM18
**Database**: LionGroupERP
**Module**: 景點與旅遊地點管理 (OPTBM)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| ct18_country | varchar | — | PK | — | 所在國代碼（**PK1**） |
| ct18_city | varchar | — | — | — | 城市代碼（**PK2**） |
| ct18_cityzone | varchar | — | — | — | 區域代碼（**PK3**） |
| ct18_name | varchar | — | — | — | 名稱（區域的正式名稱） |
| ct18_dname | varchar | — | — | — | 顯示名稱（前台或系統顯示用的名稱） |
| ct18_desc | varchar | — | — | — | 分區描述（區域的詳細說明） |
| ct18_cto | varchar | — | — | — | CTO 基準區域（該區域在 CTO 系統中的基準分類） |
| ct18_show | bit | — | — | — | 有元件資料的城市區域（由國家的「設定 CTO 元件國家」功能做設定） |
| ct18_weborder | int | — | — | — | 網上顯示順序（255 = 不在 search 下拉 bar 上顯示） |
| ct18_proorder | int | — | — | — | 達人館順序（不知何用（待確認）） |
| ct18_pro_pic | varchar | — | — | — | 達人館的區圖片（區域代表圖片路徑） |
