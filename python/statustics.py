import scipy.stats as stats

# サンプルサイズと視聴率の設定
n = 500
observed_rate = 0.15

# 帰無仮説の下での期待値
expected_rate = 0.20

# 標準誤差の計算
standard_error = (expected_rate * (1 - expected_rate) / n) ** 0.5

# Zスコアの計算
z_score = (observed_rate - expected_rate) / standard_error

# 両側検定の場合、有意水準を0.05とした場合の臨界値
alpha = 0.05
critical_value = stats.norm.ppf(1 - alpha / 2)

# Zスコアと臨界値の比較
if abs(z_score) > critical_value:
    result = "帰無仮説を棄却します"
else:
    result = "帰無仮説を採択します"

print(f"Zスコア: {z_score}")
print(f"臨界値: {critical_value}")
print(f"結果: {result}")
