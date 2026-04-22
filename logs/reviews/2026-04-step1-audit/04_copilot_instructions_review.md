# copilot-instructions.md 審查報告

> 審查對象:`.github/copilot-instructions.md`(lion-erp-schema-docs)
> 審查框架:改編 skill-reviewer 的維度,適配 GitHub Copilot instruction 檔情境
> 審查日期:2026-04-22

---

## Summary

整體評分 **2.7 / 5**(6 維度平均)。

這份 instructions 在 **基本路由規則**(正向/反向查詢)與 **禁止行為**(copy 來源、scope 宣告)上寫得清楚,這是 Copilot 穩定運作的底線。

但在 **真實失敗模式的預防**、**跨 table 查詢路由**、**與 repo 當前資料狀態的對齊** 三個維度上有明顯缺口。最嚴重的問題是:**指令說「以 schemas/ 為唯一欄位參考」,但 schemas 本身品質問題(15 張缺 PK、9 張欄位型別全 unknown、60 個非標準化 FK)沒有被 instructions 告知,Copilot 會在這些 table 上給出無法落地的建議而不自知。**

## Score

| 維度 | 分數 | Notes |
|------|------|-------|
| D1. Trigger/Activation | 3/5 | 隱性啟動,沒有 trigger 關鍵字列表 |
| D2. Gotchas/Failure modes | 2/5 | 有「禁止行為」但不是真實失敗模式;缺警示清單 |
| D3. Routing clarity | 3/5 | 正向/反向清楚,跨 table / SQL 生成沒寫 |
| D4. Constraint enforcement | 4/5 | 禁止推測、禁止中文欄位名 — 寫得好 |
| D5. Consistency with repo state | 1/5 | 🔴 關鍵問題:沒告知 schemas 現存的資料品質缺口 |
| D6. Evolvability | 3/5 | 結構簡單易編輯,但沒有寫「如何新增規則」的元規則 |
| **Overall** | **2.7 / 5** | |

---

## 🔴 Critical Issues

### C1. instructions 與 repo 當前資料狀態脫鉤

**現況**:instructions 寫「以 `schemas/*.md` 為唯一欄位參考」,但沒告訴 Copilot:
- 有 9 張 `tppcm*` table 所有欄位的 `type` 都是 `unknown`
- 有 15 張 table 沒有標 PK
- 有 60 個 FK 是 `fk_note` 自由文字(其中 22 個指向 repo 外部)

**後果**:Copilot 對這些 table 會信誓旦旦地產出 SQL(因為規則說「以 schemas 為準」),但建議出來的結果可能:
- 使用錯誤型別做 JOIN(因為 type=unknown)
- 假設不存在的 PK(因為沒標 PK)
- 把不在 repo 的 table(如 `opagm20`)當成存在的 table

**建議改寫**:在 instructions 加一個「資料品質警示」區塊(具體內容見下方 Suggested Rewrites)。

### C2. 沒有「跨 table 查詢」路由

**現況**:instructions 只有「正向查詢」與「反向查詢」兩個場景。
但 RD 實際最常問的「幫我寫 JOIN 查某團所有訂單」、「從估價到出團資料怎麼流」這類跨 table 問題,沒有路由規則。

**後果**:Copilot 自行決定 JOIN 欄位,很容易接錯(例如把 `ordr_prod` JOIN 到 `pd11_prod` 而漏掉 `ordr_year`)。

**建議改寫**:新增「跨 table 查詢」場景,指向 `domains/*.md` 的 SQL 範例區。

### C3. scope 宣告與 YAML 內容矛盾

**現況**:README 和 instructions 都宣告「不收錄 LionGroupRPM」,但 YAML 內實際有:
- `bookm10` — database 標 LionGroupRPM
- `iscpm00` — database 標 LionGroupRPM
- `istbm00` — database 標 LionGroupRPM

**後果**:Copilot 按 instructions 應該回答「schema 文件未收錄此 table」,但實際上讀到檔案會回答。這種自相矛盾會讓 Copilot 行為不穩定。

