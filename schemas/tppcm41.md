# tppcm41 — 檔次成本明細檔。儲存各檔次中各成本項目的明細金額（機票、旅館、餐食等分項成本）

**Aliases**: 檔次成本明細檔, tppcm41, PCM41, TPPCM41
**Database**: LionGroupERP
**Module**: 團體估價系統

## Columns

| Column | Type | Null | Key | FK | Description |
|--------|------|------|-----|-----|-------------|
| tp41_tpform | unknown | — | — | FK → `tppcm00.tp00_tpform` | 估價代號（`tppcm00.tp00_tpform`） |
| tp41_size | unknown | — | — | — | 檔次（1~6，對應不同人數檔次） |
| tp41_tpcost | unknown | — | — | — | 項目。同 tppcm10（對應 `tppcm10.tp10_tpcost`，如：機票、旅館、餐食） |
| tp41_name | unknown | — | — | — | 項目名。不是 tppcm10 來的沒有名稱，計算時要回寫，否則看不出啥項目 ZCar-車資*, zRoom-單房間差*（因要擺最下頭）（計算後回寫） |
| tp41_cost | unknown | — | — | — | 各項累計成本/人。計算時，計算後回寫（每人分攤的項目成本） |
