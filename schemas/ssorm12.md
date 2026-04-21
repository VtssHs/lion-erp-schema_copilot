# ssorm12 — 訂單明細副檔。記錄訂單旅客的補充資料，包含企業團專屬欄位、保險資訊、歐洲簽證資料、台胞證加簽、配偶資料等擴充欄位

**Aliases**: 訂單明細副檔, ssorm12, ORM12, SSORM12
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or12_ordr | varchar | — | PK | ssorm00.ordr_ordr | 訂單編號 |
| or12_year | varchar | — | — | ssorm00.ordr_year | 訂單年度（；For 簽證表格使用） |
| or12_seq | int | — | — | ssorm10.orer_seq | 訂單明細序號 |
| or12_comp | varchar | — | — | — | 公司名稱 |
| or12_comp2 | varchar | — | — | — | 分公司名稱 |
| or12_caddr | varchar | — | — | — | 公司地址 |
| or12_ecaddr | varchar | — | — | — | 公司英文地址 |
| or12_dept | varchar | — | — | — | 部門名稱 |
| or12_title | varchar | — | — | — | 職稱 |
| or12_jdate | datetime | — | — | — | 到職日期 |
| or12_salary | decimal | — | — | — | 年收入 |
| or12_bID | varchar | — | — | — | 受益人 idno |
| or12_bname | varchar | — | — | — | 受益人姓名 |
| or12_bplace | varchar | — | — | — | 出生地（For 歐洲簽證用） |
| or12_brelman | varchar | — | — | — | 受益人與被保險人關係（台壽: 1=本人 2=配偶 3=子女 4=父母 5=其他 6=兄弟姐妹 7=法定） |
| or12_eaddr | varchar | — | — | — | 住家英文地址 |
| or12_father_ename | varchar | — | — | — | 父親英文姓名 |
| or12_mother_ename | varchar | — | — | — | 母親英文姓名 |
| or12_spouse_ename | varchar | — | — | — | 配偶英文名（First Name） |
| or12_spouse_ename1 | varchar | — | — | — | 配偶英文姓（Last Name） |
| or12_spouse_bdate | datetime | — | — | — | 配偶出生日期 |
| or12_spouse_bplace | varchar | — | — | — | 配偶出生地 |
| or12_visa2_cn | varchar | — | — | — | 台胞加簽號碼 |
| or12_date2_cn | datetime | — | — | — | 台胞加簽日期 |
| or12_safeamt1 | decimal | — | — | — | 投保死殘金額（060208 國泰保險上傳資料） |
| or12_safeamt2 | decimal | — | — | — | 投保醫療金額 |
| or12_safeamt3 | decimal | — | — | — | 投保疾病金額 |
| or12_carr | varchar | — | — | — | 航班（主要企業團用，記錄每位旅客特別規格；名稱只是用來識別） |
| or12_ship | varchar | — | — | — | 船班 |
| or12_bus | varchar | — | — | — | 車號（只要該團統一即可；使用多團旅客資料表印出內容） |
| or12_room | varchar | — | — | — | 分房 |
| or12_desc | varchar | — | — | — | 特殊需求 |
| or12_color | varchar | — | — | — | 行李牌顏色 |
| or12_hat | varchar | — | — | — | 帽子顏色 |
| or12_size | varchar | — | — | — | 服裝大小 |
