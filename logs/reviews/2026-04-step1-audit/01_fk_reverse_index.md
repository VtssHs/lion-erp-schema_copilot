# FK 反向索引
> 每張 table 被哪些 `{source_table}.{column}` 引用。
> 涵蓋標準 `fk:` 欄位與 `fk_note:` 中可自動辨識的 table 名稱。
> 自動產出 — 請勿手動編輯,有 inconsistency 請回頭修 YAML。

## 統計

- 總 table 數:106
- 有被引用的 table:23
- 零引用 table:83
- 指向 repo 外部的引用數(未收錄的 table):26
- fk_note 無法自動解析的筆數:28

---

## 一、被引用的 table(依被引用次數排序)

### `tppdm10` — 團體主檔

被 **25** 個欄位引用:

**標準 FK**:

- `bookm00.bk00_prod` → `.prod_prod`
- `ssorm00.ordr_prod` → `.prod_prod`
- `tppdm11.pd11_prod` → `.prod_prod`
- `tppdm12.pd12_prod` → `.prod_prod`
- `tppdm15.pd15_prod` → `.prod_prod`
- `tppdm16.pd16_prod` → `.prod_prod`
- `tppdm17.pd17_prod` → `.prod_prod`
- `tppdm17.pd17_chdprod` → `.prod_prod`
- `tppdm18.pd18_prod` → `.prod_prod`
- `tppdm19.pd19_prod` → `.prod_prod`
- `tppdm19a.p19a_prod` → `.prod_prod`
- `tppdm30.pd30_prod` → `.tpdm10_geno`
- `tppdm36.pd36_prod` → `.prod_prod`
- `tppdm41.pd41_prod` → `.prod_prod`
- `tppdm50.pd50_prod` → `.prod_prod`
- `tppdm55.pd55_prod` → `.prod_prod`
- `tppdm57.pd57_prod` → `.prod_prod`
- `tppdm60.pd60_prod` → `.prod_prod`
- `tppdm65.pd65_prod` → `.prod_prod`
- `tppdm67.pd67_prod` → `.prod_prod`
- `tppdm81.pd81_prod` → `.prod_prod`
- `tppdm90.pd90_prod` → `.prod_prod`
- `tppdm91.pd91_prod` → `.prod_prod`
- `tppdm92.pd92_prod` → `.prod_prod`
- `tppdm98.pd98_prod` → `.prod_prod`

### `istbm00` — 基礎代碼主檔

被 **23** 個欄位引用:

**標準 FK**:

- `tppdm10.prod_project`

**來自 fk_note(需人工驗證)**:

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

被 **19** 個欄位引用:

**標準 FK**:

- `ssorm01.or01_ordr` → `.ordr_ordr`
- `ssorm01.or01_year` → `.ordr_year`
- `ssorm02.or02_ordr` → `.ordr_ordr`
- `ssorm02.or02_year` → `.ordr_year`
- `ssorm03.or03_ordr` → `.ordr_ordr`
- `ssorm03.or03_year` → `.ordr_year`
- `ssorm04.or04_ordr` → `.ordr_ordr`
- `ssorm04.or04_year` → `.ordr_year`
- `ssorm05.or05_ordr` → `.ordr_ordr`
- `ssorm06.or06_ordr` → `.ordr_ordr`
- `ssorm06.or06_year` → `.ordr_year`
- `ssorm07.or07_ordr` → `.ordr_ordr`
- `ssorm07.or07_year` → `.ordr_year`
- `ssorm10.orer_ordr` → `.ordr_ordr`
- `ssorm10.orer_year` → `.ordr_year`
- `ssorm12.or12_ordr` → `.ordr_ordr`
- `ssorm12.or12_year` → `.ordr_year`
- `tppdm66.pd66_ordr` → `.ordr_ordr`
- `tppdm66.pd66_year` → `.ordr_year`

### `tppcm00` — 團體產品估價主檔

被 **8** 個欄位引用:

**來自 fk_note(需人工驗證)**:

- `tppcm09.tp09_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm10.tp10_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm20.tp20_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm21.tp21_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm30.tp30_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm40.tp40_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm41.tp41_tpform` — 原文:`FK → `tppcm00.tp00_tpform``
- `tppcm50.tp50_tpform` — 原文:`FK → `tppcm00.tp00_tpform``

### `isbum00` — Bu 事業體主檔

被 **7** 個欄位引用:

**標準 FK**:

