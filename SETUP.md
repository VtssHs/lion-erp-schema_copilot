# 部署指引

本壓縮包含兩個獨立的 GitHub repo 內容。請依以下步驟部署。

## 總覽

- `lion-erp-schema-tools/` → 推到 GitHub 成為 **工具 repo**（PM 維護用）
- `lion-erp-schema-docs/` → 推到 GitHub 成為 **文件 repo**（RD submodule 引用）

## 本次包已完成的自動作業

- 106 張 table 從舊版 erp-schema 遷移完成
- 106 張 table 的 aliases 已自動補完（從 H1、模組、用途關鍵字抽取）
- 5 個中文泛詞、6 個英文縮寫衝突已被自動剔除
- 詳見 `lion-erp-schema-docs/logs/alias_seeding_report.md`

## 步驟 1：建立 tools repo

```bash
cd lion-erp-schema-tools
git init
git add .
git commit -m "Initial commit: ERP schema tooling"
git remote add origin git@github.com:YOUR_ORG/lion-erp-schema-tools.git
git branch -M main
git push -u origin main
```

## 步驟 2：建立 docs repo

```bash
cd ../lion-erp-schema-docs
git init
git add .
git commit -m "Initial commit: ERP schema docs (106 tables with aliases)"
git remote add origin git@github.com:YOUR_ORG/lion-erp-schema-docs.git
git branch -M main
git push -u origin main
```

## 步驟 3：修 CI 中的 org 名稱

編輯 `lion-erp-schema-docs/.github/workflows/build.yml` 第 18 行：

```yaml
repository: YOUR_ORG/lion-erp-schema-tools
```

commit 並 push。

## 步驟 4：若兩個 repo 都是 private

CI 需要從 docs repo 讀 tools repo。設定 PAT：

1. 到 tools repo Settings → Deploy keys 或產生 PAT
2. 到 docs repo Settings → Secrets → 新增 `TOOLS_REPO_TOKEN`
3. 把 `build.yml` 第 19 行的 `# token:` 註解拿掉

## 步驟 5：RD 專案引用 submodule

```bash
git submodule add git@github.com:YOUR_ORG/lion-erp-schema-docs.git docs/erp-schema
```

## 步驟 6：驗證 Copilot 檢索

在 RD 的專案打開 Copilot Chat 問：

```
產品主檔的 gpno 是什麼型別？
```

因為 aliases 已經自動補入「產品主檔」→ tppdm10，Copilot 應該能命中。

## 步驟 7：人工校對（選擇性）

打開 `lion-erp-schema-docs/logs/alias_seeding_report.md`，快速掃過每張 table 的 aliases 是否合理。發現有問題可直接改對應的 `tables/{table}.yaml`，commit 後 CI 會自動重生 md。

常見需要手動補的情境：
- RD 口語用法（例：「產品主檔」如果 H1 是「團體主檔」，可能需要手動加）
- 業務簡稱（例：「PAK 團」、「包機團」等專業術語）

## 日常工作流

```bash
# 改 YAML
vim lion-erp-schema-docs/tables/tppdm10.yaml

# 本地驗證（選擇性，CI 會做同樣的事）
cd lion-erp-schema-docs
python3 ../lion-erp-schema-tools/scripts/yaml_to_md.py
git diff schemas/

# commit & push
git add tables/tppdm10.yaml
git commit -m "Update aliases for tppdm10"
git push
# CI 會自動重生並 commit schemas/
```

## 疑難排解

- CI 失敗 → 看 Actions log
- schemas 和 tables 不同步 → 本地跑 `yaml_to_md.py` 後 commit
- 新加 table → 直接寫 `tables/newtable.yaml`，push 後 CI 會產出對應 md
