# ==============================================================================
# 出版級高解析度圖表生成腳本 (Publication Figures Generator)
# ==============================================================================

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

out_dir = "manuscript/figures"
os.makedirs(out_dir, exist_ok=True)
print(f"正在輸出圖表至 {out_dir}...")

# ------------------------------------------------------------------------------
# 1. 第 1 章：模型彈性 vs 可解釋性權衡 (Flexibility vs Interpretability)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
models = [
    ("Subset Selection", 1.0, 9.0),
    ("Lasso / Ridge", 2.2, 8.0),
    ("Linear Regression", 2.0, 8.5),
    ("Logistic / GLM", 2.5, 7.8),
    ("GAM", 4.5, 6.0),
    ("Decision Trees", 5.0, 7.0),
    ("Bagging / RF", 7.5, 3.5),
    ("Boosting / XGB", 8.2, 3.0),
    ("SVM (RBF Kernel)", 8.0, 3.2),
    ("Deep Neural Nets", 9.5, 1.5)
]

for name, flex, interp in models:
    ax.scatter(flex, interp, color='#1f77b4', s=100, zorder=5)
    offset_y = 0.25 if interp > 5 else -0.35
    offset_x = 0.1
    if "Linear Regression" in name:
        offset_y = -0.4
    ax.text(flex + offset_x, interp + offset_y, name, fontsize=10, fontweight='bold', color='#333333')