- `ispfm00.prof_bu`
- `tppdm91.pd91_bu` → `.bu00_bu`
- `tppdm92.pd92_bu` → `.bu00_bu`
- `tppdm93.pd93_chlbu` → `.bu00_bu`
- `tppdm93.pd93_prodbu` → `.bu00_bu`
- `tptbm20.tb20_bu`
- `wtorm00.wor00_bu`

### `ssorm10` — 訂單明細檔

被 **7** 個欄位引用:

**標準 FK**:

- `ssorm11.or11_ordr` → `.orer_ordr`
- `ssorm11.or11_year` → `.orer_year`
- `ssorm11.or11_seq` → `.orer_seq`
- `ssorm12.or12_seq` → `.orer_seq`
- `ssorm13.or13_ordr` → `.orer_ordr`
- `ssorm13.or13_year` → `.orer_year`
- `tppdm66.pd66_seq` → `.orer_seq`

### `tppdm20` — 團體行程代號主檔

被 **7** 個欄位引用:

**標準 FK**:

- `tppdm21.pd21_tur2` → `.pd20_tur2`
- `tppdm22.pd22_tur2` → `.pd20_tur2`
- `tppdm23.pd23_tur2` → `.pd20_tur2`
- `tppdm24.pd24_tur2` → `.pd20_tur2`
- `tppdm26.pd26_tur2` → `.pd20_tur2`
- `tppdm27.pd27_tur2` → `.pd20_tur2`

**來自 fk_note(需人工驗證)**:

- `tppdm25.pd25_tur2` — 原文:`**PK1**, FK to tppdm20.pd20_tur2`

### `wtorm00` — 訂位單主檔

被 **6** 個欄位引用:

**標準 FK**:

- `wtorm10.Wor10_wtordr` → `.Wor00_wtordr`
- `wtorm10.Wor10_wtyear` → `.Wor00_wtyear`
- `wtorm20.Wor20_wtordr` → `.Wor00_wtordr`
- `wtorm20.Wor20_wtyear` → `.Wor00_wtyear`
- `wtorm30.wor30_wtordr` → `.Wor00_wtordr`
- `wtorm30.wor30_wtyear` → `.Wor00_wtyear`

### `tptbm10` — 團體銷售資訊說明檔

被 **5** 個欄位引用:

**標準 FK**:

- `tptbm11.tb11_note`
- `tptbm11.tb11_country`
- `tptbm11.tb11_area`
- `tptbm11.tb11_darea`
- `tptbm11.tb11_seq`

### `tptbm20` — 前台旅遊地區代碼檔

被 **4** 個欄位引用:

**標準 FK**:

- `tppdm10.prod_webarea` → `.tb20_webarea`
- `tptbm00.tbm0_webarea`
- `tptbm20_lang.tb20_lang_webarea`
- `tptrm22.tr22_webarea`

### `tptbm00` — 標準團名資料檔

被 **4** 個欄位引用:

**標準 FK**:

- `tptbm06.tbm6_code`
- `tptbm09.tbm9_name`
- `tptbm11.tb11_name`
- `tptrm32.tr32_name`

### `ssorm13` — 商務部旅客機票資料

被 **3** 個欄位引用:

**標準 FK**:

- `ssorm14.or14_ordr` → `.or13_ordr`
- `ssorm14.or14_year` → `.or13_year`
- `ssorm14.or14_seq` → `.or13_seq`

### `istbm10` — 線別代碼檔

被 **3** 個欄位引用:

**標準 FK**:

- `tptbm00.tbm0_line`
- `tptbm02.tbm2_line`
- `tptbm15.tb15_line`

### `tptrm20` — 旅遊館

被 **3** 個欄位引用:

**標準 FK**:

- `tptrm21.tr21_travel`
- `tptrm22.tr22_travel`
- `tptrm30.tr30_travel`

### `istbm83` — 公用標籤檔

被 **2** 個欄位引用:

**標準 FK**:

- `istbm83_lan.tb83lan_no`
- `tptbm06.tbm6_no`

### `tppcm40` — 檔次報價總表

被 **2** 個欄位引用:

**標準 FK**:

- `tppdm10.prod_tpform`
- `tppdm10.prod_size`

### `tppdm20_ez` — 易遊行程主檔

被 **2** 個欄位引用:

**標準 FK**:

- `tppdm21_ez.ez21_tur2` → `.ez20_tur2`

**來自 fk_note(需人工驗證)**:

- `tppdm25_ez.ez25_tur2` — 原文:`**PK1**, FK to tppdm20_ez.ez20_tur2`

### `tppdm62` — 郵輪岸上觀光主檔

被 **2** 個欄位引用:

**標準 FK**:

