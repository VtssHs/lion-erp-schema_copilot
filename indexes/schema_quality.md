# Schema 資料品質警示(indexes/schema_quality.md)

> **用途**:Copilot 產出 SQL 或 schema 建議前的強制檢查清單
> **自動產出**,每次 build 時重生
> **Copilot 使用時機**:產出任何涉及 table 的 SQL / DDL / JOIN 建議前,**必讀**

---

## 一、快速檢查摘要

當使用者要求 SQL / schema 建議時,按下列表檢查:

| 檢查項 | 影響 table 數 | 章節 |
|--------|--------------|------|
| 欄位型別 = `unknown` | 9 | [§二](#二型別未確認的-table) |
| 無 PK 標記 | 15 | [§三](#三無-pk-標記的-table) |
| 含多型 FK(istbm00) | 11 | [§四](#四多型-fk-必須加條件) |
| 含非標準 fk_note | 36 | [§五](#五非標準-fk_note) |

---

## 二、型別未確認的 table

以下 table 所有欄位的 `type` 標為 `unknown`,代表型別資訊缺失:

- `tppcm00` — 團體產品估價主檔
- `tppcm09` — 估價幣別匯率檔
- `tppcm10` — 估價明細成本檔
- `tppcm20` — 估價明細檔
- `tppcm21` — 估價明細暫存計算檔
- `tppcm30` — 檔次估價成本主檔
- `tppcm40` — 檔次報價總表
- `tppcm41` — 檔次成本明細檔
- `tppcm50` — 估價單附件檔案管理表

### 規則

涉及以上 table 時,Copilot **必須**:

1. **不可假設欄位型別**(不要預設是 varchar/decimal/int)
2. **不可產出依賴型別的 SQL 函數**(如 `SUM()`、`CAST()`、日期運算)而不加警示
3. **必須在回答末尾加註**:「⚠️ 此 table 欄位型別尚未在 schema 中確認,執行前請 DBA 或查詢實際 DB 驗證」

### 範例

**❌ 不合規的回答**:
```sql
SELECT SUM(tp40_tot_amt) FROM tppcm40 WHERE tp40_size = 1;
```
(直接用 SUM,假設是數值型別)

**✅ 合規的回答**:
```sql
-- ⚠️ tppcm40 欄位型別在 schema 中標為 unknown,以下 SQL 假設 tp40_tot_amt 為數值型別
-- 執行前請向 DBA 或 DB 確認 tp40_tot_amt 的實際型別
SELECT SUM(tp40_tot_amt) FROM tppcm40 WHERE tp40_size = 1;
```

---

## 三、無 PK 標記的 table

以下 table 的 YAML 中沒有任何欄位標 `pk: true`。可能原因:
- schema 文件遺漏
- table 真的沒有單一 PK(使用複合 key)
- 有複合 PK 但未標註

**完整清單**:

- `bookm01` — 預訂明細
- `tppcm09` — 估價幣別匯率檔
- `tppcm10` — 估價明細成本檔
- `tppcm20` — 估價明細檔
- `tppcm40` — 檔次報價總表
- `tppcm41` — 檔次成本明細檔
- `tppcm50` — 估價單附件檔案管理表
- `tppdm12` — 說明會副檔
- `tppdm20` — 團體行程代號主檔
- `tppdm27` — 團體行程修改自動留言檔
- `tppdm30` — 團體產品行程異動記錄檔
- `tppdm61` — 郵輪接駁車
- `tppdm63` — 郵輪岸上觀光景點
- `tppdm90` — 團體售價資料檔
- `tptbm09` — 標準團名不發簡訊設定檔

### 規則

涉及以上 table 的 INSERT / UPDATE / DELETE SQL 時,Copilot **必須**:

1. **不可假設某個欄位是 PK**
2. **必須詢問使用者**:「此 table 的 PK 在 schema 中未標註,請確認應該用哪個欄位(組)作為 WHERE 條件?」
3. SELECT 查詢可照常產出,但若使用者明確詢問 PK,按上述處理

---

## 四、多型 FK 必須加條件

以下欄位的 FK 指向 `istbm00`(基礎代碼主檔),但必須加 `tabl_type` 條件才能正確 JOIN。

### 多型 FK 清單(按 tabl_type 分組)

**`tabl_type = 'ATTR'`** (3 個欄位):

- `tptbm00.tbm0_attr1`
- `tptbm00.tbm0_attr2`
- `tptbm00.tbm0_attr3`

**`tabl_type = 'CRSKIND'`** (2 個欄位):

- `ssorm02.or02_crs`
- `wtorm00.Wor00_crs`

**`tabl_type = 'CXLDESC'`** (1 個欄位):

- `wtorm00.wor00_cxldesc`

**`tabl_type = 'FORM'`** (1 個欄位):

- `tppdm10.prod_form`

**`tabl_type = 'FREEKIND'`** (1 個欄位):

- `tptrm20.tr20_freekind`

**`tabl_type = 'MEAT'`** (1 個欄位):

- `ssorm11.or11_meat`

**`tabl_type = 'MEET'`** (1 個欄位):

- `tppdm12.pd12_meetplace`

**`tabl_type = 'NOTE'`** (1 個欄位):

- `tptbm10.note_note`

**`tabl_type = 'PDHOT'`** (1 個欄位):

- `tptrm32.tr32_pdhot`

**`tabl_type = 'PSUBJECT'`** (3 個欄位):

- `tptbm00.tbm0_psubject1`
- `tptbm00.tbm0_psubject2`
- `tptbm00.tbm0_psubject3`

**`tabl_type = 'RELMAN'`** (1 個欄位):

- `ssorm11.or11_urgent_relman`

**`tabl_type = 'TAIRLINE'`** (1 個欄位):

- `ssorm10.orer_tairline`

**`tabl_type = 'TKPERIOD'`** (1 個欄位):

- `wtorm10.wor10_tkperiod`

### 規則

為以上欄位產出 JOIN SQL 時,Copilot **必須**:

1. **一律加 `tabl_type` 條件**,不可寫 `JOIN istbm00 ON prod_form = tabl_code` 這種漏條件的 SQL
2. **正確範例**:
```sql
JOIN istbm00 AS form_code 
  ON form_code.tabl_code = tppdm10.prod_form 
  AND form_code.tabl_type = 'FORM'
```

---

## 五、非標準 fk_note

共 **36 張 table** 含有 `fk_note`(非標準化 FK 記錄)。

**使用原則**:

- 遇到 `fk_note` 欄位,**不可**直接當標準 FK 使用
- 必須查 [indexes/fk_reverse.md §四](./fk_reverse.md) 的外部引用章節確認目標
- 多型 FK(§四 已列)直接套 §四 規則即可
- 外部引用:告知使用者「此 FK 目標不在本 repo」,禁止 hallucinate

**修正進度**:60 筆 fk_note 中,14 筆預計機械轉為標準 `fk:`,18 筆待新增 `fk_condition:` 語法,22 筆為外部引用。詳見 `logs/reviews/2026-04-step1-audit/02_fknote_classification.md`。

---

## 六、已知 description 不準確的 table

以下 table 的 `description` 在 schema 與實際業務語意存在落差:

| Table | Schema 描述 | 實際語意 | 處理 |
|-------|------------|----------|------|
| `tppdm11` | 出團行程檔 | 團訂單人數檔(欄位全為 HL/HK/KK 等訂單統計) | 產 SQL 時優先依欄位語意,不依 description |
| `bookm10` | 團體訂單主檔(CTO 元件預訂) | erp-schema skill 標為「預訂旅客資料檔」(**語意衝突**) | 產涉及 bookm10 的 SQL 時必須先跟使用者確認用途 |

---

## 七、Scope 衝突 table

README 宣告本 repo 只收錄 `LionGroupERP` database,但以下 table 的 YAML 標註為其他 database:

| Table | YAML 標註的 database | 應處理方式 |
|-------|---------------------|-----------|
| `bookm10` | LionGroupRPM | 待團隊決議是移除還是修標註 |
| `iscpm00` | LionGroupRPM | 同上 |
| `istbm00` | LionGroupRPM | 同上(影響重大,23 個欄位引用它) |

**Copilot 規則**:看到以上 3 張 table 的查詢時,可照常回答,但**須附註**:「此 table 的 database 歸屬在團隊討論中,查詢結果以實際 DB 為準。」

