import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

n = np.array([61, 85, 75, 86, 64, 96, 87, 93, 67, 97, 77, 88, 90, 84, 65, 71, 69, 66, 98, 72])
x_i = np.array([4, 3, 2, 4, 2, 4, 5, 3, 6, 7, 6, 5, 8, 5, 5, 3, 3, 4, 5, 8])
p_hat = np.sum(x_i) / np.sum(n)
p_hat


ucl = p_hat + 3 * np.sqrt(p_hat * (1 - p_hat) / n)
lcl = p_hat - 3 * np.sqrt(p_hat * (1 - p_hat) / n)



day_i = np.arange(1, 21)
p_i = x_i / n
df = pd.DataFrame({
    "Day": day_i,
    "Defective Rate": p_i,
    "UCL": ucl,
    "LCL": lcl,
    "Ave. Rate": [p_hat] * 20
})
sns.lineplot(x="Day", y="Defective Rate", data=df, marker="o", label="Defective Rate")
sns.lineplot(x="Day", y="UCL", data=df, color='red', label="UCL")
sns.lineplot(x="Day", y="LCL", data=df, color='red', label="LCL")
sns.lineplot(x="Day", y="Ave. Rate", data=df, color='black', linestyle='--', label="Ave. Rate")
plt.fill_between(df["Day"], df["LCL"], df["UCL"], color='red', alpha=0.1)
plt.title('P chart')
plt.ylabel('Defective Rate')
plt.legend(loc="lower right")
plt.show()



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
# 각 소집단에 대한 측정값 5개씩 (n=5, k=10)
data = np.array([
    [10.487, 9.816, 9.842, 9.678, 10.260],
    [9.310, 10.523, 9.772, 10.096, 9.925],
    [10.439, 9.382, 9.903, 9.885, 10.340],
    [9.670, 9.948, 9.737, 10.013, 10.175],
    [9.670, 10.343, 10.270, 10.151, 10.270],
    [9.795, 9.963, 9.719, 9.920, 10.159],
    [9.793, 9.881, 9.794, 9.746, 9.799],
    [9.996, 9.665, 10.070, 10.498, 10.223],
    [9.942, 9.734, 9.776, 10.508, 10.015],
    [9.809, 10.057, 10.630, 10.036, 10.185]
])
n = data.shape[1]   # 소집단 크기
k = data.shape[0]   # 소집단 수
# pandas DataFrame으로 변환
columns = [f'x{i+1}' for i in range(n)]
df = pd.DataFrame(data, columns=columns)
df.insert(0, 'subgroup', np.arange(1, k+1))
# 각 소집단별 평균과 범위 계산
df['xbar_i'] = df[columns].mean(axis=1)
df['R_i'] = df[columns].max(axis=1) - df[columns].min(axis=1)
print("평균 및 범위 계산 결과:")
print(df[['subgroup', 'xbar_i', 'R_i']], '\n')
# 평균의 평균(Grand Mean)과 범위의 평균(Rbar)
xbarbar = df['xbar_i'].mean()
Rbar = df['R_i'].mean()
print(f"Grand Mean (x̄̄): {xbarbar:.4f}")
print(f"Average Range (R̄): {Rbar:.4f}\n")
# 관리도 상수 (n=5)
A2, D3, D4 = 0.577, 0.000, 2.115
# 관리한계 계산
UCLx = xbarbar + A2 * Rbar
LCLx = xbarbar - A2 * Rbar
UCLr = D4 * Rbar
LCLr = D3 * Rbar
print("관리한계:")
print(f"Xbar 관리도 → UCL: {UCLx:.4f}, CL: {xbarbar:.4f}, LCL: {LCLx:.4f}")
print(f"R 관리도   → UCL: {UCLr:.4f}, CL: {Rbar:.4f}, LCL: {LCLr:.4f}\n")
summary = df[['subgroup', 'xbar_i', 'R_i']].copy()
print("요약:")
print(summary.round(3), '\n')


import seaborn as sns
fig, axes = plt.subplots(2, 1, figsize=(9, 9), sharex=True)
sns.lineplot(ax=axes[0], x="subgroup", y="xbar_i", data=df, marker="o")
axes[0].axhline(UCLx, linestyle="--", color="red", label="UCL")
axes[0].axhline(xbarbar, linestyle="-", color="black", label="CL")
axes[0].axhline(LCLx, linestyle="--", color="red", label="LCL")
axes[0].set_title("X-bar Control Chart")
axes[0].set_ylabel("Subgroup Mean ($\\bar{X}$)")
axes[0].legend(loc="upper right")
sns.lineplot(ax=axes[1], x="subgroup", y="R_i", data=df, marker="o", color="orange")
axes[1].axhline(UCLr, linestyle="--", color="red", label="UCL")
axes[1].axhline(Rbar, linestyle="-", color="black", label="CL")
axes[1].axhline(LCLr, linestyle="--", color="red", label="LCL")
axes[1].set_title("R Control Chart")
axes[1].set_xlabel("Subgroup")
axes[1].set_ylabel("Range ($R$)")
axes[1].legend(loc="upper right")
plt.tight_layout()
plt.show()