from sklearn.preprocessing import StandardScaler
 
# 스케일러 초기화 및 'Math_Score', 'Running_Time' 표준화 적용
scaler = StandardScaler()
data_standardized = data_example.copy()
data_standardized[['Math_Score', 'Running_Time']] = scaler.fit_transform(data_example[['Math_Score', 'Running_Time']])
 
# 시각화: 표준화 전후의 데이터 비교 및 결합
fig, ax = plt.subplots(3, 1, figsize=(10, 18))
 
# 1. 표준화 전 (별도 막대)
ax[0].bar(index - 0.2, data_example['Math_Score'], 0.4, label='Math Score', color='lightblue')
ax[0].bar(index + 0.2, data_example['Running_Time'], 0.4, label='Running Time', color='lightgreen')
# 2. 표준화 후 (별도 막대)
ax[1].bar(index - 0.2, data_standardized['Math_Score'], 0.4, label='Standardized Math Score', color='lightblue')
ax[1].bar(index + 0.2, data_standardized['Running_Time'], 0.4, label='Standardized Running Time', color='lightgreen')
# 3. 결합된 표준화 점수 막대
combined_scores = data_standardized['Math_Score'] + data_standardized['Running_Time']
ax[2].bar(index, combined_scores, bar_width, label='Combined Standardized Scores', color='lightcoral')

plt.show()
