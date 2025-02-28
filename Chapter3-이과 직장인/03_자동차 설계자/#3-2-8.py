# [상관관계 히트맵 시각화 및 주요 변수 탐색 코드]
import matplotlib.pyplot as plt
import seaborn as sns
 
# 결측치 확인
missing_values = data.isnull().sum()
 
# 상관 행렬 계산 및 히트맵 생성
corr_matrix = data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, cmap='coolwarm', linewidths=0.5)
plt.title('Feature Correlation Heatmap')
plt.show()

# 출력 변수와 상위 상관계수 변수 확인
top_corr_features = corr_matrix['STEP1_FREQ_1ST'].sort_values(ascending=False).head(10)
 
missing_values, top_corr_features
