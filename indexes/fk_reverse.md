# FK 反向索引(indexes/fk_reverse.md)

> **用途**:查詢「哪些 table 引用了 X」— 支援影響範圍分析
> **自動產出,請勿手動編輯**(每次 build 從 tables/*.yaml 重生)
> **Copilot 使用時機**:當使用者問「改 X 會影響哪些 table」「誰引用 X」「X 的 downstream」

---

## 一、快速查詢表

每張 table 被引用次數。次數高者為系統樞紐,改動成本高。

| Target Table | 被引用次數 | 主要描述 |
|--------------|-----------|----------|
| `tppdm10` | 25 | 團體主檔 |
| `istbm00` | 23 | 基礎代碼主檔 |
| `ssorm00` | 19 | 訂單主檔 |
| `tppcm00` | 8 | 團體產品估價主檔 |
| `isbum00` | 7 | Bu 事業體主檔 |
| `ssorm10` | 7 | 訂單明細檔 |
| `tppdm20` | 7 | 團體行程代號主檔 |
| `wtorm00` | 6 | 訂位單主檔 |
| `tptbm10` | 5 | 團體銷售資訊說明檔 |
| `tptbm20` | 4 | 前台旅遊地區代碼檔 |
| `tptbm00` | 4 | 標準團名資料檔 |
| `ssorm13` | 3 | 商務部旅客機票資料 |
| `istbm10` | 3 | 線別代碼檔 |
| `tptrm20` | 3 | 旅遊館 |
| `istbm83` | 2 | 公用標籤檔 |
| `tppcm40` | 2 | 檔次報價總表 |
| `tppdm20_ez` | 2 | 易遊行程主檔 |
| `tppdm62` | 2 | 郵輪岸上觀光主檔 |
| `tppdm64` | 2 | 郵輪岸上觀光車次 |
| `isbum01` | 2 | bu事業體頻道 |
| `tptrm30` | 2 | 旅遊館群組 |
| `bookm00` | 1 | 預訂主檔 |
| `tppdm98` | 1 | 團多房價群組檔 |

零引用 table 共 83 張,見 [§三](#三零引用-table)。

---

## 二、詳細反向索引

格式:`source_table.source_column → target_table[.target_column]`

### `tppdm10` — 團體主檔

**標準 FK (25 筆)**:

- `bookm00.bk00_prod` → `tppdm10.prod_prod`
- `ssorm00.ordr_prod` → `tppdm10.prod_prod`
- `tppdm11.pd11_prod` → `tppdm10.prod_prod`
- `tppdm12.pd12_prod` → `tppdm10.prod_prod`
- `tppdm15.pd15_prod` → `tppdm10.prod_prod`
- `tppdm16.pd16_prod` → `tppdm10.prod_prod`
- `tppdm17.pd17_prod` → `tppdm10.prod_prod`
- `tppdm17.pd17_chdprod` → `tppdm10.prod_prod`
- `tppdm18.pd18_prod` → `tppdm10.prod_prod`
- `tppdm19.pd19_prod` → `tppdm10.prod_prod`
- `tppdm19a.p19a_prod` → `tppdm10.prod_prod`
- `tppdm30.pd30_prod` → `tppdm10.tpdm10_geno`
- `tppdm36.pd36_prod` → `tppdm10.prod_prod`
- `tppdm41.pd41_prod` → `tppdm10.prod_prod`
- `tppdm50.pd50_prod` → `tppdm10.prod_prod`
- `tppdm55.pd55_prod` → `tppdm10.prod_prod`
- `tppdm57.pd57_prod` → `tppdm10.prod_prod`
- `tppdm60.pd60_prod` → `tppdm10.prod_prod`
- `tppdm65.pd65_prod` → `tppdm10.prod_prod`
- `tppdm67.pd67_prod` → `tppdm10.prod_prod`
- `tppdm81.pd81_prod` → `tppdm10.prod_prod`
- `tppdm90.pd90_prod` → `tppdm10.prod_prod`
- `tppdm91.pd91_prod` → `tppdm10.prod_prod`
- `tppdm92.pd92_prod` → `tppdm10.prod_prod`
- `tppdm98.pd98_prod` → `tppdm10.prod_prod`

### `istbm00` — 基礎代碼主檔

**標準 FK (1 筆)**:

- `tppdm10.prod_project` → `istbm00`

**來自 fk_note (需驗證,22 筆)**:

- `ssorm02.or02_crs` — 原文:`FK → Istbm00 (CRSKIND)`
- `ssorm10.orer_tairline` — 原文:`FK → Istbm00 (TAIRLINE)`
- `ssorm11.or11_urgent_relman` — 原文:`FK → Istbm00 (RELMAN)`
- `ssorm11.or11_meat` — 原文:`FK → Istbm00 (MEAT)`
- `tppdm10.prod_form` — 原文:`FK → Istbm00 (FORM)`
- `tppdm12.pd12_meetplace` — 原文:`FK → Istbm00 (MEET)`
- `tppdm19a.p19a_type` — 原文:`FK → ISTBM00 (TPPD19_代碼)`
- `tptbm00.tbm0_attr1` — 原文:`FK → istbm00 (ATTR)`
- `tptbm00.tbm0_attr2` — 原文:`FK → istbm00 (ATTR)`
- `tptbm00.tbm0_attr3` — 原文:`FK → istbm00 (ATTR)`
- `tptbm00.tbm0_psubject1` — 原文:`FK → istbm00 (PSUBJECT)`
- `tptbm00.tbm0_psubject2` — 原文:`FK → istbm00 (PSUBJECT)`
- `tptbm00.tbm0_psubject3` — 原文:`FK → istbm00 (PSUBJECT)`
- `tptbm10.note_note` — 原文:`FK → Istbm00 (NOTE)`
- `tptrm20.tr20_freekind` — 原文:`FK → istbm00 (FREEKIND)`
- `tptrm32.tr32_pdhot` — 原文:`FK → istbm00 (PDHOT)`
- `wtorm00.Wor00_ordrin1` — 原文:`FK → Istbm00 (ORDRIN1)`
- `wtorm00.Wor00_ordrin2` — 原文:`FK → Istbm00 (ORDRIN2)`
- `wtorm00.Wor00_crs` — 原文:`FK → Istbm00 (CRSKIND)`
- `wtorm00.wor00_cxldesc` — 原文:`FK → istbm00 (CXLDESC)`
- `wtorm00.wor00_cxldesc2` — 原文:`FK → istbm00 (CXLDESC2)`
- `wtorm10.wor10_tkperiod` — 原文:`FK → Istbm00 (TKPERIOD)`

### `ssorm00` — 訂單主檔

**標準 FK (19 筆)**:

- `ssorm01.or01_ordr` → `ssorm00.ordr_ordr`
- `ssorm01.or01_year` → `ssorm00.ordr_year`
- `ssorm02.or02_ordr` → `ssorm00.ordr_ordr`
- `ssorm02.or02_year` → `ssorm00.ordr_year`
- `ssorm03.or03_ordr` → `ssorm00.ordr_ordr`
- `ssorm03.or03_year` → `ssorm00.ordr_year`
- `ssorm04.or04_ordr` → `ssorm00.ordr_ordr`
- `ssorm04.or04_year` → `ssorm00.ordr_year`
- `ssorm05.or05_ordr` → `ssorm00.ordr_ordr`
- `ssorm06.or06_ordr` → `ssorm00.ordr_ordr`
- `ssorm06.or06_year` → `ssorm00.ordr_year`
- `ssorm07.or07_ordr` → `ssorm00.ordr_ordr`
- `ssorm07.or07_year` → `ssorm00.ordr_year`
- `ssorm10.orer_ordr` → `ssorm00.ordr_ordr`
- `ssorm10.orer_year` → `ssorm00.ordr_year`
- `ssorm12.or12_ordr` → `ssorm00.ordr_ordr`
- `ssorm12.or12_year` → `ssorm00.ordr_year`
- `tppdm66.pd66_ordr` → `ssorm00.ordr_ordr`
- `tppdm66.pd66_year` → `ssorm00.ordr_year`

### `tppcm00` — 團體產品估價主檔

**來自 fk_note (需驗證,8 筆)**:

- `tppcm09.tp09_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm10.tp10_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm20.tp20_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm21.tp21_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm30.tp30_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm40.tp40_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm41.tp41_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm50.tp50_tpform` — 原文:`FK → `tppcm00.tp00_tpform``

### `isbum00` — Bu 事業體主檔

**標準 FK (7 筆)**:

- `ispfm00.prof_bu` → `isbum00`
- `tppdm91.pd91_bu` → `isbum00.bu00_bu`
- `tppdm92.pd92_bu` → `isbum00.bu00_bu`
- `tppdm93.pd93_chlbu` → `isbum00.bu00_bu`
- `tppdm93.pd93_prodbu` → `isbum00.bu00_bu`
- `tptbm20.tb20_bu` → `isbum00`
- `wtorm00.wor00_bu` → `isbum00`

### `ssorm10` — 訂單明細檔

**標準 FK (7 筆)**:

- `ssorm11.or11_ordr` → `ssorm10.orer_ordr`
- `ssorm11.or11_year` → `ssorm10.orer_year`
- `ssorm11.or11_seq` → `ssorm10.orer_seq`
- `ssorm12.or12_seq` → `ssorm10.orer_seq`
- `ssorm13.or13_ordr` → `ssorm10.orer_ordr`
- `ssorm13.or13_year` → `ssorm10.orer_year`
- `tppdm66.pd66_seq` → `ssorm10.orer_seq`

### `tppdm20` — 團體行程代號主檔

**標準 FK (6 筆)**:

- `tppdm21.pd21_tur2` → `tppdm20.pd20_tur2`
- `tppdm22.pd22_tur2` → `tppdm20.pd20_tur2`
- `tppdm23.pd23_tur2` → `tppdm20.pd20_tur2`
- `tppdm24.pd24_tur2` → `tppdm20.pd20_tur2`
- `tppdm26.pd26_tur2` → `tppdm20.pd20_tur2`
- `tppdm27.pd27_tur2` → `tppdm20.pd20_tur2`

**來自 fk_note (需驗證,1 筆)**:

- `tppdm25.pd25_tur2` — 原文:`**PK1**, FK to tppdm20.pd20_tur2`

### `wtorm00` — 訂位單主檔

**標準 FK (6 筆)**:

- `wtorm10.Wor10_wtordr` → `wtorm00.Wor00_wtordr`
- `wtorm10.Wor10_wtyear` → `wtorm00.Wor00_wtyear`
- `wtorm20.Wor20_wtordr` → `wtorm00.Wor00_wtordr`
- `wtorm20.Wor20_wtyear` → `wtorm00.Wor00_wtyear`
- `wtorm30.wor30_wtordr` → `wtorm00.Wor00_wtordr`
- `wtorm30.wor30_wtyear` → `wtorm00.Wor00_wtyear`

### `tptbm10` — 團體銷售資訊說明檔

**標準 FK (5 筆)**:

- `tptbm11.tb11_note` → `tptbm10`
- `tptbm11.tb11_country` → `tptbm10`
- `tptbm11.tb11_area` → `tptbm10`
- `tptbm11.tb11_darea` → `tptbm10`
- `tptbm11.tb11_seq` → `tptbm10`

### `tptbm20` — 前台旅遊地區代碼檔

**標準 FK (4 筆)**:

- `tppdm10.prod_webarea` → `tptbm20.tb20_webarea`
- `tptbm00.tbm0_webarea` → `tptbm20`
- `tptbm20_lang.tb20_lang_webarea` → `tptbm20`
- `tptrm22.tr22_webarea` → `tptbm20`

### `tptbm00` — 標準團名資料檔

**標準 FK (4 筆)**:

- `tptbm06.tbm6_code` → `tptbm00`
- `tptbm09.tbm9_name` → `tptbm00`
- `tptbm11.tb11_name` → `tptbm00`
- `tptrm32.tr32_name` → `tptbm00`

### `ssorm13` — 商務部旅客機票資料

**標準 FK (3 筆)**:

- `ssorm14.or14_ordr` → `ssorm13.or13_ordr`
- `ssorm14.or14_year` → `ssorm13.or13_year`
- `ssorm14.or14_seq` → `ssorm13.or13_seq`

### `istbm10` — 線別代碼檔

**標準 FK (3 筆)**:

- `tptbm00.tbm0_line` → `istbm10`
- `tptbm02.tbm2_line` → `istbm10`
- `tptbm15.tb15_line` → `istbm10`

### `tptrm20` — 旅遊館

**標準 FK (3 筆)**:

- `tptrm21.tr21_travel` → `tptrm20`
- `tptrm22.tr22_travel` → `tptrm20`
- `tptrm30.tr30_travel` → `tptrm20`

### `istbm83` — 公用標籤檔

**標準 FK (2 筆)**:

- `istbm83_lan.tb83lan_no` → `istbm83`
- `tptbm06.tbm6_no` → `istbm83`

### `tppcm40` — 檔次報價總表

**標準 FK (2 筆)**:

- `tppdm10.prod_tpform` → `tppcm40`
- `tppdm10.prod_size` → `tppcm40`

### `tppdm20_ez` — 易遊行程主檔

**標準 FK (1 筆)**:

- `tppdm21_ez.ez21_tur2` → `tppdm20_ez.ez20_tur2`

**來自 fk_note (需驗證,1 筆)**:

- `tppdm25_ez.ez25_tur2` — 原文:`**PK1**, FK to tppdm20_ez.ez20_tur2`

### `tppdm62` — 郵輪岸上觀光主檔

**標準 FK (2 筆)**:

- `tppdm64.pd64_localtour` → `tppdm62.pd62_localtour`
- `tppdm66.pd66_localtour` → `tppdm62.pd62_localtour`

### `tppdm64` — 郵輪岸上觀光車次

**標準 FK (2 筆)**:

- `tppdm66.pd66_date` → `tppdm64.pd64_date`
- `tppdm66.pd66_bus` → `tppdm64.pd64_bus`

### `isbum01` — bu事業體頻道

**標準 FK (2 筆)**:

- `tppdm92.pd92_chl` → `isbum01.bu01_channel`
- `tppdm93.pd93_chl` → `isbum01.bu01_channel`

### `tptrm30` — 旅遊館群組

**標準 FK (2 筆)**:

- `tptrm32.tr32_travel` → `tptrm30`
- `tptrm32.tr32_group` → `tptrm30`

### `bookm00` — 預訂主檔

**標準 FK (1 筆)**:

- `bookm01.bk01_bookno` → `bookm00.bk00_bookno`

### `tppdm98` — 團多房價群組檔

**標準 FK (1 筆)**:

- `tppdm90.pd90_pd98no` → `tppdm98`

---

## 三、零引用 table

以下 83 張 table 沒有被任何其他 table 的 FK 指向。
這**不代表可以刪除** — 通常是:
- 入口型主檔(如 tppdm10 本身是被引用,但它指向的上游是 tppcm 這類估價)
- 獨立模組(如標籤系統 istbm82/83)
- FK 尚未完整記錄

| Table | Database | 主要描述 |
|-------|----------|----------|
| `bookm01` | LionGroupERP | 預訂明細 |
| `bookm10` | LionGroupRPM | 團體訂單主檔 |
| `isbum02` | LionGroupERP | bu事業體頻道審核人員 |
| `isbum03` | LionGroupERP | bu事業體不分銷對象設定 |
| `iscpm00` | LionGroupRPM | 公司主檔 |
| `iscpm21` | LionGroupERP | 雄獅國家網站代碼 |
| `ispfm00` | LionGroupERP | 單位主檔 |
| `istbm11` | LionGroupERP | 各線審核毛利負責人名單 |
| `istbm12` | LionGroupERP | 各單位線別毛利率與日售價資料 |
| `istbm20` | LionGroupERP | 地區代碼檔 |
| `istbm82` | LionGroupERP | 公用標籤群組檔 |
| `istbm83_lan` | LionGroupERP | 公用標籤名稱語系檔 |
| `optbm18` | LionGroupERP | 城市區域檔 |
| `ssorm01` | LionGroupERP | 訂單副檔 |
| `ssorm02` | LionGroupERP | 訂單副檔 |
| `ssorm03` | LionGroupERP | 訂單帳款副檔 |
| `ssorm04` | LionGroupERP | 訂單副檔 |
| `ssorm05` | LionGroupERP | 各產品網單同意記錄檔 |
| `ssorm06` | LionGroupERP | 訂單保險資料副檔 |
| `ssorm07` | LionGroupERP | 訂單業務自檢項目 |
| `ssorm11` | LionGroupERP | 訂單明細副檔 |
| `ssorm12` | LionGroupERP | 訂單明細副檔 |
| `ssorm14` | LionGroupERP | 商務部旅客機票航段資料 |
| `tppcm09` | LionGroupERP | 估價幣別匯率檔 |
| `tppcm10` | LionGroupERP | 估價明細成本檔 |
| `tppcm20` | LionGroupERP | 估價明細檔 |
| `tppcm21` | LionGroupERP | 估價明細暫存計算檔 |
| `tppcm30` | LionGroupERP | 檔次估價成本主檔 |
| `tppcm41` | LionGroupERP | 檔次成本明細檔 |
| `tppcm50` | LionGroupERP | 估價單附件檔案管理表 |
| `tppdm11` | LionGroupERP | 出團行程檔 |
| `tppdm12` | LionGroupERP | 說明會副檔 |
| `tppdm13` | LionGroupERP | 團體說明資料檔 |
| `tppdm14` | LionGroupERP | 團體領隊建議核派名單檔 |
| `tppdm15` | LionGroupERP | 團體活動節目關聯檔 |
| `tppdm16` | LionGroupERP | 團體副檔 |
| `tppdm17` | LionGroupERP | 團體關連檔 |
| `tppdm18` | LionGroupERP | 團體預訂數量檔 |
| `tppdm19` | LionGroupERP | 團體滿意度調查統計檔 |
| `tppdm19a` | LionGroupERP | 團體滿意度調查統計副檔 |
| `tppdm21` | LionGroupERP | 日行程檔 |
| `tppdm21_ez` | LionGroupERP | 易遊團體日行程檔 |
| `tppdm22` | LionGroupERP | 自由行行程檔 |
| `tppdm23` | LionGroupERP | 行程自費活動關聯檔 |
| `tppdm24` | LionGroupERP | 團體日行程CTO資料檔 |
| `tppdm25` | LionGroupERP | 團體行程副檔 |
| `tppdm25_ez` | LionGroupERP | 易遊團體行程副檔 |
| `tppdm26` | LionGroupERP | 行程上下車地點關聯檔 |
| `tppdm27` | LionGroupERP | 團體行程修改自動留言檔 |
| `tppdm30` | LionGroupERP | 團體產品行程異動記錄檔 |
| `tppdm36` | LionGroupERP | 團體上下車地點關聯檔 |
| `tppdm40` | LionGroupERP | 團體班機資料 |
| `tppdm41` | LionGroupERP | 團體 PNR 資料 |
| `tppdm50` | LionGroupERP | 出團旅館檔 |
| `tppdm55` | LionGroupERP | 交付 B2P 供應商處理團 |
| `tppdm56` | LionGroupERP | 供應商詳細欄位設定檔 |
| `tppdm57` | LionGroupERP | 團詳細設定欄位 |
| `tppdm60` | LionGroupERP | 郵輪團說明會資料檔 |
| `tppdm61` | LionGroupERP | 郵輪接駁車 |
| `tppdm63` | LionGroupERP | 郵輪岸上觀光景點 |
| `tppdm65` | LionGroupERP | 郵輪岸上觀光車次團體 |
| `tppdm66` | LionGroupERP | 郵輪相關檔案 |
| `tppdm67` | LionGroupERP | 團體郵輪設定 |
| `tppdm76` | LionGroupERP | 團產品預設圖檔 |
| `tppdm81` | LionGroupERP | 設定滑雪團各級教練人數 |
| `tppdm90` | LionGroupERP | 團體售價資料檔 |
| `tppdm91` | LionGroupERP | 產品分銷設定 |
| `tppdm92` | LionGroupERP | 產品分銷上架設定 |
| `tppdm93` | LionGroupERP | 多渠道自動上架設定 |
| `tptbm02` | LionGroupERP | 標準團名關鍵字檔 |
| `tptbm06` | LionGroupERP | 標準團名標籤關聯檔 |
| `tptbm09` | LionGroupERP | 標準團名不發簡訊設定檔 |
| `tptbm11` | LionGroupERP | 標準團名對應銷售資訊檔 |
| `tptbm15` | LionGroupERP | 台灣說明會提醒文字 |
| `tptbm20_lang` | LionGroupERP | 前台旅遊地區代碼多語系檔 |
| `tptbm30` | LionGroupERP | 海外 FIT 票地區代碼檔 |
| `tptbm31` | LionGroupERP | 海外 FIT 票統計大類代碼檔 |
| `tptrm21` | LionGroupERP | 旅遊館常用證照項目 |
| `tptrm22` | LionGroupERP | 旅遊館對應旅遊地區代碼檔 |
| `tptrm32` | LionGroupERP | 旅遊館群組行程 |
| `wtorm10` | LionGroupERP | 訂位單旅客資料檔 |
| `wtorm20` | LionGroupERP | 訂位單航段檔 |
| `wtorm30` | LionGroupERP | 訂房記錄檔 |

---

## 四、指向 repo 外部的引用

以下 FK 目標**不在 schemas/ 中**。Copilot 看到這類 FK 時:
- **禁止** hallucinate 目標 table 的欄位
- **必須**告知使用者「此 FK 目標不在本 repo」
- 可建議使用者查詢對應的外部 skill(如 opagm* 可能在 LionGroupRPM 或其他 skill)

| External Target | 引用筆數 | 可能位置(推測) |
|-----------------|---------|-----------------|
| `tptbm` | 4 | tptbm* — 已在 repo,此欄位 FK 格式不完整 |
| `optbm20` | 4 | optbm* 系列 — 元件管理,需確認歸屬 |
| `optbm30` | 2 | optbm* 系列 — 元件管理,需確認歸屬 |
| `optnm00` | 2 | optnm* — 活動節目主檔 |
| `optbm11` | 2 | optbm* 系列 — 元件管理,需確認歸屬 |
| `opagm10` | 1 | opagm* 系列 — 可能在 LionGroupRPM 或獨立 repo |
| `iscpm11` | 1 | iscpm* — 公司主檔(部分已在 repo,部分外部) |
| `optbm70` | 1 | optbm* 系列 — 元件管理,需確認歸屬 |
| `customer` | 1 | 客戶主檔,歸屬未確認 |
| `opagm20` | 1 | opagm* 系列 — 可能在 LionGroupRPM 或獨立 repo |
| `PCM` | 1 |  |
| `B2P供應商主檔` | 1 | B2P 供應商系統 |
| `opvim00` | 1 | opvim* — 景點主檔(CTO 元件) |
| `tppdm72` | 1 | tppdm72 — 未在 repo,skill index 未記錄 |
| `DBA` | 1 | DBA 資料庫 — 可能是 erp2 相關 |
| `HTORM31` | 1 | 房產訂房明細 — skill 中存在,repo 未收錄 |
| `ophtm70` | 1 | ophtm* — 旅館主檔(CTO 元件) |

### 詳細引用來源

**`tptbm`** 被以下欄位引用:

- `tppdm20.pd20_line` — `tptbm`
- `tppdm20.pd20_dline` — `tptbm`
- `tppdm20.pd20_area` — `tptbm`
- `tppdm20.pd20_darea` — `tptbm`

**`optbm20`** 被以下欄位引用:

- `tppdm26.pd26_station` — `optbm20.tb20_station`
- `tppdm26.pd26_station1` — `optbm20.tb20_station`
- `tppdm36.pd36_station` — `optbm20.tb20_station`
- `tppdm36.pd36_station1` — `optbm20.tb20_station`

**`optbm30`** 被以下欄位引用:

- `bookm00.bk00_meatstyle` — `optbm30`
- `bookm01.bk01_meatstyle` — `optbm30`

**`optnm00`** 被以下欄位引用:

- `tppdm15.pd15_option` — `optnm00`
- `tppdm23.pd23_option` — `optnm00`

**`optbm11`** 被以下欄位引用:

- `tppdm40.pd40_fairport` — `optbm11`
- `tppdm40.pd40_tairport` — `optbm11`

**`opagm10`** 被以下欄位引用:

- `bookm00.bk00_local` — `opagm10`

**`iscpm11`** 被以下欄位引用:

- `bookm00.bk00_payfor` — `iscpm11`

**`optbm70`** 被以下欄位引用:

- `bookm00.bk00_bus_carr` — `optbm70`

**`customer`** 被以下欄位引用:

- `ssorm00.ordr_cust` — `customer`

**`opagm20`** 被以下欄位引用:

- `tppdm14.pd14_tl` — `opagm20`

**`PCM`** 被以下欄位引用:

- `tppdm20.pd20_tripidno` — `PCM.dbo`

**`B2P供應商主檔`** 被以下欄位引用:

- `tppdm55.pd55_local` — `B2P供應商主檔`

**`opvim00`** 被以下欄位引用:

- `tppdm63.pd63_view` — `opvim00`

**`tppdm72`** 被以下欄位引用:

- `tppdm67.pd67_rtno` — `tppdm72.pd72_rtno`

**`DBA`** 被以下欄位引用:

- `wtorm30.wor30_orderseq` — `DBA`

**`HTORM31`** 被以下欄位引用:

- `wtorm30.wor30_hor31descseq` — `HTORM31.HOR31_DESC`

**`ophtm70`** 被以下欄位引用:

- `wtorm30.wor30_discount` — `ophtm70`

---

## 五、Copilot 使用規則

讀本檔案時必須遵守:

1. **影響範圍查詢必回答具體清單**:當使用者問「改 X 會影響什麼」,必須從 §二 找出引用清單回答,禁止給出「可能會影響訂單相關 table」這種模糊答案。

2. **來自 fk_note 的引用需標示「待驗證」**:§二 中標為「fk_note (需驗證)」的引用,在回答時必須說明「此關聯來自非標準化 FK,建議使用前驗證」。

3. **外部引用必須禁止推測**:§四 列出的 table 不在 repo,看到這些 FK 不可 hallucinate 欄位。

4. **零引用 table 不等於無用**:§三 的清單不代表可刪除或忽略,它們可能是主檔型 table 或獨立模組。
