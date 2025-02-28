# [모델 성능 시각화 코드]
import matplotlib.pyplot as plt
 
# 모델과 성능 데이터
models = performance_df_all['Model']
mse_values = performance_df_all['MSE']
r2_values = performance_df_all['R^2']
# MSE 비교 플롯
plt.figure(figsize=(10, 6))
plt.bar(models, mse_values, color='skyblue')
plt.show()
# R² 비교 플롯
plt.figure(figsize=(10, 6))
plt.bar(models, r2_values, color='lightgreen')
plt.show()
