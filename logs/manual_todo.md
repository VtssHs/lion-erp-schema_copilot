# 人工待補清單

此清單由 `scripts/gen_todo.py` 自動產生。

## 待補 aliases（0 張）

**這是 Copilot 檢索品質的命脈。** 每張 table 補 2-3 個中文別名到 YAML 的 `aliases:` 欄位。


## 無 module 需補（27 張）

原始 md 未標註模組，請補上 `module:` 欄位。

- [ ] isbum01
- [ ] isbum02
- [ ] isbum03
- [ ] iscpm21
- [ ] ispfm00
- [ ] istbm10
- [ ] istbm11
- [ ] istbm12
- [ ] istbm20
- [ ] istbm82
- [ ] istbm83
- [ ] istbm83_lan
- [ ] tppdm20
- [ ] tppdm30
- [ ] tptbm00
- [ ] tptbm02
- [ ] tptbm06
- [ ] tptbm09
- [ ] tptbm11
- [ ] tptbm15
- [ ] tptbm20
- [ ] tptbm20_lang
- [ ] tptrm20
- [ ] tptrm21
- [ ] tptrm22
- [ ] tptrm30
- [ ] tptrm32

## 無 PK 標記需確認（15 張）

這些 table 的欄位都沒標 PK，可能是：(a) 原始 md 遺漏、(b) 真的沒有單一 PK、(c) 複合 PK 但未標註。

- [ ] bookm01
- [ ] tppcm09
- [ ] tppcm10
- [ ] tppcm20
- [ ] tppcm40
- [ ] tppcm41
- [ ] tppcm50
- [ ] tppdm12
- [ ] tppdm20
- [ ] tppdm27
- [ ] tppdm30
- [ ] tppdm61
- [ ] tppdm63
- [ ] tppdm90
- [ ] tptbm09

## type 全為 unknown（9 張）

這些 table 的原始 md 用了「欄位名稱 | 中文名稱 | 資料說明 | 備註」模板，根本沒有型別欄位。需要從 DB 或其他文件補型別。

- [ ] tppcm00
- [ ] tppcm09
- [ ] tppcm10
- [ ] tppcm20
- [ ] tppcm21
- [ ] tppcm30
- [ ] tppcm40
- [ ] tppcm41
- [ ] tppcm50

## 有 fk_note 需人工標準化（36 張 table）

這些 FK 格式無法自動標準化，通常是多型 FK 或條件 FK（例如 `istbm00 (ATTR)`）。可考慮保留 `fk_note` 或轉成結構化 `fk` + `fk_condition`。

### bookm00
- `bk00_ctokey`: `FK → 各類別主檔 (ophtm/opmtm/opbsm/opvim/opspm)`

### istbm83
- `tb83_groupno`: `FK`

### ssorm00
- `ordr_sales`: `FK → opagm20 (員工主檔)`
- `ordr_agent`: `FK → opagm00 (法人資料主檔)`

### ssorm02
- `or02_crs`: `FK → Istbm00 (CRSKIND)`

### ssorm07
- `or07_code`: `FK → istbm81 (CHECKLIST)`

### ssorm10
- `orer_tairline`: `FK → Istbm00 (TAIRLINE)`

### ssorm11
- `or11_urgent_relman`: `FK → Istbm00 (RELMAN)`
- `or11_meat`: `FK → Istbm00 (MEAT)`

### tppcm09
- `tp09_tpform`: `FK → `tppcm00.tp00_tpform``

### tppcm10
- `tp10_tpform`: `FK → `tppcm00.tp00_tpform``

### tppcm20
- `tp20_tpform`: `FK → `tppcm00.tp00_tpform``

### tppcm21
- `tp21_tpform`: `FK → `tppcm00.tp00_tpform``

### tppcm30
- `tp30_tpform`: `FK → `tppcm00.tp00_tpform``

### tppcm40
- `tp40_tpform`: `FK → `tppcm00.tp00_tpform``

