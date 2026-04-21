# Alias Seeding Report

- 處理 table 數: 106
- 寫入 YAML: 106
- 跳過（已有 aliases）: 0
- 跳過（無對應 YAML）: 0
- 黑名單門檻: 出現 ≥ 5 張

## 中文黑名單（5 個詞被剔除）

| 詞 | 出現張數 |
|---|---|
| 團體產品系統 | 25 |
| 團體產品管理 | 18 |
| 訂單管理系統 | 13 |
| 團體估價系統 | 9 |
| 郵輪子系統 | 7 |

## 英文縮寫衝突黑名單（6 個縮寫跨 table 衝突）

| 縮寫 | 衝突張數 |
|---|---|
| TBM20 | 2 |
| TBM10 | 2 |
| TBM11 | 2 |
| TBM00 | 2 |
| ORM10 | 2 |
| ORM00 | 2 |

## 各 table 收錄結果

### bookm00
- 最終 aliases: `['預訂主檔', '預訂系統', 'bookm00', 'OKM00', 'BOOKM00']`

### bookm01
- 最終 aliases: `['預訂明細', '預訂系統', 'bookm01', 'OKM01', 'BOOKM01']`

### bookm10
- 最終 aliases: `['團體訂單主檔', 'CTO元件預訂', '預訂管理', '團體預訂主檔', '團體預訂明細', 'bookm10', 'OKM10', 'BOOKM10']`

### isbum00
- 最終 aliases: `['Bu 事業體主檔', '財務結算', 'isbum00', 'BUM00', 'ISBUM00']`

### isbum01
- 最終 aliases: `['bu事業體頻道', 'isbum01', 'BUM01', 'ISBUM01']`

### isbum02
- 最終 aliases: `['bu事業體頻道審核人員', 'isbum02', 'BUM02', 'ISBUM02']`

### isbum03
- 最終 aliases: `['bu事業體不分銷對象設定', 'isbum03', 'BUM03', 'ISBUM03']`

### iscpm00
- 最終 aliases: `['公司主檔', '供應商主檔', 'iscpm00', 'CPM00', 'ISCPM00']`

### iscpm21
- 最終 aliases: `['雄獅國家網站代碼', 'iscpm21', 'CPM21', 'ISCPM21']`

### ispfm00
- 最終 aliases: `['單位主檔', 'ispfm00', 'PFM00', 'ISPFM00']`

### istbm00
- 最終 aliases: `['基礎代碼主檔', 'istbm00', 'ISTBM00']`

### istbm10
- 最終 aliases: `['線別代碼檔', 'istbm10', 'ISTBM10']`

### istbm11
- 最終 aliases: `['各線審核毛利負責人名單', 'istbm11', 'ISTBM11']`

### istbm12
- 最終 aliases: `['各單位線別毛利率與日售價資料', 'istbm12', 'TBM12', 'ISTBM12']`

### istbm20
- 最終 aliases: `['地區代碼檔', 'istbm20', 'ISTBM20']`

### istbm82
- 最終 aliases: `['公用標籤群組檔', 'istbm82', 'TBM82', 'ISTBM82']`

### istbm83
- 最終 aliases: `['公用標籤檔', 'istbm83', 'TBM83', 'ISTBM83']`

### istbm83_lan
- 最終 aliases: `['公用標籤名稱語系檔', 'istbm83_lan', 'TBM83_LAN', 'ISTBM83_LAN']`

### optbm18
- 最終 aliases: `['城市區域檔', '景點與旅遊地點管理', '元件的城市區域分類主檔', 'optbm18', 'TBM18', 'OPTBM18']`

