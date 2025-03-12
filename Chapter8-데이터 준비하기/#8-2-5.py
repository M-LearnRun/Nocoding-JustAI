# IQR 계산 및 이상치 경계 정의
Q1 = data['Age'].quantile(0.25)
Q3 = data['Age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR  # 하한
upper_bound = Q3 + 1.5 * IQR  # 상한
 
# 'Age' 열에서 이상치 탐지 및 처리 (하한 미만 값은 하한으로, 상한 초과 값은 상한으로 조정)
data_imputed_iqr = data.copy()
data_imputed_iqr['Age'] = np.where(data['Age'] < lower_bound, lower_bound, data['Age'])
data_imputed_iqr['Age'] = np.where(data['Age'] > upper_bound, upper_bound, data_imputed_iqr['Age'])
 
# 이상치 처리 전후의 분포 비교 (히스토그램)
plt.figure(figsize=(14, 6))
 
# 이상치 처리 전 분포
plt.subplot(1, 2, 1)
plt.hist(data['Age'].dropna(), bins=20, color='lightblue', edgecolor='black')
plt.title('Age Distribution Before Outlier Treatment')
plt.xlabel('Age')
plt.ylabel('Frequency')
 
# 이상치 처리 후 분포
plt.subplot(1, 2, 2)
plt.hist(data_imputed_iqr['Age'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Age Distribution After IQR Outlier Treatment')
plt.xlabel('Age')
plt.ylabel('Frequency')
 
plt.tight_layout()
plt.show()
 
# 이상치 처리 전후의 박스플롯 비교
plt.figure(figsize=(12, 6))
 
# 이상치 처리 전 박스플롯
plt.subplot(1, 2, 1)
plt.boxplot(data['Age'].dropna(), vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Box Plot of Age Before Outlier Treatment')
plt.xlabel('Age')
