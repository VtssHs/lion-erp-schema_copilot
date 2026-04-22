# 外部引用白名單(indexes/external_refs.md)

> **用途**:列出所有 `fk:` 或 `fk_note:` 指向 **但不在本 repo 的 schemas/ 中** 的 table
> **自動產出**,每次 build 時重生
> **Copilot 使用時機**:看到 FK 指向陌生 table 時,先查此檔確認是否為已知外部引用

---

## 一、外部系統對照

按 table 前綴,推測應查哪個外部來源:

| Prefix | 可能所屬系統 | 應查詢 |
|--------|------------|-------|
| `opagm*` | 法人 / 員工主檔 | `erp-schema` skill(OPAGM 模組)或 LionGroupRPM |
| `optbm*` | 基礎代碼 | `erp-schema` skill(OPTBM 模組) |
| `optnm*` | 活動節目主檔 | `erp-schema` skill 或 CTOM 模組 |
| `ophtm*` | 旅館主檔(CTO 元件) | `erp-schema` skill(OPHTM 模組) |
| `opmtm*` | 餐廳主檔(CTO 元件) | `erp-schema` skill(OPMTM 模組) |
| `opbsm*` | 車公司主檔(CTO 元件) | `erp-schema` skill(OPBSM 模組) |
| `opvim*` | 景點主檔(CTO 元件) | `erp-schema` skill(OPVIM 模組) |
| `opspm*` | 商店主檔(CTO 元件) | `erp-schema` skill |
| `ctom*` | CTO 元件管理 | `erp-schema` skill(CTOM 模組) |
| `iscpm1*` 系列 | 公司刷卡 / 副檔 | `erp-schema` skill(ISCPM 模組,部分未建檔) |
| `gitpcm*` | PCM 產品管理 | `pcm-schema` skill(LionGroupRPM) |
| `trip00` 系列 | 行程組合器 | `trip-composer-schema` skill(LionGroupRPM) |
| POI / Area | CMS 景點主檔 | `cms-schema` skill(LionGroupCMS) |
| `PCM.dbo.*` | 舊 PCM database | ⚠️ 已下線,須改為指向 `gitpcm*`(LionGroupRPM) |
| `HTORM*` | 房產訂房明細 | `erp-schema` skill(HTORM 模組,部分未建檔) |

---

## 二、完整外部引用清單

共 **18** 個不同的外部目標。

### `(中文命名外部主檔)`

被 **22** 個欄位引用:

- `bookm00.bk00_ctokey` — 原始 fk_note:`FK → 各類別主檔 (ophtm/opmtm/opbsm/opvim/opspm)`
- `tppdm16.pd16_vscountry1` — 原始 fk_note:`FK → 國家代碼表`
- `tppdm16.pd16_vsseq1` — 原始 fk_note:`FK → 簽證類型表`
- `tppdm16.pd16_vscountry2` — 原始 fk_note:`FK → 國家代碼表`
- `tppdm16.pd16_vsseq2` — 原始 fk_note:`FK → 簽證類型表`
- `tppdm16.pd16_safecode` — 原始 fk_note:`FK → 保險承辦單位代碼表`
- `tppdm16.pd16_safemode` — 原始 fk_note:`FK → 交通工具代碼表`
- `tppdm16.pd16_SafeInsComp` — 原始 fk_note:`FK → 保險公司代碼表`
- `tppdm20.pd20_prodname` — 原始 fk_note:`FK → 標準團名檔，有值時行程名稱=NULL`
- `tppdm24.pd24_ctokey` — 原始 fk_note:`FK → 對應的主檔（景點/餐廳/旅館/商店）`
- `tppdm50.pd50_hotel` — 原始 fk_note:`FK → 旅館主檔 (ophtm*)`
- `tppdm55.pd55_bkstfn` — 原始 fk_note:`只存第一次設定者，FK → 員工主檔`
- `tppdm56.pd56_local` — 原始 fk_note:`**PK1**, FK → 供應商主檔，配合 B2P 系統型態`
- `tppdm56.pd56_code` — 原始 fk_note:`FK → 欄位代碼主檔`
- `tppdm57.pd57_local` — 原始 fk_note:`**PK2**, FK → 供應商主檔`
- `tppdm57.pd57_coltype` — 原始 fk_note:`**PK3**, FK → 欄位代碼主檔`
- `tppdm76.pd76_line` — 原始 fk_note:`FK → 線別代碼表，例如：歐洲線、美洲線`
- `tppdm76.pd76_dline` — 原始 fk_note:`FK → 副線別代碼表，細分線別`
- `tppdm76.pd76_area` — 原始 fk_note:`FK → 地區代碼表，例如：西歐、東歐`
- `tppdm76.pd76_darea` — 原始 fk_note:`FK → 細地區代碼表，更細緻的地區分類`
- `tppdm98.pd98_hotel` — 原始 fk_note:`FK → 旅館主檔，該方案主要使用的旅館`
- `tppdm98.pd98_mstfn` — 原始 fk_note:`FK → 員工主檔`