- `tppdm64.pd64_localtour` → `.pd62_localtour`
- `tppdm66.pd66_localtour` → `.pd62_localtour`

### `tppdm64` — 郵輪岸上觀光車次

被 **2** 個欄位引用:

**標準 FK**:

- `tppdm66.pd66_date` → `.pd64_date`
- `tppdm66.pd66_bus` → `.pd64_bus`

### `isbum01` — bu事業體頻道

被 **2** 個欄位引用:

**標準 FK**:

- `tppdm92.pd92_chl` → `.bu01_channel`
- `tppdm93.pd93_chl` → `.bu01_channel`

### `tptrm30` — 旅遊館群組

被 **2** 個欄位引用:

**標準 FK**:

- `tptrm32.tr32_travel`
- `tptrm32.tr32_group`

### `bookm00` — 預訂主檔

被 **1** 個欄位引用:

**標準 FK**:

- `bookm01.bk01_bookno` → `.bk00_bookno`

### `tppdm98` — 團多房價群組檔

被 **1** 個欄位引用:

**標準 FK**:

- `tppdm90.pd90_pd98no`

---

## 二、指向 repo 外部(schemas 未收錄的 table)

以下欄位的 FK 目標不在本 repo 的 schemas/ 中。
可能是 (a) 需要補進 repo、(b) 屬於其他 repo(LionGroupRPM/CMS)、(c) FK 欄位填錯。

### `tptbm` (被 4 個欄位引用)

- `tppdm20.pd20_line` — `tptbm`
- `tppdm20.pd20_dline` — `tptbm`
- `tppdm20.pd20_area` — `tptbm`
- `tppdm20.pd20_darea` — `tptbm`

### `optbm20` (被 4 個欄位引用)

- `tppdm26.pd26_station` — `optbm20.tb20_station`
- `tppdm26.pd26_station1` — `optbm20.tb20_station`
- `tppdm36.pd36_station` — `optbm20.tb20_station`
- `tppdm36.pd36_station1` — `optbm20.tb20_station`

### `optbm30` (被 2 個欄位引用)

- `bookm00.bk00_meatstyle` — `optbm30`
- `bookm01.bk01_meatstyle` — `optbm30`

### `optnm00` (被 2 個欄位引用)

- `tppdm15.pd15_option` — `optnm00`
- `tppdm23.pd23_option` — `optnm00`

### `optbm11` (被 2 個欄位引用)

- `tppdm40.pd40_fairport` — `optbm11`
- `tppdm40.pd40_tairport` — `optbm11`

### `opagm10` (被 1 個欄位引用)

- `bookm00.bk00_local` — `opagm10`

### `iscpm11` (被 1 個欄位引用)

- `bookm00.bk00_payfor` — `iscpm11`

### `optbm70` (被 1 個欄位引用)

- `bookm00.bk00_bus_carr` — `optbm70`

### `customer` (被 1 個欄位引用)

- `ssorm00.ordr_cust` — `customer`

### `opagm20` (被 1 個欄位引用)

- `tppdm14.pd14_tl` — `opagm20`

### `PCM` (被 1 個欄位引用)

- `tppdm20.pd20_tripidno` — `PCM.dbo`

### `B2P供應商主檔` (被 1 個欄位引用)

- `tppdm55.pd55_local` — `B2P供應商主檔`

### `opvim00` (被 1 個欄位引用)

- `tppdm63.pd63_view` — `opvim00`

### `tppdm72` (被 1 個欄位引用)

- `tppdm67.pd67_rtno` — `tppdm72.pd72_rtno`

### `DBA` (被 1 個欄位引用)

- `wtorm30.wor30_orderseq` — `DBA`

### `HTORM31` (被 1 個欄位引用)

- `wtorm30.wor30_hor31descseq` — `HTORM31.HOR31_DESC`

### `ophtm70` (被 1 個欄位引用)

- `wtorm30.wor30_discount` — `ophtm70`

---

## 三、無法自動解析的 fk_note

以下 `fk_note` 無法機械辨識出 table 名稱,需人工分類。
(與產出 2「fk_note 分類」會重疊,僅先列出以供交叉對照)