ax.set_xlim(0, 11)
ax.set_ylim(0, 10.5)
ax.set_xlabel("Model Flexibility (Capacity / Degrees of Freedom)", fontsize=11, fontweight='bold')
ax.set_ylabel("Model Interpretability / Statistical Inference", fontsize=11, fontweight='bold')
ax.set_title("Figure 1.1: The Trade-off Between Flexibility and Interpretability", fontsize=12, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig01_flexibility_tradeoff.png"))
plt.close()
print("✓ 產生 fig01_flexibility_tradeoff.png")

# ------------------------------------------------------------------------------
# 2. 第 2 章：偏誤-變異數權衡分解曲線 (Bias-Variance Decomposition)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
flex = np.linspace(1, 10, 200)
bias_sq = 8.0 / (flex**1.1)
variance = 0.12 * (flex**1.85)
irr_error = np.full_like(flex, 1.5)
total_error = bias_sq + variance + irr_error

ax.plot(flex, bias_sq, label=r"Bias$^2$ (Model Underfitting)", color='#2ca02c', linewidth=2.5, linestyle='--')
ax.plot(flex, variance, label=r"Variance (Model Overfitting)", color='#d62728', linewidth=2.5, linestyle='-.')
ax.plot(flex, irr_error, label=r"Irreducible Error $\sigma_\epsilon^2$", color='#7f7f7f', linewidth=2.0, linestyle=':')
ax.plot(flex, total_error, label=r"Total Expected Test MSE", color='#1f77b4', linewidth=3.0)

min_idx = np.argmin(total_error)
ax.scatter(flex[min_idx], total_error[min_idx], color='#1f77b4', s=120, zorder=6)
ax.axvline(flex[min_idx], color='#1f77b4', linestyle=':', alpha=0.7)
ax.text(flex[min_idx] + 0.15, total_error[min_idx] + 0.3, "Optimal Flexibility\n(Minimum Test Error)", color='#1f77b4', fontweight='bold', fontsize=9)

ax.set_xlabel("Model Flexibility (Model Capacity)", fontsize=11, fontweight='bold')
ax.set_ylabel("Expected Mean Squared Error", fontsize=11, fontweight='bold')
ax.set_title("Figure 2.1: The Fundamental Bias-Variance Trade-off", fontsize=12, fontweight='bold', pad=12)
ax.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig02_bias_variance.png"))
plt.close()
print("✓ 產生 fig02_bias_variance.png")

# ------------------------------------------------------------------------------
# 3. 第 3 章：最小平方法幾何正交投影 (OLS Orthogonal Projection)
# ------------------------------------------------------------------------------
fig = plt.figure(figsize=(7, 6), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# 繪製列空間平面 C(X)
xx, yy = np.meshgrid(np.linspace(0, 4, 10), np.linspace(0, 4, 10))
zz = 0.2 * xx + 0.3 * yy
ax.plot_surface(xx, yy, zz, alpha=0.3, color='#aec7e8')

# 繪製向量
y_pt = np.array([2.0, 2.5, 3.8])
y_hat = np.array([2.0, 2.5, 0.2*2.0 + 0.3*2.5]) # 正交投影點

ax.quiver(0, 0, 0, y_pt[0], y_pt[1], y_pt[2], color='#d62728', arrow_length_ratio=0.08, linewidth=2.5, label=r'Observation vector $\mathbf{y}$')
ax.quiver(0, 0, 0, y_hat[0], y_hat[1], y_hat[2], color='#1f77b4', arrow_length_ratio=0.08, linewidth=2.5, label=r'Fitted vector $\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}$')
ax.plot([y_hat[0], y_pt[0]], [y_hat[1], y_pt[1]], [y_hat[2], y_pt[2]], color='#2ca02c', linewidth=2.0, linestyle='--', label=r'Residual vector $\mathbf{e} = (\mathbf{I}-\mathbf{H})\mathbf{y}$')

ax.set_xlabel('X1 Axis')
ax.set_ylabel('X2 Axis')
ax.set_zlabel('Y Dimension')
ax.set_title("Figure 3.1: Geometric Orthogonal Projection in OLS", fontsize=11, fontweight='bold', pad=12)
ax.legend(loc='upper left', fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig03_ols_projection.png"))
plt.close()
print("✓ 產生 fig03_ols_projection.png")

# ------------------------------------------------------------------------------
# 4. 第 4 章：Lasso vs Ridge 幾何等高線切點 (L1 vs L2 Geometry)
# ------------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5), dpi=300)

b1, b2 = np.meshgrid(np.linspace(-2.5, 3.5, 300), np.linspace(-2.5, 3.5, 300))
# OLS 橢圓形損失等高線，中心位於 (2.0, 1.5)
Z = 1.8 * (b1 - 2.0)**2 + 0.8 * (b2 - 1.5)**2 + 1.2 * (b1 - 2.0) * (b2 - 1.5)

# Lasso L1 菱形: |b1| + |b2| <= 1.0
t_lasso = 1.0
diamond_x = [t_lasso, 0, -t_lasso, 0, t_lasso]
diamond_y = [0, t_lasso, 0, -t_lasso, 0]
ax1.plot(diamond_x, diamond_y, color='#d62728', linewidth=2.5, label=r'L1 Constraint: $|\beta_1| + |\beta_2| \leq t$')
ax1.fill(diamond_x, diamond_y, color='#ff9896', alpha=0.3)
cs1 = ax1.contour(b1, b2, Z, levels=[0.5, 1.2, 2.2, 3.8, 6.0], colors='#1f77b4', linewidths=1.5)
ax1.scatter([0], [1.0], color='#d62728', s=100, zorder=10)
ax1.text(0.1, 1.15, r'Corner Touch point ($\beta_1=0$, Sparse!)', color='#d62728', fontweight='bold', fontsize=9)
ax1.scatter([2.0], [1.5], color='#1f77b4', marker='x', s=100, linewidth=2, label=r'Unconstrained OLS $\hat{\beta}$')
ax1.axhline(0, color='gray', linestyle=':', alpha=0.7)
ax1.axvline(0, color='gray', linestyle=':', alpha=0.7)
ax1.set_xlim(-2, 3.5); ax1.set_ylim(-2, 3)
ax1.set_xlabel(r'$\beta_1$', fontsize=11, fontweight='bold'); ax1.set_ylabel(r'$\beta_2$', fontsize=11, fontweight='bold')
ax1.set_title("Lasso (L1 Regularization): Sparse Solution", fontsize=11, fontweight='bold')
ax1.legend(loc='lower left', fontsize=8)

# Ridge L2 圓形: b1^2 + b2^2 <= s
theta = np.linspace(0, 2*np.pi, 200)
r_ridge = 1.1
circle_x = r_ridge * np.cos(theta)
circle_y = r_ridge * np.sin(theta)
ax2.plot(circle_x, circle_y, color='#2ca02c', linewidth=2.5, label=r'L2 Constraint: $\beta_1^2 + \beta_2^2 \leq s$')
ax2.fill(circle_x, circle_y, color='#98df8a', alpha=0.3)
cs2 = ax2.contour(b1, b2, Z, levels=[0.5, 1.2, 2.2, 3.8, 6.0], colors='#1f77b4', linewidths=1.5)
# 切點在圓弧上
touch_x, touch_y = 0.85, 0.7
ax2.scatter([touch_x], [touch_y], color='#2ca02c', s=100, zorder=10)
ax2.text(touch_x + 0.1, touch_y + 0.15, r'Smooth Touch point ($\beta_1 \neq 0, \beta_2 \neq 0$)', color='#2ca02c', fontweight='bold', fontsize=9)
ax2.scatter([2.0], [1.5], color='#1f77b4', marker='x', s=100, linewidth=2, label=r'Unconstrained OLS $\hat{\beta}$')
ax2.axhline(0, color='gray', linestyle=':', alpha=0.7)
ax2.axvline(0, color='gray', linestyle=':', alpha=0.7)
ax2.set_xlim(-2, 3.5); ax2.set_ylim(-2, 3)
ax2.set_xlabel(r'$\beta_1$', fontsize=11, fontweight='bold'); ax2.set_ylabel(r'$\beta_2$', fontsize=11, fontweight='bold')
ax2.set_title("Ridge (L2 Regularization): Shrinkage Solution", fontsize=11, fontweight='bold')
ax2.legend(loc='lower left', fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig04_lasso_ridge_geometry.png"))
plt.close()
print("✓ 產生 fig04_lasso_ridge_geometry.png")

# ------------------------------------------------------------------------------
# 5. 第 8 章：支援向量機最大間距幾何 (SVM Margin & Support Vectors)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 6), dpi=300)
np.random.seed(42)
# 生成兩類點
x_pos = np.array([[1.5, 3.2], [2.2, 4.0], [1.0, 4.5], [2.8, 3.8], [2.0, 2.5]])
x_neg = np.array([[3.2, 1.5], [4.0, 2.2], [4.5, 1.0], [3.8, 2.8], [4.8, 2.0]])

ax.scatter(x_pos[:, 0], x_pos[:, 1], color='#1f77b4', s=80, marker='o', label=r'Positive Class ($y_i = +1$)')
ax.scatter(x_neg[:, 0], x_neg[:, 1], color='#d62728', s=80, marker='s', label=r'Negative Class ($y_i = -1$)')

# 分離超平面 w1*x1 + w2*x2 + b = 0 -> x2 = -x1 + 4.6
x_line = np.linspace(0.5, 5.0, 100)
ax.plot(x_line, -x_line + 4.8, color='black', linewidth=2.5, label=r'Separating Hyperplane: $\mathbf{w}^\top\mathbf{x} + b = 0$')
ax.plot(x_line, -x_line + 5.5, color='#d62728', linestyle='--', linewidth=1.8, label=r'Negative Margin: $\mathbf{w}^\top\mathbf{x} + b = -1$')
ax.plot(x_line, -x_line + 4.1, color='#1f77b4', linestyle='--', linewidth=1.8, label=r'Positive Margin: $\mathbf{w}^\top\mathbf{x} + b = +1$')

# 標註支援向量
svs = np.array([[2.0, 2.5], [1.5, 3.2], [3.2, 1.5], [4.0, 2.2]])
ax.scatter(svs[:, 0], svs[:, 1], s=250, facecolors='none', edgecolors='gold', linewidths=3, label='Support Vectors (Non-zero $\\alpha_i$)')

ax.set_xlim(0.5, 5.2); ax.set_ylim(0.5, 5.2)
ax.set_xlabel(r'$X_1$', fontsize=11, fontweight='bold'); ax.set_ylabel(r'$X_2$', fontsize=11, fontweight='bold')
ax.set_title("Figure 8.1: Max-Margin Separation and Support Vectors in SVM", fontsize=11, fontweight='bold', pad=12)
ax.legend(loc='lower left', fontsize=8.5)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig08_svm_margin.png"))
plt.close()
print("✓ 產生 fig08_svm_margin.png")

# ------------------------------------------------------------------------------
# 6. 第 13 章：現代雙重下降現象 (Double Descent Curve)
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
p_over_n = np.linspace(0.1, 3.0, 400)

# 構造雙重下降曲線
test_risk = []
train_risk = []
for p in p_over_n:
    if p < 1.0:
        # 古典區間: U型，在接近 1 時方差爆炸
        tr = max(0.0, 1.0 - p)
        vr = 0.2 + 0.15 / ((1.0 - p + 0.05)**1.2)
    else:
        # 過度參數化區間: 訓練誤差為0，測試誤差再次下降
        tr = 0.0
        vr = 0.2 + 0.25 / ((p - 1.0 + 0.15)**0.9)
    train_risk.append(tr)
    test_risk.append(vr)

ax.plot(p_over_n, test_risk, color='#d62728', linewidth=3.0, label='Test Risk (Double Descent)')
ax.plot(p_over_n, train_risk, color='#1f77b4', linewidth=2.0, linestyle='--', label='Training Risk (Zero after p=n)')

ax.axvline(1.0, color='gray', linestyle=':', linewidth=2.0)
ax.text(1.02, 2.5, "Interpolation Threshold\n(p = n, Variance Explosion)", color='#555555', fontsize=9, fontweight='bold')

ax.annotate("Classical Under-parameterized\nRegime (U-shaped)", xy=(0.4, 0.9), xytext=(0.2, 1.8),
            arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6), fontweight='bold', fontsize=8.5)

ax.annotate("Modern Over-parameterized\nRegime (Benign Overfitting)", xy=(2.2, 0.45), xytext=(1.8, 1.4),
            arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6), fontweight='bold', fontsize=8.5)

ax.set_ylim(-0.1, 3.5)
ax.set_xlabel(r"Model Parameter Capacity / Sample Size ($p / n$)", fontsize=11, fontweight='bold')
ax.set_ylabel("Risk / Prediction Error", fontsize=11, fontweight='bold')
ax.set_title("Figure 13.1: The Modern Double Descent Phenomenon in Deep Learning", fontsize=12, fontweight='bold', pad=12)
ax.legend(loc='upper right', frameon=True, fontsize=9.5)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "fig13_double_descent.png"))
plt.close()
print("✓ 產生 fig13_double_descent.png")

print("全部出版級圖表生成完畢！")
