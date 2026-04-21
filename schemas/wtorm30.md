# wtorm30 — 訂房記錄檔。記錄訂位單的每日訂房明細，每筆對應一個住宿日期的一種房型，為訂房訂單的核心明細檔

**Aliases**: 訂房記錄檔, 網位單管理系統, 訂房子系統, 記錄訂位單的每日訂房明細, 為訂房訂單的核心明細檔, wtorm30, ORM30, WTORM30
**Database**: LionGroupERP
**Module**: 網位單管理系統 (Web Transaction Order) - 訂房子系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| wor30_wtordr | varchar | — | — | wtorm00.Wor00_wtordr | 訂位單流水號 |
| wor30_wtyear | varchar | — | — | wtorm00.Wor00_wtyear | 訂位單年碼 |
| wor30_seq | varchar | — | — | — | 房型代碼（; 人工單/電話單存「序號+空白」） |
| wor30_date | datetime | — | PK | — | 住宿日期 |
| wor30_roomdesc | varchar | — | — | — | 房型說明 |
| wor30_amtkind | varchar | — | — | — | 房價類別 |
| wor30_orderseq | int | — | — | DBA | 商品明細紀錄流水號（-ERP2/Hotel:HTORM31.orderseq） |
| wor30_hor31descseq | int | — | — | HTORM31.HOR31_DESC | 詳細說明對應序（；同房型同入住區間的「詳」只記第一筆，需透過此欄取得正確資料） |
| wor30_act | int | — | — | — | 住房人數 |
| wor30_roomact | int | — | — | — | 入住人數（大人人數） |
| wor30_childqty | int | — | — | — | 小孩人數 |
| wor30_child1age | int | — | — | — | 第一位小孩歲數 |
| wor30_child2age | int | — | — | — | 第二位小孩歲數 |
| wor30_child3age | int | — | — | — | 第三位小孩歲數 |
| wor30_qty | int | — | — | — | 訂房數量 |
| wor30_amt | decimal | — | — | — | 房價 |
| wor30_amt_base | decimal | — | — | — | 基本售價（不包含加人加價之價格） |
| wor30_amt2 | decimal | — | — | — | 服務費（旅館國家=TW 時：房價 × 0.1） |
| wor30_b2b_amt | decimal | — | — | — | 批售價（通路公司成本） |
| wor30_b2c_amt | decimal | — | — | — | 直客價 |
| wor30_cost | decimal | — | — | — | 成本價格 |
| wor30_cost_base | decimal | — | — | — | 基本成本（不包含加人加價之成本） |
| wor30_discount | decimal | — | — | ophtm70 | 活動折扣 |
| wor30_local_discount | decimal | — | — | — | 供應商折扣 |
| wor30_curr | varchar | — | — | — | 幣別 |
| wor30_sale_curr | varchar | — | — | — | 銷售幣別 |
| wor30_confirm | varchar | — | — | — | 保證住房 |
| wor30_save | varchar | — | — | — | 保留房（2006/05/19 啟用） |
