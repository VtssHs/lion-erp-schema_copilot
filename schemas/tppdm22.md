# tppdm22 — 自由行行程檔。自由行產品的行程細節（與團體行程結構不同）

**Aliases**: 自由行行程檔, tppdm22, PDM22, TPPDM22
**Database**: LionGroupERP
**Module**: 團體產品系統 (Group Product)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| pd22_tur2 | varchar(20) | — | PK | tppdm20.pd20_tur2 | 行程代號（**PK1**, , 複製不copy本檔） |
| pd22_num | int | — | — | — | 流水號（**PK2**, 每個行程內的序號） |
| pd22_seq | int | — | — | — | 序號（**PK3**, 使用者自編的流水號（如第4種）） |
| pd22_unit | varchar(20) | — | — | — | 資料單位（內容類別或區分用） |
| pd22_chgline | bit | — | — | — | 內容換行（控制顯示格式） |
| pd22_desc | nvarchar(max) | — | — | — | 內容說明（自由行行程詳細描述） |
| pd22_hotel | nvarchar(500) | — | — | — | 旅館簡介（住宿資訊） |
| pd22_meat | nvarchar(500) | — | — | — | 餐食簡介（用餐資訊） |
