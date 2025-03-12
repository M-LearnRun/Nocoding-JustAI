# 데이터 전처리: 필요 컬럼 선택 및 이름 정리
data_new.rename(columns={"연봉(2018)\t": "연봉(2018)"}, inplace=True)
data_for_plot = data_new[['출루율', '연봉(2018)']].dropna()
 
# 연봉(2018) 컬럼을 로그 변환
data_for_plot = data_for_plot[data_for_plot['연봉(2018)'] > 0]
data_for_plot['log_salary'] = np.log(data_for_plot['연봉(2018)'])
 
# 데이터 스케일링
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_for_plot[['출루율', 'log_salary']])
 
# KMeans 클러스터링
kmeans = KMeans(n_clusters=4, random_state=42)
data_for_plot['cluster'] = kmeans.fit_predict(scaled_data)
 
# 클러스터 색상 정의
cluster_colors = {0: 'green', 1: 'red', 2: 'blue', 3: 'purple'}
data_for_plot['color'] = data_for_plot['cluster'].map(cluster_colors)
 
# 그래프 그리기
plt.figure(figsize=(10, 6))
for cluster_id, color in cluster_colors.items():
    cluster_data = data_for_plot[data_for_plot['cluster'] == cluster_id]
    plt.scatter(cluster_data['출루율'], cluster_data['log_salary'], c=color, label=f'Cluster {cluster_id}', alpha=0.6)
 
# 평균값 기준선 추가
plt.axvline(data_for_plot['출루율'].mean(), color='black', linestyle='--', label='평균 출루율')
plt.axhline(data_for_plot['log_salary'].mean(), color='gray', linestyle='--', label='평균 로그 연봉')
 
# 그래프 제목과 축 설정
plt.title('출루율과 로그 변환된 연봉(최근) 기반 군집화', fontsize=14)
plt.xlabel('출루율', fontsize=12)
plt.ylabel('로그 변환 연봉 (만원)', fontsize=12)
plt.legend(title='Cluster')
plt.grid(True)
plt.show()