### ssorm00
- 最終 aliases: `['訂單主檔', '團體旅遊正式訂單主檔', 'ssorm00', 'SSORM00']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm01
- 最終 aliases: `['訂單副檔', 'ssorm01', 'ORM01', 'SSORM01']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm02
- 最終 aliases: `['訂單副檔', 'ssorm02', 'ORM02', 'SSORM02']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm03
- 最終 aliases: `['訂單帳款副檔', 'ssorm03', 'ORM03', 'SSORM03']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm04
- 最終 aliases: `['訂單副檔', 'ssorm04', 'ORM04', 'SSORM04']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm05
- 最終 aliases: `['各產品網單同意記錄檔', 'ssorm05', 'ORM05', 'SSORM05']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm06
- 最終 aliases: `['訂單保險資料副檔', '航班資訊與投保明細', 'ssorm06', 'ORM06', 'SSORM06']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm07
- 最終 aliases: `['訂單業務自檢項目', 'ssorm07', 'ORM07', 'SSORM07']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm10
- 最終 aliases: `['訂單明細檔', 'ssorm10', 'SSORM10']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm11
- 最終 aliases: `['訂單明細副檔', 'ssorm11', 'ORM11', 'SSORM11']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm12
- 最終 aliases: `['訂單明細副檔', 'ssorm12', 'ORM12', 'SSORM12']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm13
- 最終 aliases: `['商務部旅客機票資料', 'ssorm13', 'ORM13', 'SSORM13']`
- 被黑名單剔除: `['訂單管理系統']`

### ssorm14
- 最終 aliases: `['商務部旅客機票航段資料', '哩程等明細', 'ssorm14', 'ORM14', 'SSORM14']`
- 被黑名單剔除: `['訂單管理系統']`

### tppcm00
- 最終 aliases: `['團體產品估價主檔', 'tppcm00', 'PCM00', 'TPPCM00']`
- 被黑名單剔除: `['團體估價系統']`

### tppcm09
- 最終 aliases: `['估價幣別匯率檔', 'tppcm09', 'PCM09', 'TPPCM09']`
- 被黑名單剔除: `['團體估價系統']`

### tppcm10
- 最終 aliases: `['估價明細成本檔', 'tppcm10', 'PCM10', 'TPPCM10']`
- 被黑名單剔除: `['團體估價系統']`

### tppcm20
- 最終 aliases: `['估價明細檔', 'tppcm20', 'PCM20', 'TPPCM20']`
- 被黑名單剔除: `['團體估價系統']`

### tppcm21
- 最終 aliases: `['估價明細暫存計算檔', '多幣別成本計算暫存檔', 'tppcm21', 'PCM21', 'TPPCM21']`
- 被黑名單剔除: `['團體估價系統']`

### tppcm30
- 最終 aliases: `['檔次估價成本主檔', 'tppcm30', 'PCM30', 'TPPCM30']`
- 被黑名單剔除: `['團體估價系統']`

### tppcm40
- 最終 aliases: `['檔次報價總表', 'tppcm40', 'PCM40', 'TPPCM40']`
- 被黑名單剔除: `['團體估價系統']`

### tppcm41
- 最終 aliases: `['檔次成本明細檔', 'tppcm41', 'PCM41', 'TPPCM41']`
- 被黑名單剔除: `['團體估價系統']`

### tppcm50
- 最終 aliases: `['估價單附件檔案管理表', 'tppcm50', 'PCM50', 'TPPCM50']`
- 被黑名單剔除: `['團體估價系統']`

### tppdm10
- 最終 aliases: `['團體主檔', 'tppdm10', 'PDM10', 'TPPDM10']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm11
- 最終 aliases: `['出團行程檔', 'tppdm11', 'PDM11', 'TPPDM11']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm12
- 最終 aliases: `['說明會副檔', 'tppdm12', 'PDM12', 'TPPDM12']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm13
- 最終 aliases: `['團體說明資料檔', 'tppdm13', 'PDM13', 'TPPDM13']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm14
- 最終 aliases: `['團體領隊建議核派名單檔', 'tppdm14', 'PDM14', 'TPPDM14']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm15
- 最終 aliases: `['團體活動節目關聯檔', 'tppdm15', 'PDM15', 'TPPDM15']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm16
- 最終 aliases: `['團體副檔', 'tppdm16', 'PDM16', 'TPPDM16']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm17
- 最終 aliases: `['團體關連檔', 'tppdm17', 'PDM17', 'TPPDM17']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm18
- 最終 aliases: `['團體預訂數量檔', 'tppdm18', 'PDM18', 'TPPDM18']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm19
- 最終 aliases: `['團體滿意度調查統計檔', '說明會相關', 'tppdm19', 'PDM19', 'TPPDM19']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm19a
- 最終 aliases: `['團體滿意度調查統計副檔', '說明會相關', 'tppdm19a', 'PDM19A', 'TPPDM19A']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm20
- 最終 aliases: `['團體行程代號主檔', 'tppdm20', 'PDM20', 'TPPDM20']`

