from sklearn.preprocessing import MinMaxScaler
 
# Min-Max 스케일러 초기화 및 'Math_Score', 'Running_Time'에 적용
scaler_minmax = MinMaxScaler()
data_normalized = data_example.copy()
data_normalized[['Math_Score', 'Running_Time']] = scaler_minmax.fit_transform(data_example[['Math_Score', 'Running_Time']])
 
# 시각화: 정규화 전후 데이터 비교 및 결합
fig, ax = plt.subplots(3, 1, figsize=(10, 18))
 
# 1. 정규화 전
ax[0].bar(index - 0.2, data_example['Math_Score'], 0.4, label='Math Score', color='lightblue')
ax[0].bar(index + 0.2, data_example['Running_Time'], 0.4, label='Running Time', color='lightgreen')
 
# 2. 정규화 후
ax[1].bar(index - 0.2, data_normalized['Math_Score'], 0.4, label='Normalized Math Score', color='lightblue')
ax[1].bar(index + 0.2, data_normalized['Running_Time'], 0.4, label='Normalized Running Time', color='lightgreen')
 
# 3. 결합된 정규화 점수 막대
combined_normalized_scores = data_normalized['Math_Score'] + data_normalized['Running_Time']
ax[2].bar(index, combined_normalized_scores, bar_width, label='Combined Normalized Scores', color='lightcoral')
 
plt.show()
