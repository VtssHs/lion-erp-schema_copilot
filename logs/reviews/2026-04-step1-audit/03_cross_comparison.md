# 交叉比對:lion-erp-schema-docs(repo)vs erp-schema skill

> 這份報告比對兩個來源,找出:
> 1. 只有一方有的 table(覆蓋率差異)
> 2. 兩邊都有但語意不一致的 table(schema drift)
> 3. Database 標註不一致(SSOT 衝突)
> 4. erp-schema 的 skill 覆蓋率相對 repo 的進度

## 基本統計

- **repo tables**: 106
- **skill tables**: 135
- **交集**(兩邊都有): 106
- **只在 repo**: 0
- **只在 skill**: 29

---

## 一、只在 repo 的 table(0 張)

(無)

## 二、只在 skill 的 table(29 張)

這些 table 在 skill 有 schema,repo 尚未收錄。按命名前綴分組:

### `dbfdm*` (2 張)

- `dbfdm00`
- `dbfdm00tmp`

### `dbrtm*` (1 張)

- `dbrtm00`

### `dbtbm*` (1 張)

- `dbtbm00`

### `logor*` (3 張)

- `logortbm10`
- `logortbm10a`
- `logortbm12`

### `orbzm*` (1 張)

- `orbzm00`

### `orctm*` (1 張)

- `orctm00`

### `ordom*` (2 張)

- `ordom00`
- `ordom10`

### `orflm*` (1 張)

- `orflm00`

### `orldm*` (2 張)

- `orldm00`
- `orldm10`

### `orlkm*` (1 張)

- `orlkm00`

### `ornom*` (1 張)

- `ornom00`

### `orrpm*` (1 張)

- `orrpm00`

### `orsdm*` (1 張)

- `orsdm00`

### `ortbm*` (10 張)

- `ortbm00`
- `ortbm01`
- `ortbm01_lang`
- `ortbm02`
- `ortbm03`
- `ortbm03_lang`
- `ortbm04`
- `ortbm10`
- `ortbm11`
- `ortbm12`

### `ortrm*` (1 張)

- `ortrm00`

---

## 三、兩邊都有但值得檢查語意差異的 table

以下是已知在兩邊都有、但從 index.md 觀察到 **說明不一致** 的 table。
這不代表一定有錯,但建議人工確認語意對齊。

### `bookm10` 🔴 高

- **repo**: 團體訂單主檔(CTO 元件預訂)
- **skill**: 預訂旅客資料檔
- **問題**: 這是兩種完全不同的業務物件 — 一個記 CTO 元件預訂,一個記旅客。必須確認 real DB 的 table structure 是哪一個。

### `tppdm11` 🟡 中

- **repo**: 出團行程檔
- **skill**: 團訂單人數檔
- **問題**: repo 的欄位(pd11_hl/pd11_hk/pd11_ob 等)明顯是訂單人數統計,skill 的命名比較貼切。repo 的 description 可能過時。

### `istbm00` 🔴 高

- **repo**: Database: LionGroupRPM
- **skill**: Database: LionGroupERP(依 index.md 分類)
- **問題**: memory 裡記錄 istbm00 應屬 LionGroupERP(團體產品管理模組基礎代碼),但 repo 標成 LionGroupRPM。這會影響 README 的 Non-Scope 宣告。

### `iscpm00` 🔴 高

- **repo**: Database: LionGroupRPM
- **skill**: Database: LionGroupERP(依 index.md 分類到 ISCPM 模組)
- **問題**: 同上,公司主檔的歸屬需要對齊。

---

## 四、repo 內部的 Database 欄位審查

README 明確宣告「不收錄 LionGroupRPM」,但實際 YAML 中發現:

### Database = `LionGroupERP` (103 張)

- `bookm00`
- `bookm01`
- `isbum00`
- `isbum01`
- `isbum02`
- `isbum03`
- `iscpm21`
- `ispfm00`
- `istbm10`
- `istbm11`
- `istbm12`
- `istbm20`
- `istbm82`
- `istbm83`
- `istbm83_lan`
- `optbm18`
- `ssorm00`
- `ssorm01`
- `ssorm02`
- `ssorm03`
- `ssorm04`
- `ssorm05`
- `ssorm06`
- `ssorm07`
- `ssorm10`
- `ssorm11`
- `ssorm12`
- `ssorm13`
- `ssorm14`
- `tppcm00`
- `tppcm09`
- `tppcm10`
- `tppcm20`
- `tppcm21`
- `tppcm30`
- `tppcm40`
- `tppcm41`
- `tppcm50`
- `tppdm10`
- `tppdm11`
- `tppdm12`
- `tppdm13`
- `tppdm14`
- `tppdm15`
- `tppdm16`
- `tppdm17`
- `tppdm18`
- `tppdm19`
- `tppdm19a`
- `tppdm20`
- `tppdm20_ez`
- `tppdm21`
- `tppdm21_ez`
- `tppdm22`
- `tppdm23`
- `tppdm24`
- `tppdm25`
- `tppdm25_ez`
- `tppdm26`
- `tppdm27`
- `tppdm30`
- `tppdm36`
- `tppdm40`
- `tppdm41`
- `tppdm50`
- `tppdm55`
- `tppdm56`
- `tppdm57`
- `tppdm60`
- `tppdm61`
- `tppdm62`
- `tppdm63`
- `tppdm64`
- `tppdm65`
- `tppdm66`
- `tppdm67`
- `tppdm76`
- `tppdm81`
- `tppdm90`
- `tppdm91`
- `tppdm92`
- `tppdm93`
- `tppdm98`
- `tptbm00`
- `tptbm02`
- `tptbm06`
- `tptbm09`
- `tptbm10`
- `tptbm11`
- `tptbm15`
- `tptbm20`
- `tptbm20_lang`
- `tptbm30`
- `tptbm31`
- `tptrm20`
- `tptrm21`
- `tptrm22`
- `tptrm30`
- `tptrm32`
- `wtorm00`
- `wtorm10`
- `wtorm20`
- `wtorm30`

### Database = `LionGroupRPM` (3 張)

⚠️ **違反 README Non-Scope 宣告**。需要決定:
- (a) 把這些 table 移出 repo
- (b) 修改 README,把 scope 擴張到這些 db
- (c) 確認是標註錯誤,改回 LionGroupERP

- `bookm10`
- `iscpm00`
- `istbm00`

---

## 五、從 skill 可借用但 repo 還沒做的結構

erp-schema skill 的 `index.md` 有幾個 repo 目前沒有的結構,值得借用:

1. **業務場景快速導航**:index.md 開頭的「我要建立新產品/開團收客/處理訂單」就是一份初版的「查詢場景路由表」
2. **建檔狀態標記**(✓/🔧/⚠️):用符號標記每張 table 的完整度,對共編非常友善
3. **按 module 分組的 table 清單**:目前 repo 把 module 放在 YAML 內部,外部索引反而沒有
4. **`inferred_tables.md`**:推測但未確認的 table 獨立隔離,避免污染 SSOT

