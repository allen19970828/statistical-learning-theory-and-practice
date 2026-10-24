# 統計學習理論與實務：深入淺出指南
### Statistical Learning: Theory and Practice — An In-Depth Dual-Track Guide

[![Quarto Publish](https://github.com/allen19970828/statistical-learning-theory-and-practice/actions/workflows/quarto-publish.yml/badge.svg)](https://github.com/allen19970828/statistical-learning-theory-and-practice/actions/workflows/quarto-publish.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![R: >=4.2.0](https://img.shields.io/badge/R-%3E%3D4.2.0-blue.svg)](https://www.r-project.org/)
[![Python: >=3.10](https://img.shields.io/badge/Python-%3E%3D3.10-blue.svg)](https://www.python.org/)
[![Quarto](https://img.shields.io/badge/Rendered%20with-Quarto-447099.svg)](https://quarto.org/)

> **📖 線上閱讀專書**：[https://allen19970828.github.io/statistical-learning-theory-and-practice/](https://allen19970828.github.io/statistical-learning-theory-and-practice/)

---

## 🎯 寫作緣起與使命

在當前人工智慧與資料科學蓬勃發展的浪潮中，「機器學習」已成為各學科競相修習的核心領域。然而，長期以來，大專院校師生與自學專業人士在中文教材的選擇上面臨著顯著的結構性斷層：

1. **頂尖西方原著**（如 *ISLR/ISLP* 與 *ESL*）為維持通俗性，經常略去關鍵矩陣推導與演算法收斂證明。
2. **海峽兩岸現有文獻**（如李航《統計學習方法》、周志華《機器學習》）理論嚴謹但缺乏可執行的實體程式碼，且術語常有兩岸習慣差異。
3. **商業技術書籍**則過度偏重套件 API 呼叫（純粹 `model.fit()`），缺乏假設檢定條件、殘差診斷與泛化理論的深度探討。

本書立足於當代十部經典文獻與演算法原創奠基論文的肩膀上，為繁體中文讀者打造一部**「既有嚴格數學推導、又有深刻統計直觀、更能透過 R 與 Python 雙軌程式落地實戰」**的出版級專書。

---

## 🌟 本書三大核心支柱

1. **理論推導不妥協，杜絕黑盒子**：
   * Gauss-Markov 定理（BLUE 最佳線性無偏估計量）嚴格矩陣證明。
   * 偏誤-變異數權衡（Bias-Variance Decomposition）期望誤差六項展開。
   * Lasso 軟閾值座標下降法（Coordinate Descent）次梯度解析推導。
   * 支援向量機（SVM）拉格朗日對偶問題、KKT 互補鬆弛條件與 SMO 演算法推導。
   * AdaBoost 指數損失函數最小化與樣本重權重更新證明。
   * 高斯混合模型（GMM）基於 Jensen 不等式之證據下界（ELBO）與 EM 閉式解推導。
2. **R 語言與 Python 雙軌實戰對照（Dual-Track）**：
   * 打破「統計系用 R，資工/業界用 Python」的壁壘。
   * 全書 13 章同步提供現代 R（Tidyverse、`glmnet`、`e1071`、`randomForest`、`mgcv`）與標準 Python（`numpy`、`scipy`、`scikit-learn`、`statsmodels`、`xgboost`、`shap`）完整實體程式碼。
3. **臺灣教育部審定標準統計術語**：
   * 嚴格規範專業名詞（如「迴歸」、「殘差」、「過度配適」、「穩健」、「支援向量機」、「交叉驗證」、「單純貝氏」等），內附完整三欄中英術語對照表。

---

## 📚 全書章節目錄與架構地圖

| 篇章分類 | 章節名稱 | 核心理論證明 | 數值推演範例 | 程式實踐亮點 |
| :--- | :--- | :--- | :--- | :--- |
| **第一篇：基礎理論與評估** | [第 1 章：統計學習概論與思維典範](manuscript/chapters/ch01_introduction.qmd) | 沒有免費午餐定理 (NFL)、可約化與不可約化誤差 | 維度災難幾何收縮推算 | 模型彈性 vs 可解釋性權衡實驗 |
| | [第 2 章：模型評估、重抽樣與理論](manuscript/chapters/ch02_model_assessment.qmd) | 偏誤-變異數分解、LOOCV 槓桿捷徑定理、OOB 36.8% 極限 | 5 筆樣本槓桿值與 LOOCV 手算 | 手刻 LOOCV 捷徑 vs 套件驗證 |
| **第二篇：線性模型與正則化** | [第 3 章：多元線性迴歸與古典推論](manuscript/chapters/ch03_linear_regression.qmd) | Gauss-Markov 定理 (BLUE)、幾何正交投影 | 4 筆 2D 樣本正規方程與 $SE(\hat{\beta})$ | 報表全字段解讀與異變異數診斷 |
| | [第 4 章：正則化技術與高維特徵篩選](manuscript/chapters/ch04_regularization.qmd) | Lasso 次梯度與軟閾值算子、SVD 有效自由度 | 單變量 Ridge vs Lasso 收縮率手算 | 座標下降演算法手刻與 glmnet |
| **第三篇：非線性與分類模型** | [第 5 章：非線性模型與平滑技術](manuscript/chapters/ch05_splines_gam.qmd) | 截斷冪次基底、Reinsch 變分定理、Backfitting | 4 筆樣本單節點分段仿樣聯立方程求解 | 自然三次仿樣與 mgcv GAM 擬合 |
| | [第 6 章：羅吉斯迴歸與廣義線性模型](manuscript/chapters/ch06_logistic_glm.qmd) | 對數似然嚴格凹性、Deviance 與 LRT 檢定 | 4 筆樣本 IRLS 首步加權最小平方手算 | 手刻 IRLS 演算法與勝算比解讀 |
| | [第 7 章：生成式分類模型](manuscript/chapters/ch07_generative_models.qmd) | Fisher 投影極大化廣義瑞利商、LDA 高斯邊界 | 4 筆 2D 樣本合併共變異數逆矩陣求解 | LDA / QDA / 單純貝氏決策邊界 |
| | [第 8 章：支援向量機與核方法](manuscript/chapters/ch08_svm.qmd) | Wolfe 對偶、KKT 條件、RBF 核無限維映射 | 3 筆樣本手算 Gram 矩陣與對偶變數 $\alpha$ | 手刻線性 SVM 對偶 QP 與 e1071 |
| **第四篇：樹模型與集成學習** | [第 9 章：決策樹演算法](manuscript/chapters/ch09_decision_trees.qmd) | 吉尼不純度與交叉熵嚴格凹性、弱連接剪枝 | 6 筆樣本窮舉候選切分點吉尼增益表 | 成本-複雜度剪枝路徑 (ccp_alpha) |
| | [第 10 章：集成學習理論](manuscript/chapters/ch10_ensemble_learning.qmd) | AdaBoost 指數損失最小化、XGBoost 二階泰勒展開 | 10 筆樣本手推兩輪 AdaBoost 樣本權重 | 隨機森林 OOB 評估與 XGBoost |
| **第五篇：非監督學習** | [第 11 章：主成分分析與流形學習](manuscript/chapters/ch11_pca_manifold.qmd) | 最大投影方差 vs 最小重建誤差、SVD 對偶性 | 3 筆 2D 樣本手算共變異數特徵值 $\lambda$ | PCA 解釋變異數比例 vs t-SNE |
| | [第 12 章：分群演算法與混合模型](manuscript/chapters/ch12_clustering_em.qmd) | Lloyd 單調收斂性、GMM ELBO 下界與 M-步閉式解 | 4 筆 K-Means 迭代與 2 筆 GMM EM 手算 | 輪廓係數分析與 GMM 軟分群 |
| **第六篇：現代前沿** | [第 13 章：現代前沿：深度學習與 XAI](manuscript/chapters/ch13_modern_frontiers.qmd) | 雙重下降機制、共變量偏移加權、Shapley 唯一公理 | 6 假設 BH 程序臨界線與 Shapley 手算 | FDR 逐步校正與 TreeSHAP 歸因 |

---

## 🛠️ 雙軌驗證套件（Zero-Error Delivery）

為保證書中所有演算法與程式碼具備 100% 可重現性，本專案提供端到端自動化驗證套件：

### 1. Python 驗證測試
```bash
python3 manuscript/code/verify_all.py
```
*涵蓋全書 13 章端到端回歸模型、正則化路徑、IRLS、LDA、SVM、隨機森林、XGBoost、PCA、K-Means、GMM 與 SHAP 測試。*

### 2. R 語言驗證測試
```bash
Rscript manuscript/code/verify_all.R
```
*涵蓋 `ISLR2`、`boot`、`car`、`glmnet`、`splines`、`mgcv`、`MASS`、`e1071`、`rpart`、`randomForest`、`xgboost`、`cluster` 與 `Rtsne` 測試。*

---

## 💻 本地 Quarto 專書預覽與編譯

本專案基於現代 Quarto Book 引擎架構：

```bash
cd manuscript

# 1. 本地即時預覽 (Live-Reloading Preview)
quarto preview

# 2. 編譯為完整靜態 HTML 網頁專書 (輸出至 _book/ 目錄)
quarto render --to html

# 3. 編譯為出版級 PDF 電子書 (需安裝 TinyTeX 或 XeLaTeX)
quarto render --to pdf
```

---

## 📜 授權協議

本專案程式碼與教學文稿採用 [MIT 授權條款](LICENSE) 開源發布，歡迎學術研究、課程教學與自學社群廣泛轉載引用。

**作者**：梁成瑜 (AllenYU) 與 Antigravity 創作團隊  
*2026 年 10 月*
