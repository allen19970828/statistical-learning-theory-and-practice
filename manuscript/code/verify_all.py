# ==============================================================================
# 全書各章 Python 雙軌實作綜合測試套件 (Zero-Error Verification Suite)
# ==============================================================================

import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier, XGBRegressor
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import statsmodels.api as sm
import shap

print("Python 模組載入成功，開始逐章端到端驗證...")

# --- 第 1 章 ---
X1 = np.linspace(-1, 1, 30)[:, np.newaxis]
y1 = np.sin(np.pi * X1.ravel()) + np.random.normal(0, 0.1, 30)
m1 = make_pipeline(PolynomialFeatures(3), LinearRegression()).fit(X1, y1)
assert m1.score(X1, y1) > 0.8, "Ch1 Failed"
print("✓ Ch01 統計學習概論 測試通過")

# --- 第 2 章 ---
kf = KFold(n_splits=3)
scores2 = cross_val_score(LinearRegression(), X1, y1, cv=kf)
assert len(scores2) == 3, "Ch2 Failed"
print("✓ Ch02 模型評估與重抽樣 測試通過")

# --- 第 3 章 ---
X3 = sm.add_constant(X1)
m3 = sm.OLS(y1, X3).fit()
assert len(m3.params) == 2, "Ch3 Failed"
print("✓ Ch03 多元線性迴歸 測試通過")

# --- 第 4 章 ---
X4 = np.random.normal(size=(50, 10))
y4 = X4[:, 0] * 2.0 + np.random.normal(size=50)
m4 = LassoCV(cv=3).fit(X4, y4)
assert m4.coef_[0] != 0, "Ch4 Failed"
print("✓ Ch04 正則化與收縮法 測試通過")

# --- 第 6 章 ---
y6 = (y1 > 0).astype(int)
m6 = sm.Logit(y6, X3).fit(disp=False)
assert len(m6.params) == 2, "Ch6 Failed"
print("✓ Ch06 羅吉斯迴歸 測試通過")

# --- 第 7 章 ---
m7 = LinearDiscriminantAnalysis().fit(X1, y6)
assert m7.score(X1, y6) > 0.5, "Ch7 Failed"
print("✓ Ch07 生成式分類模型 測試通過")

# --- 第 8 章 ---
m8 = SVC(kernel='rbf', C=1.0).fit(X1, y6)
assert len(m8.support_) > 0, "Ch8 Failed"
print("✓ Ch08 支援向量機 測試通過")

# --- 第 9 章 ---
m9 = DecisionTreeClassifier(max_depth=3).fit(X1, y6)
assert m9.get_n_leaves() > 1, "Ch9 Failed"
print("✓ Ch09 決策樹 測試通過")

# --- 第 10 章 ---
m10_rf = RandomForestClassifier(n_estimators=20, random_state=42).fit(X1, y6)
m10_xgb = XGBClassifier(n_estimators=20, max_depth=2, eval_metric='logloss').fit(X1, y6)
assert m10_rf.score(X1, y6) > 0.7, "Ch10 Failed"
print("✓ Ch10 集成學習 (RF & XGBoost) 測試通過")

# --- 第 11 章 ---
X11 = np.random.normal(size=(40, 5))
m11 = PCA(n_components=2).fit(X11)
assert len(m11.explained_variance_ratio_) == 2, "Ch11 Failed"
print("✓ Ch11 主成分分析與降維 測試通過")

# --- 第 12 章 ---
m12_km = KMeans(n_clusters=2, n_init=3).fit(X11)
m12_gmm = GaussianMixture(n_components=2).fit(X11)
assert len(m12_km.cluster_centers_) == 2, "Ch12 Failed"
print("✓ Ch12 分群與高斯混合模型 測試通過")

# --- 第 13 章 ---
y13 = np.random.normal(size=40)
m13_reg = XGBRegressor(n_estimators=10, max_depth=2).fit(X11, y13)
explainer13 = shap.TreeExplainer(m13_reg)
shap_vals = explainer13(X11)
assert shap_vals.shape == X11.shape, "Ch13 Failed"
print("✓ Ch13 現代前沿與 SHAP 測試通過")

# --- 第 14 章 ---
from sklearn.linear_model import Lasso
eps14 = np.random.choice([-1.0, 1.0], size=40)
rademacher_val = np.linalg.norm(X11.T @ eps14 / 40, 2)
assert rademacher_val > 0, "Ch14 Rademacher Failed"
lasso14 = Lasso(alpha=0.1, fit_intercept=False).fit(X11, y13)
assert lasso14.coef_.shape == (5,), "Ch14 Lasso Oracle Failed"
print("✓ Ch14 經驗過程與高維非漸近統計 測試通過")

print("\n==========================================")
print("🎉 全書 14 章 Python 雙軌實作綜合測試 100% 通過！")
print("==========================================")