### tppdm20_ez
- 最終 aliases: `['易遊行程主檔', 'tppdm20_ez', 'PDM20_EZ', 'TPPDM20_EZ']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm21
- 最終 aliases: `['日行程檔', 'tppdm21', 'PDM21', 'TPPDM21']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm21_ez
- 最終 aliases: `['易遊團體日行程檔', '易遊子系統', '易遊系統的日行程明細', 'tppdm21_ez', 'PDM21_EZ', 'TPPDM21_EZ']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm22
- 最終 aliases: `['自由行行程檔', 'tppdm22', 'PDM22', 'TPPDM22']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm23
- 最終 aliases: `['行程自費活動關聯檔', 'tppdm23', 'PDM23', 'TPPDM23']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm24
- 最終 aliases: `['團體日行程CTO資料檔', 'tppdm24', 'PDM24', 'TPPDM24']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm25
- 最終 aliases: `['團體行程副檔', 'tppdm25', 'PDM25', 'TPPDM25']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm25_ez
- 最終 aliases: `['易遊團體行程副檔', 'tppdm25_ez', 'PDM25_EZ', 'TPPDM25_EZ']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm26
- 最終 aliases: `['行程上下車地點關聯檔', 'tppdm26', 'PDM26', 'TPPDM26']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm27
- 最終 aliases: `['團體行程修改自動留言檔', 'tppdm27', 'PDM27', 'TPPDM27']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm30
- 最終 aliases: `['團體產品行程異動記錄檔', 'tppdm30', 'PDM30', 'TPPDM30']`

### tppdm36
- 最終 aliases: `['團體上下車地點關聯檔', 'tppdm36', 'PDM36', 'TPPDM36']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm40
- 最終 aliases: `['團體班機資料', 'tppdm40', 'PDM40', 'TPPDM40']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm41
- 最終 aliases: `['團體 PNR 資料', 'tppdm41', 'PDM41', 'TPPDM41']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm50
- 最終 aliases: `['出團旅館檔', 'tppdm50', 'PDM50', 'TPPDM50']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm55
- 最終 aliases: `['交付 B2P 供應商處理團', 'tppdm55', 'PDM55', 'TPPDM55']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm56
- 最終 aliases: `['供應商詳細欄位設定檔', 'tppdm56', 'PDM56', 'TPPDM56']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm57
- 最終 aliases: `['團詳細設定欄位', 'tppdm57', 'PDM57', 'TPPDM57']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm60
- 最終 aliases: `['郵輪團說明會資料檔', '郵輪相關', 'tppdm60', 'PDM60', 'TPPDM60']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm61
- 最終 aliases: `['郵輪接駁車', 'tppdm61', 'PDM61', 'TPPDM61']`
- 被黑名單剔除: `['團體產品管理', '郵輪子系統']`

### tppdm62
- 最終 aliases: `['郵輪岸上觀光主檔', 'tppdm62', 'PDM62', 'TPPDM62']`
- 被黑名單剔除: `['團體產品管理', '郵輪子系統']`

### tppdm63
- 最終 aliases: `['郵輪岸上觀光景點', 'tppdm63', 'PDM63', 'TPPDM63']`
- 被黑名單剔除: `['團體產品管理', '郵輪子系統']`

### tppdm64
- 最終 aliases: `['郵輪岸上觀光車次', 'tppdm64', 'PDM64', 'TPPDM64']`
- 被黑名單剔除: `['團體產品管理', '郵輪子系統']`

### tppdm65
- 最終 aliases: `['郵輪岸上觀光車次團體', 'tppdm65', 'PDM65', 'TPPDM65']`
- 被黑名單剔除: `['團體產品管理', '郵輪子系統']`

### tppdm66
- 最終 aliases: `['郵輪相關檔案', '岸上觀光訂單關聯', 'tppdm66', 'PDM66', 'TPPDM66']`
- 被黑名單剔除: `['團體產品管理', '郵輪子系統']`

### tppdm67
- 最終 aliases: `['團體郵輪設定', 'tppdm67', 'PDM67', 'TPPDM67']`
- 被黑名單剔除: `['團體產品管理', '郵輪子系統']`