### `tptbm`

被 **4** 個欄位引用:

- `tppdm20.pd20_line`
- `tppdm20.pd20_dline`
- `tppdm20.pd20_area`
- `tppdm20.pd20_darea`

### `optbm20`

被 **4** 個欄位引用:

- `tppdm26.pd26_station` — 原始 fk_note:`optbm20.tb20_station`
- `tppdm26.pd26_station1` — 原始 fk_note:`optbm20.tb20_station`
- `tppdm36.pd36_station` — 原始 fk_note:`optbm20.tb20_station`
- `tppdm36.pd36_station1` — 原始 fk_note:`optbm20.tb20_station`

### `optbm30`

被 **2** 個欄位引用:

- `bookm00.bk00_meatstyle`
- `bookm01.bk01_meatstyle`

### `optnm00`

被 **2** 個欄位引用:

- `tppdm15.pd15_option`
- `tppdm23.pd23_option`

### `optbm11`

被 **2** 個欄位引用:

- `tppdm40.pd40_fairport`
- `tppdm40.pd40_tairport`

### `opagm10`

被 **1** 個欄位引用:

- `bookm00.bk00_local`

### `iscpm11`

被 **1** 個欄位引用:

- `bookm00.bk00_payfor`

### `optbm70`

被 **1** 個欄位引用:

- `bookm00.bk00_bus_carr`

### `customer`

被 **1** 個欄位引用:

- `ssorm00.ordr_cust`

### `opagm20`

被 **1** 個欄位引用:

- `tppdm14.pd14_tl`

### `PCM`

被 **1** 個欄位引用:

- `tppdm20.pd20_tripidno` — 原始 fk_note:`PCM.dbo`

### `B2P供應商主檔`

被 **1** 個欄位引用:

- `tppdm55.pd55_local`

### `opvim00`

被 **1** 個欄位引用:

- `tppdm63.pd63_view`

### `tppdm72`

被 **1** 個欄位引用:

- `tppdm67.pd67_rtno` — 原始 fk_note:`tppdm72.pd72_rtno`

### `DBA`

被 **1** 個欄位引用:

- `wtorm30.wor30_orderseq`

### `HTORM31`

被 **1** 個欄位引用:

- `wtorm30.wor30_hor31descseq` — 原始 fk_note:`HTORM31.HOR31_DESC`

### `ophtm70`

被 **1** 個欄位引用:

- `wtorm30.wor30_discount`

---

## 三、Copilot 使用規則

讀本檔案時必須遵守:

1. **目標 table 在本清單中**:
   - 禁止 hallucinate 該 table 的欄位
   - 必須告知使用者:「此 FK 指向 `{target}`,不在本 repo 中,建議查詢 `{對應 skill}`」
   - 可產出 SQL 的 FROM / JOIN,但註解標示「外部 table,欄位需另行確認」

2. **目標 table 不在本清單**:
   - 先查 schemas/ 看是不是內部 table
   - 若不在 schemas/ 也不在本清單,**可能是 YAML 填錯**,應告知使用者「此 FK 目標未知,建議檢查來源 YAML」

3. **`PCM.dbo.*` 是舊參照**:遇到這類 FK 必須主動提醒使用者 PCM database 已下線,需改指 `gitpcm*`(LionGroupRPM)。
