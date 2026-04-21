# ssorm13 — 商務部旅客機票資料。記錄商務部（企業差旅）旅客的機票詳細資訊，包含航班、票價、PNR、企業申請單、簽證辦理等專業資料

**Aliases**: 商務部旅客機票資料, ssorm13, ORM13, SSORM13
**Database**: LionGroupERP
**Module**: 訂單管理系統 (Sales Order)

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| or13_ordr | varchar | — | — | ssorm10.orer_ordr | 訂單編號 |
| or13_year | varchar | — | — | ssorm10.orer_year | 訂單年碼 |
| or13_seq | int | — | PK | — | 序號 |
| or13_fdate | datetime | — | — | — | 出發日 |
| or13_fflightNo | varchar | — | — | — | 出發航班 |
| or13_tdate | datetime | — | — | — | 回程日 |
| or13_tflightNo | varchar | — | — | — | 回程航班 |
| or13_carr | varchar | — | — | — | 票源航空公司（如：BR） |
| or13_al | varchar | — | — | — | 航段內航空公司（如：BR/MU/MU/BR） |
| or13_class | varchar | — | — | — | 航段內艙等（如：Y/M/M/Y） |
| or13_rtid | varchar | — | — | — | 航段（如：TPE/HKG/SHA/HKG/SHA） |
| or13_country | varchar | — | — | — | 目的地國家 |
| or13_city | varchar | — | — | — | 目的地城市 |
| or13_name | varchar | — | — | — | 行程(產品名稱)（原 crtid） |
| or13_bsp_amt | decimal | — | — | — | BSP票價 |
| or13_tax1 | decimal | — | — | — | 燃油稅 |
| or13_tax9 | decimal | — | — | — | 其他稅金 |
| or13_amt4 | decimal | — | — | — | 手續費 |
| or13_pnr | varchar | — | — | — | PNR（1E=Eterm, ZZ=其他; 其中 AB 及 AM 才可以用 PNR 帶入訂位資料） |
| or13_crs | varchar | — | — | — | CRS系統（AB=Abacus, 1G=Galileo, AM=Amadeus, AL=AirLine） |
| or13_pnr_ldate | datetime | — | — | — | PNR最後修改日 |
| or13_pnr_qty | int | — | — | — | PNR修改次數 |
| or13_tkno | varchar | — | — | — | 機票號碼（格式: xxx xxxxxxxxxx/ xxx xxxxxxxxxx 目前最多3組） |
| or13_reissue | bit | — | — | — | Re票（1=re票） |
| or13_empid | varchar | — | — | — | 旅客員工編號 |
| or13_empid2 | varchar | — | — | — | 代訂員編 |
| or13_deptid | varchar | — | — | — | 旅客部門代號 |
| or13_dept_name | varchar | — | — | — | 分公司名稱 |
| or13_orderid | varchar | — | — | — | 旅客企業内的申請單號 |
| or13_proj | varchar | — | — | — | 專案代號 |
| or13_request | varchar | — | — | — | 差旅/個人（0=差旅, 1=個人） |
| or13_request_date | datetime | — | — | — | 需求日期 |
| or13_travel_purpose | varchar | — | — | — | 差旅目的 |
| or13_vscountry | varchar | — | — | — | 證照國家 |
| or13_vsseq | varchar | — | — | — | 證照類別（1=已送件, F=已完成, B=補件中） |
| or13_visa_flow | varchar | — | — | — | 辦證進度 |
| or13_visa_date | datetime | — | — | — | 預計辦好日 |
| or13_hotel | varchar | — | — | — | 旅館代號 |
| or13_night | int | — | — | — | 旅館住x晚 |
| or13_desc | varchar | — | — | — | 企業特殊說明 1 |
| or13_desc2 | varchar | — | — | — | 企業特殊說明 2 |
| or13_desc3 | varchar | — | — | — | 企業特殊說明 3 |
| or13_desc4 | varchar | — | — | — | 企業特殊說明 4 |
| or13_fnio1 | varchar | — | — | — | 代轉編號1 |
| or13_fnio2 | varchar | — | — | — | 代轉編號2 |
| or13_fnio3 | varchar | — | — | — | 代轉編號3 |
| or13_mileage | int | — | — | — | 哩程數 |
| or13_co2 | decimal | — | — | — | 排碳量 |
