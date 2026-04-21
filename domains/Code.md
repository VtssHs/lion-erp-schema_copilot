# Code Domain — 出發日管理

> **Domain 定義**：Code（出發日）是 ERP 系統的核心控制域。一個 Code = 一個可出發的旅遊產品實例（固定的出發日、行程、定價、配額）。所有訂單、估價、導領資料都以 Code 為錨點。

## Business Object → Table 映射

| Business Object | 對應 Table | 說明 |
|---|---|---|
| 出發日主檔 | `tppdm10` | Code 的核心紀錄；一行 = 一個可出發的團 |
| 出發日副檔（詳細設定） | `tppdm16` | 簽證、包含/不含費用、旅遊契約、保險設定 |
| 說明會 / 導領核派 | `tppdm12` | 說明會作業、領隊指派與確認流程 |
| 行程內容（後台） | `tppdm20` | 後台行程主檔（大 tppdm10 的行程欄位） |
| 行程顯示細節 | `tppdm19` / `tppdm19a` | 行程天描述、注意事項 |
| 售價設定 | `tppdm90` | 各人別（大人/小孩/嬰兒）售價主檔 |
| 售價明細 | `tppdm91` / `tppdm92` / `tppdm93` | 各類價格細分（票價、稅費、附加費） |
| 配額控管 | `tppdm50` | 各人別剩餘配額；候補管理 |
| 旅館安排 | `tppdm40` / `tppdm41` | 行程各夜旅館；房型/Check-in/Check-out |
| 銷售須知 | `tppdm55` / `tppdm56` / `tppdm57` | 前台顯示的必讀須知 |
| 出發地設定 | `tppdm60` / `tppdm61` | 出發地點（集合地、搭機城市） |
| 費用包含 / 不包含 | `tppdm62` / `tppdm63` | 費用包含 / 不包含說明文字 |
| 附加費 | `tppdm64` / `tppdm65` / `tppdm66` | 單人房差、附加費、附加費說明 |
| 地接社設定 | `tppdm67` | LOCAL 地接社代碼與聯絡資訊 |
| 估價單（關聯） | `tppcm00` | 本 Code 對應的估價主檔（通過 `prod_tpform` FK） |
| 估價檔次 | `tppcm40` | 每個估價的 1~6 檔次定價結果 |

## 核心關聯圖（文字版）

```
tppcm00 (估價主檔)
  └── tppcm40 (檔次報價總表)  ← 1:6
       └── tppcm30 (Local成本主檔)
            └── tppcm50 (Local成本明細)

tppdm10 (出發日主檔)  ← 所有 Code domain 的錨點
  ├── tppdm16  (副檔：簽證/費用包含/契約)       1:1
  ├── tppdm12  (說明會/導領核派)                  1:1
  ├── tppdm20  (行程後台主檔)                     1:1
  ├── tppdm19  (行程天描述)                       1:N
  ├── tppdm90  (售價主檔)                         1:1
  │    ├── tppdm91  (售價明細-票)                1:N
  │    ├── tppdm92  (售價明細-稅)                1:N
  │    └── tppdm93  (售價明細-附加)              1:N
  ├── tppdm50  (配額控管)                         1:1
  ├── tppdm40  (旅館安排)                         1:N
  ├── tppdm60  (出發地)                           1:N
  └── tppdm67  (地接社)                           1:N

tppdm10.prod_tpform → tppcm00.tp00_tpform  (估價單 FK)
tppdm10.prod_size   → tppcm40.tp40_size    (檔次 FK)
```

## 核心 Tables 一覽

### `tppdm10` — 出發日主檔

> 整個 Code domain 的根。每行代表一個可出發的團（出發日 + 行程 + 定價已確立）。

**關鍵欄位**

| Column | 業務意義 |
|---|---|
| `prod_prod` | 團號（PK）。格式如 `9Z25A001`，編碼規則：線別+年份+序號 |
| `prod_d8` / `prod_d9` | 出發日 / 回國日 |
| `prod_sts` | 團型（1=outb, 2=票團, 3=外丟, 4=商務, 5=Inb, 6=Local） |
| `prod_full` | 團控狀況（C=結, L=鎖, M=挪, V=取消） |
| `prod_max` / `prod_min` | 團位數 / 追加機位 |
| `prod_go` | 保證出團（1=保證） |
| `prod_tpform` | FK → `tppcm00`（此團使用哪張估價單） |
| `prod_size` | FK → `tppcm40`（使用估價的第幾檔次） |
| `prod_amt_d` / `prod_amt_w` | 直售價 / 批售價（從 `tppdm90` 反寫，加速 search） |

**常用查詢場景**

