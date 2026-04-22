# fk_note 分類清單

> 把 36 張 table 的 60 個 `fk_note` 依性質分成 5 類,給出機械化建議。
> A 類可直接改腳本自動轉換;B/C 類需設計新 schema 欄位;E 類需人工介入。

## 分類定義

| 代號 | 類別 | 處理方式 |
|------|------|----------|
| **A** | 標準 FK 但未標準化 | 可機械轉成 `fk:` 欄位 |
| **B** | 多型 FK(條件 FK) | 需新增 `fk:` + `fk_condition:` 結構 |
| **C** | 指向外部 table | 保留 `fk_note`,加 `external: true` 標記 |
| **D** | 偽 FK(其實是註解) | 刪除 `fk_note`,併入 `description` |
| **E** | 無法自動分類 | 需人工判讀 |

## 統計

- **A. 可機械轉換**: 14 筆(23.3%)
- **B. 多型 FK**: 18 筆(30.0%)
- **C. 外部 table**: 22 筆(36.7%)
- **D. 偽 FK**: 0 筆(0.0%)
- **E. 無法分類**: 6 筆(10.0%)

**總計**: 60 筆 fk_note

---

## A. 可機械轉換(修一個 script 一次解決)

以下 `fk_note` 可改寫為標準 `fk:`。可以寫一個一次性腳本批次修 YAML。

| Table | Column | 建議改寫為 | 原文 `fk_note` |
|-------|--------|-----------|----------------|
| `tppcm09` | `tp09_tpform` | `fk: tppcm00.tp00_tpform` | `FK → `tppcm00.tp00_tpform`` |
| `tppcm10` | `tp10_tpform` | `fk: tppcm00.tp00_tpform` | `FK → `tppcm00.tp00_tpform`` |
| `tppcm20` | `tp20_tpform` | `fk: tppcm00.tp00_tpform` | `FK → `tppcm00.tp00_tpform`` |
| `tppcm21` | `tp21_tpform` | `fk: tppcm00.tp00_tpform` | `FK → `tppcm00.tp00_tpform`` |
| `tppcm30` | `tp30_tpform` | `fk: tppcm00.tp00_tpform` | `FK → `tppcm00.tp00_tpform`` |
| `tppcm40` | `tp40_tpform` | `fk: tppcm00.tp00_tpform` | `FK → `tppcm00.tp00_tpform`` |
| `tppcm41` | `tp41_tpform` | `fk: tppcm00.tp00_tpform` | `FK → `tppcm00.tp00_tpform`` |
| `tppcm50` | `tp50_tpform` | `fk: tppcm00.tp00_tpform` | `FK → `tppcm00.tp00_tpform`` |
| `tppdm19a` | `p19a_type` | `fk: ISTBM00` | `FK → ISTBM00 (TPPD19_代碼)` |
| `tppdm25` | `pd25_tur2` | `fk: tppdm20.pd20_tur2` | `**PK1**, FK to tppdm20.pd20_tur2` |
| `tppdm25_ez` | `ez25_tur2` | `fk: tppdm20_ez.ez20_tur2` | `**PK1**, FK to tppdm20_ez.ez20_tur2` |
| `wtorm00` | `Wor00_ordrin1` | `fk: Istbm00` | `FK → Istbm00 (ORDRIN1)` |
| `wtorm00` | `Wor00_ordrin2` | `fk: Istbm00` | `FK → Istbm00 (ORDRIN2)` |
| `wtorm00` | `wor00_cxldesc2` | `fk: istbm00` | `FK → istbm00 (CXLDESC2)` |

## B. 多型 FK(需設計新 schema 欄位)

這類 FK 的目標 table 是一樣的(通常是 `istbm00`),但由某個條件欄位區分。
建議在 YAML schema 新增 `fk_condition` 支援,例如:

```yaml
fk: istbm00
fk_condition:
  column: __tabl_type__
  value: ATTR   # 對應該欄位應查的代碼類別
```

| Table | Column | 代碼類別(istbm00.__tabl_type__) | 原文 |
|-------|--------|--------------------------------|------|
| `ssorm02` | `or02_crs` | `CRSKIND` | `FK → Istbm00 (CRSKIND)` |
| `ssorm10` | `orer_tairline` | `TAIRLINE` | `FK → Istbm00 (TAIRLINE)` |
| `ssorm11` | `or11_meat` | `MEAT` | `FK → Istbm00 (MEAT)` |
| `ssorm11` | `or11_urgent_relman` | `RELMAN` | `FK → Istbm00 (RELMAN)` |
| `tppdm10` | `prod_form` | `FORM` | `FK → Istbm00 (FORM)` |
| `tppdm12` | `pd12_meetplace` | `MEET` | `FK → Istbm00 (MEET)` |
| `tptbm00` | `tbm0_attr1` | `ATTR` | `FK → istbm00 (ATTR)` |
| `tptbm00` | `tbm0_attr2` | `ATTR` | `FK → istbm00 (ATTR)` |
| `tptbm00` | `tbm0_attr3` | `ATTR` | `FK → istbm00 (ATTR)` |
| `tptbm00` | `tbm0_psubject1` | `PSUBJECT` | `FK → istbm00 (PSUBJECT)` |
| `tptbm00` | `tbm0_psubject2` | `PSUBJECT` | `FK → istbm00 (PSUBJECT)` |
| `tptbm00` | `tbm0_psubject3` | `PSUBJECT` | `FK → istbm00 (PSUBJECT)` |
| `tptbm10` | `note_note` | `NOTE` | `FK → Istbm00 (NOTE)` |
| `tptrm20` | `tr20_freekind` | `FREEKIND` | `FK → istbm00 (FREEKIND)` |
| `tptrm32` | `tr32_pdhot` | `PDHOT` | `FK → istbm00 (PDHOT)` |
| `wtorm00` | `Wor00_crs` | `CRSKIND` | `FK → Istbm00 (CRSKIND)` |
| `wtorm00` | `wor00_cxldesc` | `CXLDESC` | `FK → istbm00 (CXLDESC)` |
| `wtorm10` | `wor10_tkperiod` | `TKPERIOD` | `FK → Istbm00 (TKPERIOD)` |

