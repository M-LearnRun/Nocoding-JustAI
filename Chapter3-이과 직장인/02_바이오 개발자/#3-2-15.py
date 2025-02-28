import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
 
# 혼동 행렬 시각화
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=["정상인", "환자"], yticklabels=["정상인", "환자"])
plt.show()
 
# 성능 지표 시각화 (정확도, 재현율, F1-점수)
plt.figure(figsize=(10, 6))
bar_width = 0.2
index = np.arange(len(classes))
plt.bar(index, precision, bar_width, label='정확도')
plt.bar(index + bar_width, recall, bar_width, label='재현율')
plt.bar(index + 2 * bar_width, f1_score, bar_width, label='F1-점수')
plt.show()