### tppdm76
- 最終 aliases: `['團產品預設圖檔', 'tppdm76', 'PDM76', 'TPPDM76']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm81
- 最終 aliases: `['設定滑雪團各級教練人數', 'tppdm81', 'PDM81', 'TPPDM81']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm90
- 最終 aliases: `['團體售價資料檔', '團體的售價明細', 'tppdm90', 'PDM90', 'TPPDM90']`
- 被黑名單剔除: `['團體產品系統']`

### tppdm91
- 最終 aliases: `['產品分銷設定', 'tppdm91', 'PDM91', 'TPPDM91']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm92
- 最終 aliases: `['產品分銷上架設定', 'tppdm92', 'PDM92', 'TPPDM92']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm93
- 最終 aliases: `['多渠道自動上架設定', 'tppdm93', 'PDM93', 'TPPDM93']`
- 被黑名單剔除: `['團體產品管理']`

### tppdm98
- 最終 aliases: `['團多房價群組檔', 'tppdm98', 'PDM98', 'TPPDM98']`
- 被黑名單剔除: `['團體產品系統']`

### tptbm00
- 最終 aliases: `['標準團名資料檔', 'tptbm00', 'TPTBM00']`

### tptbm02
- 最終 aliases: `['標準團名關鍵字檔', 'tptbm02', 'TBM02', 'TPTBM02']`

### tptbm06
- 最終 aliases: `['標準團名標籤關聯檔', 'tptbm06', 'TBM06', 'TPTBM06']`

### tptbm09
- 最終 aliases: `['標準團名不發簡訊設定檔', 'tptbm09', 'TBM09', 'TPTBM09']`

### tptbm10
- 最終 aliases: `['團體銷售資訊說明檔', '注意事項主檔', '標準團名管理', 'tptbm10', 'TPTBM10']`

### tptbm11
- 最終 aliases: `['標準團名對應銷售資訊檔', 'tptbm11', 'TPTBM11']`

### tptbm15
- 最終 aliases: `['台灣說明會提醒文字', 'tptbm15', 'TBM15', 'TPTBM15']`

### tptbm20
- 最終 aliases: `['前台旅遊地區代碼檔', 'tptbm20', 'TPTBM20']`

### tptbm20_lang
- 最終 aliases: `['前台旅遊地區代碼多語系檔', 'tptbm20_lang', 'TBM20_LANG', 'TPTBM20_LANG']`

### tptbm30
- 最終 aliases: `['海外 FIT 票地區代碼檔', '標準團名管理', 'tptbm30', 'TBM30', 'TPTBM30']`

### tptbm31
- 最終 aliases: `['海外 FIT 票統計大類代碼檔', '標準團名管理', 'tptbm31', 'TBM31', 'TPTBM31']`

### tptrm20
- 最終 aliases: `['旅遊館', 'tptrm20', 'TRM20', 'TPTRM20']`

### tptrm21
- 最終 aliases: `['旅遊館常用證照項目', 'tptrm21', 'TRM21', 'TPTRM21']`

### tptrm22
- 最終 aliases: `['旅遊館對應旅遊地區代碼檔', 'tptrm22', 'TRM22', 'TPTRM22']`

### tptrm30
- 最終 aliases: `['旅遊館群組', 'tptrm30', 'TRM30', 'TPTRM30']`

### tptrm32
- 最終 aliases: `['旅遊館群組行程', 'tptrm32', 'TRM32', 'TPTRM32']`

### wtorm00
- 最終 aliases: `['訂位單主檔', '網位單管理系統', '網位單的主檔', 'wtorm00', 'WTORM00']`

### wtorm10
- 最終 aliases: `['訂位單旅客資料檔', '網位單管理系統', '費用明細', 'wtorm10', 'WTORM10']`

### wtorm20
- 最終 aliases: `['訂位單航段檔', '網位單管理系統', 'wtorm20', 'ORM20', 'WTORM20']`

### wtorm30
- 最終 aliases: `['訂房記錄檔', '網位單管理系統', '訂房子系統', '記錄訂位單的每日訂房明細', '為訂房訂單的核心明細檔', 'wtorm30', 'ORM30', 'WTORM30']`
