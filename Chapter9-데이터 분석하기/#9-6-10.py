import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import koreanize_matplotlib  # 한글 지원 패키지
 
# 1. 데이터 전처리
# 출루율과 로그 연봉 계산
data['log_salary'] = np.log(data['연봉(2018)'])  # 연봉의 로그 변환
data = data.dropna(subset=['출루율', 'log_salary', '경기'])  # 필요한 열의 결측값 제거
 
# 2. 필터링
# 출루율 하위 10% 필터링
threshold_obp = data['출루율'].quantile(0.10)
data = data[data['출루율'] > threshold_obp]
 
# 경기 수 하위 25% 필터링
threshold_games = data['경기'].quantile(0.25)
data = data[data['경기'] > threshold_games]
 
# 3. 군집화 (K-Means 사용)
from sklearn.cluster import KMeans
clustering_data = data[['출루율', 'log_salary']]  # 군집화에 사용할 데이터
kmeans = KMeans(n_clusters=4, random_state=42)  # 4개 군집
data['cluster'] = kmeans.fit_predict(clustering_data)  # 군집 결과 추가
 
# 4. 컨투어 플롯 생성 준비
x_all = data['출루율']
y_all = data['log_salary']
z_all = data['출루율'] - 0.01 * data['log_salary']  # 종합 점수 계산
 
# 그리드를 생성하여 등고선 플롯 데이터 준비
X_grid, Y_grid = np.meshgrid(np.linspace(x_all.min(), x_all.max(), 100),
                             np.linspace(y_all.min(), y_all.max(), 100))
Z_grid = griddata(points=(x_all, y_all), values=z_all, xi=(X_grid, Y_grid), method='linear')
 
# 5. 군집 시각화를 위한 색상과 마커 설정
cluster_colors = ['green', 'blue', 'orange', 'magenta']  # 군집별 색상
cluster_markers = ['X', 'o', 'D', 's']  # 군집별 마커
 
# 6. 플롯 생성
plt.figure(figsize=(14, 10))
 
# 컨투어 플롯 생성
contour = plt.contourf(X_grid, Y_grid, Z_grid, levels=20, cmap="RdYlBu_r", alpha=0.8)
plt.colorbar(contour, label="Composite Score")  # 색상 막대 추가
 
# 각 군집의 선수 데이터 시각화
for cluster in range(4):
    cluster_data = data[data['cluster'] == cluster]
    plt.scatter(cluster_data['출루율'], cluster_data['log_salary'],
                color=cluster_colors[cluster],
                marker=cluster_markers[cluster],
                label=f"Cluster {cluster}",
                edgecolor='black', s=100)
 
# 선수 이름을 텍스트로 표시
for _, player in data.iterrows():
    plt.text(player['출루율'], player['log_salary'], player['선수명'], fontsize=8, ha='center')
 
# 7. 플롯 레이블 및 제목 추가
plt.title("2D Contour Plot of Player Rankings (Filtered by OBP > 10th Percentile and Games > 25th Percentile)", fontsize=14)
plt.xlabel("출루율", fontsize=12)
plt.ylabel("Log 연봉 (최근)", fontsize=12)
plt.legend(title="Clusters", fontsize=10, loc="upper left")
plt.grid(True)
 
# 8. 플롯 표시
plt.show()
