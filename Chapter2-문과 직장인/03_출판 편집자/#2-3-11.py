mean_value = data['세일즈포인트'].mean()
median_value = data['세일즈포인트'].median()
 
# 세일즈포인트 분포를 시각화하고 평균과 중앙값을 버티컬 라인으로 표기
plt.figure(figsize=(10, 6))
plt.hist(data['세일즈포인트'].dropna(), bins=50, edgecolor='black', alpha=0.7)
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'평균: {mean_value:.2f}')ins 수를 50으로 늘려 세일즈포인트 분포를 더 세밀하게 시각화
plt.axvline(median_value, color='blue', linestyle='dashed', linewidth=2, label=f'중앙값: {median_value:.2f}')