```sql
-- 查某條線在某時段的出發日清單
SELECT prod_prod, prod_name, prod_d8, prod_d9, prod_full
FROM tppdm10
WHERE prod_line = 'EU'
  AND prod_d8 BETWEEN '2025-01-01' AND '2025-06-30'
  AND prod_full NOT IN ('V')  -- 排除取消
ORDER BY prod_d8;

-- 查某團的估價單與檔次
SELECT prod_prod, prod_tpform, prod_size, prod_amt_d, prod_amt_w
FROM tppdm10
WHERE prod_prod = '9Z25A001';
```

---

### `tppdm16` — 出發日副檔（簽證/費用包含/契約）

> `tppdm10` 的 1:1 延伸。儲存前台顯示需要但主檔放不下的設定。

**關鍵欄位**

| Column | 業務意義 |
|---|---|
| `pd16_prod` | FK → `tppdm10.prod_prod` (PK) |
| `pd16_vscountry1~5` + `pd16_vsseq1~5` | 簽證需求（國家 + 簽證類型，最多 5 組） |
| `pd16_vsinc1~5` | Y/N = 此簽證費是否含在團費內 |
| `pd16_visa_i` / `pd16_visa_n` | 前台顯示文字（包含簽 / 不包含簽） |
| `pd16_airp_i` / `pd16_airp_n` | 機場稅費包含 / 不包含說明 |

---

### `tppdm90` — 售價主檔

> 每個出發日的定價核心。各人別（ADT/CHD/INF）的標準售價都在這裡。

**關鍵欄位**

| Column | 業務意義 |
|---|---|
| `pd90_prod` | FK → `tppdm10.prod_prod` (PK) |
| `pd90_pay` | 訂金金額（回寫到 `tppdm10.prod_pay`） |
| `pd90_payfull` | 是否需全額付清才能確認（回寫到主檔） |
| `pd90_amt_d` / `pd90_amt_w` | 大人直客價 / 同業價 |

---

### `tppdm50` — 配額控管

> 控制每個出發日各人別剩餘可售配額。超賣防控的核心。

**關鍵欄位**

| Column | 業務意義 |
|---|---|
| `pd50_prod` | FK → `tppdm10.prod_prod` (PK) |
| `pd50_max` | 最大可售人數（與 `tppdm10.prod_max` 呼應） |
| `pd50_sold` | 已售人數（ssorm 訂單累計） |
| `pd50_hk` | 候補人數（超賣後仍可下單的緩衝） |

---

### `tppcm00` — 估價主檔

> Code 建立前的估價單。一張估價單可對應多個 Code（相同行程不同出發日共用估價）。

**關鍵欄位**

| Column | 業務意義 |
|---|---|
| `tp00_tpform` | 估價代號（PK） |
| `tp00_fsts` | 進度（空白=建置中, F=完成, V=待審） |
| `tp00_fdate` / `tp00_tdate` | 此估價適用出發日期範圍 |
| `tp00_profit_d` / `tp00_profit_w` | 目標直客毛利% / 同業毛利% |
| `tp00_curr` | 估價幣別 |

---

### `tppcm40` — 檔次報價總表

> 每張估價單可有 1~6 個人數檔次（例如：16人/20人/24人），每個檔次對應不同成本與定價。

**關鍵欄位**

| Column | 業務意義 |
|---|---|
| `tp40_tpform` | FK → `tppcm00.tp00_tpform` |
| `tp40_size` | 檔次號（1~6） |
| `tp40_tot_amt` | 每人總成本 |
| `tp40_amt_w` / `tp40_amt_d` | 計算出的同業定價 / 直客定價 |
| `tp40_git` | 實際付費人數（不含 FOC/TL） |
| `tp40_foc` | FOC 人數（免費招待） |

---

## Domain 邊界說明

**Code domain 管什麼**
- 出發日的建立與維護（開團）
- 售價設定與審核
- 配額設定
- 前台顯示資訊（行程、費用說明、簽證）
- 估價單關聯

**Code domain 不管什麼**
- 訂單與旅客名單 → `ssorm*`（Order domain）
- 行程組合器的行程塊/天 → `trip*`（Itin domain，獨立系統）
- 導領執行與 QAM 評鑑 → S5 負責
- 財務立帳 → `wtorm*`

**跨 domain 的關鍵 FK**

| 來源 | 欄位 | 去向 | 說明 |
|---|---|---|---|
| `ssorm00.ordr_prod` | → | `tppdm10.prod_prod` | 訂單屬於哪個出發日 |
| `tppdm10.prod_tpform` | → | `tppcm00.tp00_tpform` | 此出發日用哪張估價 |
| `tppdm10.prod_tur2` | → | `trip00.trip_no` | 此出發日用哪個行程組合器行程 |