**建議改寫**:先修 YAML 的 database 欄位(若這些 table 其實屬於 LionGroupERP),或修 README 擴張 scope。instructions 再加一條規則:「若 YAML 的 database 非 LionGroupERP,視為 scope 外」。

---

## 🟡 Improvements

### I1. D1 — 補 trigger 觸發關鍵字列表

目前 instructions 沒有「當使用者說 X 時」這種觸發語。Copilot 啟動靠 repo context,但明確列出關鍵字可大幅提升命中率。

**建議新增**:
```markdown
## 觸發場景(Copilot 參考時機)

當使用者的問題包含以下關鍵字時,優先參考本 instructions 與 schemas/:
- **欄位/結構**:欄位、型別、FK、PK、schema、table
- **業務物件**:團號、訂單、估價、行程、旅客
- **SQL 請求**:「幫我寫 SQL」、「查詢」、「join」
- **table 名 pattern**:tppdm*、tppcm*、ssorm*、wtorm*、bookm*、istbm*、isbum*
```

### I2. D2 — 補真實失敗模式的 Gotchas

現況是「禁止行為」清單(規範性的),但沒有「Copilot 過去實際犯過的錯」。這個 repo 才剛建立,可以先預填一些從 schemas 現況可預期的失敗模式:

```markdown
## 常見 Copilot 失誤(預防清單)

1. **把 fk_note 當標準 FK 用**:看到 `fk_note: FK → istbm00 (ATTR)`,Copilot 可能直接產出 `JOIN istbm00 ON ...`,漏掉 `AND istbm00.tabl_type='ATTR'` 的條件
2. **假設 type=unknown 的欄位可做算術**:tppcm* 系列欄位型別標 unknown,Copilot 可能產出 `SUM(tp40_tot_amt)` 而不知道可能是字串型別
3. **以 table 名規律推測不存在的 table**:看到 tppdm10、tppdm11,Copilot 可能自行產出 tppdm12、tppdm13 的 SQL 而這些 table 確實存在但不是 Copilot 預期的語意
4. **用舊 description 生成 SQL**:tppdm11 在 repo 寫「出團行程檔」但實際是人數統計檔 — Copilot 若憑 description 理解會答錯
```

### I3. D3 — 補「影響範圍查詢」路由

類似 C2,但這是查詢場景的擴充:

```markdown
## 場景:改動影響範圍查詢

使用者問「改 X 會影響哪些 table」或「誰引用這張 table」時:
1. 優先參考 `_generated/fk_reverse_index.md`(需先建立)
2. 若無此檔,退而以關鍵字搜尋所有 `schemas/*.md` 的 FK 欄
3. **禁止**基於 table 名相似度推測關聯,必須有實際 FK 證據
```

### I4. D5 — 補「資料品質警示」區塊

這是 C1 的正面改寫版。建議加一整個區塊:

```markdown
## 資料品質警示(截至 2026-04)

本 repo 仍在建置中,以下品質問題會影響 Copilot 答題準確度:

### Type=unknown 的 table(9 張,共約 60 個欄位)

`tppcm00`、`tppcm09`、`tppcm10`、`tppcm20`、`tppcm21`、`tppcm30`、
`tppcm40`、`tppcm41`、`tppcm50`

**規則**:為這些 table 產 SQL 時,**必須**附註「型別未確認,執行前請 DBA 驗證」。
**禁止**:對這些欄位假設 decimal/int/varchar 型別。

### 無 PK 標記的 table(15 張)

見 `logs/manual_todo.md` 「無 PK 標記」區塊。

**規則**:為這些 table 產 INSERT/UPDATE SQL 時,**必須**詢問使用者 PK 是什麼。

### 非標準化 FK(60 個欄位用 fk_note)

**規則**:看到 `fk_note` 時,**不可**直接當 FK 使用。
- 若 fk_note 含 "istbm00 (XXX)":這是多型 FK,需加 `istbm00.tabl_type='XXX'` 條件
- 若 fk_note 指向非 schemas 收錄的 table(如 opagm20):直接告知使用者「此 FK 目標不在本 repo」
```

---

## 🟢 What's Working

### G1. 正向查詢規則寫得清楚(D3 的亮點)

「優先從 `schemas/{table_name}.md` 取得資料」這類指示非常明確,Copilot 幾乎不會搞錯。H1 / Aliases / Columns 三層的定位也清楚。

### G2. 禁止行為清單具體(D4 的亮點)

「不要從 `tables/*.yaml` 直接讀取」、「不要使用中文欄位名作為欄位識別」這類規則非常明確,Copilot 不容易越界。這是目前 instructions 最堅固的部分。

### G3. Scope 宣告存在(D5 部分加分)

有宣告不收錄 LionGroupRPM/CMS。**可惜**實際資料沒對齊(見 C3),但方向是對的。

### G4. 簡潔(D6 加分)

整份 instructions 不到 40 行,團隊共編門檻低。但要注意 — 隨著 domains 擴充,這個長度會漲,需要早點規劃章節切分。

---

## Suggested Rewrites

### 建議改寫後的 copilot-instructions.md 結構

```markdown
# Lion ERP Schema 使用指引

本 repo 是雄獅旅遊 ERP 資料庫(LionGroupERP)的 schema 文件。

## 觸發場景(Copilot 參考時機)
[見 I1]

## 查詢場景路由

### 場景 A:正向查詢(知道 table 名)
[保留現有邏輯]

### 場景 B:反向查詢(不知道 table 名)
[保留現有邏輯]

### 場景 C:跨 table JOIN 查詢(新)
1. 先讀 `domains/{相關 domain}.md` 的 SQL 範例
2. 若跨 domain,讀各相關 domain 的「跨 domain FK」章節
3. **禁止**自行推測 JOIN 條件,必須有實際 FK 證據

### 場景 D:影響範圍查詢(新)
[見 I3]

## 資料品質警示(截至 YYYY-MM)
[見 I4 — 建議此區塊由 CI 自動更新,避免人工維護落後]

## 常見 Copilot 失誤(預防清單)
[見 I2]

## 禁止行為
[保留現有邏輯]

## Scope
- 本 repo 只收錄 `database: LionGroupERP` 的 table
- 若 YAML 的 database 非 LionGroupERP,Copilot 應視為 scope 外並回「schema 文件未收錄」
- 詳細 Non-Scope 見 README

## 補充說明
[保留現有邏輯]
```

---

## 測試建議

當 instructions 改完後,建議跑以下 3 個 test prompts 驗證:

1. **「tppcm00 的 tp00_tpform 是什麼型別?」**
   預期 Copilot 答:「型別在 schemas 中標為 unknown,需 DBA 確認」
   若 Copilot 自信地答「varchar」,代表 I4 警示沒生效。

2. **「幫我寫查某團所有 ssorm00 訂單並帶出 tppdm10 的團名」**
   預期 Copilot 用 `ordr_prod = prod_prod` 且至少檢查 ordr_year
   若 Copilot 接錯欄位或漏年,代表 C2 的跨 table 路由沒生效。

3. **「改 tppdm10 的 PK 會動到哪些 table?」**
   預期 Copilot 引用 FK 反向索引(見產出 1),列出 25+ 個引用點
   若 Copilot 只給通論「可能會影響訂單」,代表 I3 的影響範圍路由沒生效。

---

## 元建議:把這份 review 加入 PR 流程

目前 copilot-instructions.md 的品質沒有 CI 把關。建議:
1. 這份 review 存到 repo 的 `logs/reviews/2026-04-copilot-instructions-review.md`
2. 每次 PR 修改 copilot-instructions.md 或 domains/ 時,reviewer 對照本檔的維度 checklist
3. 每季跑一次自動化 review(靠這類腳本產出),追蹤 schemas 品質變化