### tppcm41
- `tp41_tpform`: `FK → `tppcm00.tp00_tpform``

### tppcm50
- `tp50_tpform`: `FK → `tppcm00.tp00_tpform``

### tppdm10
- `prod_form`: `FK → Istbm00 (FORM)`

### tppdm12
- `pd12_meetplace`: `FK → Istbm00 (MEET)`

### tppdm16
- `pd16_vscountry1`: `FK → 國家代碼表`
- `pd16_vsseq1`: `FK → 簽證類型表`
- `pd16_vscountry2`: `FK → 國家代碼表`
- `pd16_vsseq2`: `FK → 簽證類型表`
- `pd16_safecode`: `FK → 保險承辦單位代碼表`
- `pd16_safemode`: `FK → 交通工具代碼表`
- `pd16_SafeInsComp`: `FK → 保險公司代碼表`
- `pd16_demandcode`: `FK → istbm81 (DEMANDLIST)`

### tppdm19a
- `p19a_type`: `FK → ISTBM00 (TPPD19_代碼)`

### tppdm20
- `pd20_prodname`: `FK → 標準團名檔，有值時行程名稱=NULL`

### tppdm21
- `pd21_ctokey`: `FK → Ctom85 (VIEW)`

### tppdm24
- `pd24_ctokey`: `FK → 對應的主檔（景點/餐廳/旅館/商店）`

### tppdm25
- `pd25_tur2`: `**PK1**, FK to tppdm20.pd20_tur2`

### tppdm25_ez
- `ez25_tur2`: `**PK1**, FK to tppdm20_ez.ez20_tur2`

### tppdm50
- `pd50_hotel`: `FK → 旅館主檔 (ophtm*)`

### tppdm55
- `pd55_bkstfn`: `只存第一次設定者，FK → 員工主檔`

### tppdm56
- `pd56_local`: `**PK1**, FK → 供應商主檔，配合 B2P 系統型態`
- `pd56_code`: `FK → 欄位代碼主檔`

### tppdm57
- `pd57_local`: `**PK2**, FK → 供應商主檔`
- `pd57_coltype`: `**PK3**, FK → 欄位代碼主檔`

### tppdm76
- `pd76_line`: `FK → 線別代碼表，例如：歐洲線、美洲線`
- `pd76_dline`: `FK → 副線別代碼表，細分線別`
- `pd76_area`: `FK → 地區代碼表，例如：西歐、東歐`
- `pd76_darea`: `FK → 細地區代碼表，更細緻的地區分類`

### tppdm98
- `pd98_hotel`: `FK → 旅館主檔，該方案主要使用的旅館`
- `pd98_mstfn`: `FK → 員工主檔`

### tptbm00
- `tbm0_attr1`: `FK → istbm00 (ATTR)`
- `tbm0_attr2`: `FK → istbm00 (ATTR)`
- `tbm0_attr3`: `FK → istbm00 (ATTR)`
- `tbm0_psubject1`: `FK → istbm00 (PSUBJECT)`
- `tbm0_psubject2`: `FK → istbm00 (PSUBJECT)`
- `tbm0_psubject3`: `FK → istbm00 (PSUBJECT)`

### tptbm10
- `note_note`: `FK → Istbm00 (NOTE)`

### tptrm20
- `tr20_freekind`: `FK → istbm00 (FREEKIND)`

### tptrm32
- `tr32_pdhot`: `FK → istbm00 (PDHOT)`

### wtorm00
- `Wor00_ordrin1`: `FK → Istbm00 (ORDRIN1)`
- `Wor00_ordrin2`: `FK → Istbm00 (ORDRIN2)`
- `Wor00_crs`: `FK → Istbm00 (CRSKIND)`
- `wor00_cxldesc`: `FK → istbm00 (CXLDESC)`
- `wor00_cxldesc2`: `FK → istbm00 (CXLDESC2)`

### wtorm10
- `wor10_tkperiod`: `FK → Istbm00 (TKPERIOD)`