- `bookm00.bk00_ctokey` — 原文:`FK → 各類別主檔 (ophtm/opmtm/opbsm/opvim/opspm)`
- `istbm83.tb83_groupno` — 原文:`FK`
- `ssorm00.ordr_sales` — 原文:`FK → opagm20 (員工主檔)`
- `ssorm00.ordr_agent` — 原文:`FK → opagm00 (法人資料主檔)`
- `ssorm07.or07_code` — 原文:`FK → istbm81 (CHECKLIST)`
- `tppdm16.pd16_vscountry1` — 原文:`FK → 國家代碼表`
- `tppdm16.pd16_vsseq1` — 原文:`FK → 簽證類型表`
- `tppdm16.pd16_vscountry2` — 原文:`FK → 國家代碼表`
- `tppdm16.pd16_vsseq2` — 原文:`FK → 簽證類型表`
- `tppdm16.pd16_safecode` — 原文:`FK → 保險承辦單位代碼表`
- `tppdm16.pd16_safemode` — 原文:`FK → 交通工具代碼表`
- `tppdm16.pd16_SafeInsComp` — 原文:`FK → 保險公司代碼表`
- `tppdm16.pd16_demandcode` — 原文:`FK → istbm81 (DEMANDLIST)`
- `tppdm20.pd20_prodname` — 原文:`FK → 標準團名檔，有值時行程名稱=NULL`
- `tppdm21.pd21_ctokey` — 原文:`FK → Ctom85 (VIEW)`
- `tppdm24.pd24_ctokey` — 原文:`FK → 對應的主檔（景點/餐廳/旅館/商店）`
- `tppdm50.pd50_hotel` — 原文:`FK → 旅館主檔 (ophtm*)`
- `tppdm55.pd55_bkstfn` — 原文:`只存第一次設定者，FK → 員工主檔`
- `tppdm56.pd56_local` — 原文:`**PK1**, FK → 供應商主檔，配合 B2P 系統型態`
- `tppdm56.pd56_code` — 原文:`FK → 欄位代碼主檔`
- `tppdm57.pd57_local` — 原文:`**PK2**, FK → 供應商主檔`
- `tppdm57.pd57_coltype` — 原文:`**PK3**, FK → 欄位代碼主檔`
- `tppdm76.pd76_line` — 原文:`FK → 線別代碼表，例如：歐洲線、美洲線`
- `tppdm76.pd76_dline` — 原文:`FK → 副線別代碼表，細分線別`
- `tppdm76.pd76_area` — 原文:`FK → 地區代碼表，例如：西歐、東歐`
- `tppdm76.pd76_darea` — 原文:`FK → 細地區代碼表，更細緻的地區分類`
- `tppdm98.pd98_hotel` — 原文:`FK → 旅館主檔，該方案主要使用的旅館`
- `tppdm98.pd98_mstfn` — 原文:`FK → 員工主檔`

---

## 四、零引用 table

以下 83 張 table 沒有被任何其他 table 的 FK 指向。
這**不一定是問題** — 主檔通常入口型(沒有上游),或 FK 記錄不完整。