## C. 指向外部 table(本 repo 未收錄)

以下 FK 目標不在 schemas/,通常是 opagm*、opnm* 等未納入本 repo 的 table。
建議 YAML 新增 `external: true` 標記,Copilot 就知道這不是本 repo 的 table,不會 hallucinate。

| Table | Column | 外部目標 | 原文 |
|-------|--------|----------|------|
| `bookm00` | `bk00_ctokey` | `None` | `FK → 各類別主檔 (ophtm/opmtm/opbsm/opvim/opspm)` |
| `tppdm16` | `pd16_SafeInsComp` | `None` | `FK → 保險公司代碼表` |
| `tppdm16` | `pd16_safecode` | `None` | `FK → 保險承辦單位代碼表` |
| `tppdm16` | `pd16_safemode` | `None` | `FK → 交通工具代碼表` |
| `tppdm16` | `pd16_vscountry1` | `None` | `FK → 國家代碼表` |
| `tppdm16` | `pd16_vscountry2` | `None` | `FK → 國家代碼表` |
| `tppdm16` | `pd16_vsseq1` | `None` | `FK → 簽證類型表` |
| `tppdm16` | `pd16_vsseq2` | `None` | `FK → 簽證類型表` |
| `tppdm20` | `pd20_prodname` | `None` | `FK → 標準團名檔，有值時行程名稱=NULL` |
| `tppdm24` | `pd24_ctokey` | `None` | `FK → 對應的主檔（景點/餐廳/旅館/商店）` |
| `tppdm50` | `pd50_hotel` | `None` | `FK → 旅館主檔 (ophtm*)` |
| `tppdm55` | `pd55_bkstfn` | `None` | `只存第一次設定者，FK → 員工主檔` |
| `tppdm56` | `pd56_code` | `None` | `FK → 欄位代碼主檔` |
| `tppdm56` | `pd56_local` | `None` | `**PK1**, FK → 供應商主檔，配合 B2P 系統型態` |
| `tppdm57` | `pd57_coltype` | `None` | `**PK3**, FK → 欄位代碼主檔` |
| `tppdm57` | `pd57_local` | `None` | `**PK2**, FK → 供應商主檔` |
| `tppdm76` | `pd76_area` | `None` | `FK → 地區代碼表，例如：西歐、東歐` |
| `tppdm76` | `pd76_darea` | `None` | `FK → 細地區代碼表，更細緻的地區分類` |
| `tppdm76` | `pd76_dline` | `None` | `FK → 副線別代碼表，細分線別` |
| `tppdm76` | `pd76_line` | `None` | `FK → 線別代碼表，例如：歐洲線、美洲線` |
| `tppdm98` | `pd98_hotel` | `None` | `FK → 旅館主檔，該方案主要使用的旅館` |
| `tppdm98` | `pd98_mstfn` | `None` | `FK → 員工主檔` |

## E. 無法自動分類(需人工判讀)

- `istbm83.tb83_groupno` — `FK`
- `ssorm00.ordr_agent` — `FK → opagm00 (法人資料主檔)`
- `ssorm00.ordr_sales` — `FK → opagm20 (員工主檔)`
- `ssorm07.or07_code` — `FK → istbm81 (CHECKLIST)`
- `tppdm16.pd16_demandcode` — `FK → istbm81 (DEMANDLIST)`
- `tppdm21.pd21_ctokey` — `FK → Ctom85 (VIEW)`

## D. 偽 FK(已併入 E)

本分類目前空,無偵測到純註解被誤填為 fk_note 的案例。

---

## 建議行動計畫

### 立即可做(一次性腳本)

- 寫 migration script 把 A 類(14筆)全數改寫為標準 `fk:` 欄位
- 腳本讀本檔案的「建議改寫為」欄位,批次修 `tables/*.yaml`

### 需團隊討論(schema 設計決策)

- **B 類(18筆)**:是否要支援 `fk_condition:`?還是維持 `fk_note` 但規範格式?
- **C 類(22筆)**:是否要新增 `external: true` 標記?或另建一份 external_refs.yaml?

### 人工處理

- **E 類(6筆)**:按上方清單逐筆確認原意

