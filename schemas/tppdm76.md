# tppdm76 — 團產品預設圖檔。依線別與地區設定團體產品的預設圖片，新建團時自動套用

**Aliases**: 團產品預設圖檔, tppdm76, PDM76, TPPDM76
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd76_seq | int | — | PK | — | 流水序號（IDENTITY(1,1) 自增值，從 1 開始） |
| pd76_line | varchar(3) | — | — | FK → 線別代碼表，例如：歐洲線、美洲線 | 線別（主）（例如：歐洲線、美洲線） |
| pd76_dline | varchar(3) | — | — | FK → 副線別代碼表，細分線別 | 線別（副）（細分線別） |
| pd76_area | varchar(3) | — | — | FK → 地區代碼表，例如：西歐、東歐 | 地區（主）（例如：西歐、東歐） |
| pd76_darea | varchar(3) | — | — | FK → 細地區代碼表，更細緻的地區分類 | 地區（副）（更細緻的地區分類） |
| pd76_picno | varchar(100) | — | — | — | 圖檔路徑或編號（可能是檔案路徑或圖檔管理系統的編號） |
| pd76_count | int | — | — | — | 取用次數（統計該預設圖被使用的次數） |
