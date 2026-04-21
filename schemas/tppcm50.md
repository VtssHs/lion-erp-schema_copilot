# tppcm50 — 估價單附件檔案管理表。儲存估價單相關的附件檔案資訊（行程 PDF、成本試算表、報價單等）

**Aliases**: 估價單附件檔案管理表, tppcm50, PCM50, TPPCM50
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp50_tpform | unknown | — | — | FK → `tppcm00.tp00_tpform` | 估價代號（`tppcm00.tp00_tpform`） |
| tp50_no | unknown | — | — | — | 序號（同一估價單的多個附件依序編號） |
| tp50_name | unknown | — | — | — | 文件內容（檔案說明或標題） |
| tp50_file | unknown | — | — | — | 文件目錄檔名/網址。目錄: `\html2\tour` 檔名: `tppc_出發訖日年碼_估價單號_序號.附檔名` Ex: `tppc_14_1305100001_1.xls（實體檔案路徑或 URL） |
| tp50_date | unknown | — | — | — | 上傳時間（檔案首次上傳時間） |
| tp50_stfn | unknown | — | — | — | 上傳者員編（上傳人員工代碼） |
| tp50_stfnname | unknown | — | — | — | 上傳者單位+姓名。ex: 資訊王大明（上傳人員單位與姓名） |
| tp50_mdate | unknown | — | — | — | 增修當地時間（最後修改時間） |
| tp50_mstfn | unknown | — | — | — | 增修者單位姓名時區。單位+姓名+空格+時區 ex:直團王大明 TW（最後修改人員資訊） |
| tp50_sts | unknown | — | — | — | 已作廢（1-已作廢，空白或 0-有效） |
