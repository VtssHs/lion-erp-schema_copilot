# tppcm10 — 估價明細成本檔。儲存估價單中各成本項目的明細資料（機票、餐食、旅館、購物等）

**Aliases**: 估價明細成本檔, tppcm10, PCM10, TPPCM10
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp10_tpform | unknown | — | — | FK → `tppcm00.tp00_tpform` | 估價代號。除車成本外的所有成本（`tppcm00.tp00_tpform`） |
| tp10_no | unknown | — | — | — | 流水號（（與 tp10_tpform 組成複合鍵）） |
| tp10_order | unknown | — | — | — | 順序 |
| tp10_tpcost | unknown | — | — | — | 項目。機票及各項雜費 `istbm00(TPCOST)`，其他則固定字樣（行程: `WAY/V/SHOP/M/H/BAG/OPTION`（行李費同 HOTEL）） |
| tp10_ctokey | unknown | — | — | — | 元件代碼。有時才 join 各元件檔 |
| tp10_day | unknown | — | — | — | 日數。機票區塊日數及順序統一為 0，以 `istbm00` 的順序排 |
| tp10_meat | unknown | — | — | — | 餐別。1-早 2-午 3-晚 |
| tp10_curr | unknown | — | — | — | 幣別 |
| tp10_ncost | unknown | — | — | — | 未稅成本。機票區塊則一律存此，稅、退佣=0 做計算 |
| tp10_rate | unknown | — | — | — | 稅 %（加值型營業稅）。成本 = 未稅成本 × (100+稅–退佣) × (100+毛利) / 10000 |
| tp10_comm | unknown | — | — | — | 成本退佣 % |
| tp10_profit | unknown | — | — | — | 毛利 % |
| tp10_cost | unknown | — | — | — | 成本。估價用 - 依上列計算後 畫面存檔時，計算寫回（幣別同上）估價時要換算匯率 |
| tp10_foc | unknown | — | — | — | 有 Foc。只有機票非全攤的項目才可勾 |
| tp10_spec_git | unknown | — | — | — | 特殊檔次。有 Foc 時才可有特殊的檔次；HOTEL 以房為單位 |
| tp10_spec_foc | unknown | — | — | — | 特殊檔次 Foc。元件塊：有特殊檔次 Foc > 0 then 有 Foc = 1, Foc 成本 = 0 |
| tp10_ncost_foc | unknown | — | — | — | 未稅 Foc 成本 |
| tp10_cost_foc | unknown | — | — | — | Foc 成本。有勾 Foc 才 save 這個欄位 |
| tp10_myself | unknown | — | — | — | 自費。自費時，不計算成本；成本、Foc 成本 = 0 |
| tp10_desc | unknown | — | — | — | 備註 |
