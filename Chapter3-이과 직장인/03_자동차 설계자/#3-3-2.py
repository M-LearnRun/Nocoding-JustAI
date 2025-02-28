import matplotlib.pyplot as plt
import seaborn as sns
 
# 시각화의 가독성을 높이기 위해 그림의 크기를 설정
plt.figure(figsize=(12, 8))
 
sns.heatmap(data.isnull(), cbar=False, cmap=['black', 'white'])
plt.show()