- `bookm01` — 預訂明細 [LionGroupERP]
- `bookm10` — 團體訂單主檔 [LionGroupRPM]
- `isbum02` — bu事業體頻道審核人員 [LionGroupERP]
- `isbum03` — bu事業體不分銷對象設定 [LionGroupERP]
- `iscpm00` — 公司主檔 [LionGroupRPM]
- `iscpm21` — 雄獅國家網站代碼 [LionGroupERP]
- `ispfm00` — 單位主檔 [LionGroupERP]
- `istbm11` — 各線審核毛利負責人名單 [LionGroupERP]
- `istbm12` — 各單位線別毛利率與日售價資料 [LionGroupERP]
- `istbm20` — 地區代碼檔 [LionGroupERP]
- `istbm82` — 公用標籤群組檔 [LionGroupERP]
- `istbm83_lan` — 公用標籤名稱語系檔 [LionGroupERP]
- `optbm18` — 城市區域檔 [LionGroupERP]
- `ssorm01` — 訂單副檔 [LionGroupERP]
- `ssorm02` — 訂單副檔 [LionGroupERP]
- `ssorm03` — 訂單帳款副檔 [LionGroupERP]
- `ssorm04` — 訂單副檔 [LionGroupERP]
- `ssorm05` — 各產品網單同意記錄檔 [LionGroupERP]
- `ssorm06` — 訂單保險資料副檔 [LionGroupERP]
- `ssorm07` — 訂單業務自檢項目 [LionGroupERP]
- `ssorm11` — 訂單明細副檔 [LionGroupERP]
- `ssorm12` — 訂單明細副檔 [LionGroupERP]
- `ssorm14` — 商務部旅客機票航段資料 [LionGroupERP]
- `tppcm09` — 估價幣別匯率檔 [LionGroupERP]
- `tppcm10` — 估價明細成本檔 [LionGroupERP]
- `tppcm20` — 估價明細檔 [LionGroupERP]
- `tppcm21` — 估價明細暫存計算檔 [LionGroupERP]
- `tppcm30` — 檔次估價成本主檔 [LionGroupERP]
- `tppcm41` — 檔次成本明細檔 [LionGroupERP]
- `tppcm50` — 估價單附件檔案管理表 [LionGroupERP]
- `tppdm11` — 出團行程檔 [LionGroupERP]
- `tppdm12` — 說明會副檔 [LionGroupERP]
- `tppdm13` — 團體說明資料檔 [LionGroupERP]
- `tppdm14` — 團體領隊建議核派名單檔 [LionGroupERP]
- `tppdm15` — 團體活動節目關聯檔 [LionGroupERP]
- `tppdm16` — 團體副檔 [LionGroupERP]
- `tppdm17` — 團體關連檔 [LionGroupERP]
- `tppdm18` — 團體預訂數量檔 [LionGroupERP]
- `tppdm19` — 團體滿意度調查統計檔 [LionGroupERP]
- `tppdm19a` — 團體滿意度調查統計副檔 [LionGroupERP]
- `tppdm21` — 日行程檔 [LionGroupERP]
- `tppdm21_ez` — 易遊團體日行程檔 [LionGroupERP]
- `tppdm22` — 自由行行程檔 [LionGroupERP]
- `tppdm23` — 行程自費活動關聯檔 [LionGroupERP]
- `tppdm24` — 團體日行程CTO資料檔 [LionGroupERP]
- `tppdm25` — 團體行程副檔 [LionGroupERP]
- `tppdm25_ez` — 易遊團體行程副檔 [LionGroupERP]
- `tppdm26` — 行程上下車地點關聯檔 [LionGroupERP]
- `tppdm27` — 團體行程修改自動留言檔 [LionGroupERP]
- `tppdm30` — 團體產品行程異動記錄檔 [LionGroupERP]
- `tppdm36` — 團體上下車地點關聯檔 [LionGroupERP]
- `tppdm40` — 團體班機資料 [LionGroupERP]
- `tppdm41` — 團體 PNR 資料 [LionGroupERP]
- `tppdm50` — 出團旅館檔 [LionGroupERP]
- `tppdm55` — 交付 B2P 供應商處理團 [LionGroupERP]
- `tppdm56` — 供應商詳細欄位設定檔 [LionGroupERP]
- `tppdm57` — 團詳細設定欄位 [LionGroupERP]
- `tppdm60` — 郵輪團說明會資料檔 [LionGroupERP]
- `tppdm61` — 郵輪接駁車 [LionGroupERP]
- `tppdm63` — 郵輪岸上觀光景點 [LionGroupERP]
- `tppdm65` — 郵輪岸上觀光車次團體 [LionGroupERP]
- `tppdm66` — 郵輪相關檔案 [LionGroupERP]
- `tppdm67` — 團體郵輪設定 [LionGroupERP]
- `tppdm76` — 團產品預設圖檔 [LionGroupERP]
- `tppdm81` — 設定滑雪團各級教練人數 [LionGroupERP]
- `tppdm90` — 團體售價資料檔 [LionGroupERP]
- `tppdm91` — 產品分銷設定 [LionGroupERP]
- `tppdm92` — 產品分銷上架設定 [LionGroupERP]
- `tppdm93` — 多渠道自動上架設定 [LionGroupERP]
- `tptbm02` — 標準團名關鍵字檔 [LionGroupERP]
- `tptbm06` — 標準團名標籤關聯檔 [LionGroupERP]
- `tptbm09` — 標準團名不發簡訊設定檔 [LionGroupERP]
- `tptbm11` — 標準團名對應銷售資訊檔 [LionGroupERP]
- `tptbm15` — 台灣說明會提醒文字 [LionGroupERP]
- `tptbm20_lang` — 前台旅遊地區代碼多語系檔 [LionGroupERP]
- `tptbm30` — 海外 FIT 票地區代碼檔 [LionGroupERP]
- `tptbm31` — 海外 FIT 票統計大類代碼檔 [LionGroupERP]
- `tptrm21` — 旅遊館常用證照項目 [LionGroupERP]
- `tptrm22` — 旅遊館對應旅遊地區代碼檔 [LionGroupERP]
- `tptrm32` — 旅遊館群組行程 [LionGroupERP]
- `wtorm10` — 訂位單旅客資料檔 [LionGroupERP]
- `wtorm20` — 訂位單航段檔 [LionGroupERP]
- `wtorm30` — 訂房記錄檔 [LionGroupERP]

