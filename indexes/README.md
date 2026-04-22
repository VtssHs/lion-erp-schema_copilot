# indexes/ — Copilot 運行時索引

本資料夾的檔案是**給 Copilot 讀的索引**,由 `tables/*.yaml` 自動產出。

## 檔案用途

| 檔案 | 用途 | Copilot 何時讀 |
|------|------|---------------|
| [`fk_reverse.md`](./fk_reverse.md) | FK 反向索引 | 回答「改 X 會影響什麼」「誰引用 X」時 |
| [`schema_quality.md`](./schema_quality.md) | 資料品質警示(type=unknown、無 PK、多型 FK) | 產出任何 SQL / DDL 前 |
| [`external_refs.md`](./external_refs.md) | 外部 table 白名單 | 看到 FK 指向陌生 table 時 |

## 與 `logs/reviews/` 的差別

- **`indexes/`**:Copilot 運行時會讀,每次 build 從 YAML 重生
- **`logs/reviews/`**:歷史盤點快照,給人類看,不會自動更新

## 與 `schemas/` 的差別

- **`schemas/`**:單張 table 的完整欄位定義(從 YAML 產出)
- **`indexes/`**:跨 table 的聚合索引與品質警示(從 YAML 計算產出)

## 自動重生

每次 PR 改動 `tables/*.yaml` 時,CI 會自動重生 `indexes/`。
**請勿手動編輯此資料夾的 `.md` 檔案**。

## 下一步(待 CI 支援)

目前 `indexes/` 是手動產出的初版。待 `tools/` 新增 index generation script 後,
會整合到 `.github/workflows/build.yml` 自動化。
