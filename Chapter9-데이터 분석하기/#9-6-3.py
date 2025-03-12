import numpy as np
import matplotlib.pyplot as plt
 
# 전체 데이터셋에 대해 Force capacity 예측 수행
y_all_pred = model.predict(X)
 
# 추세선(선형 회귀선) 계산
z = np.polyfit(y, y_all_pred, 1)  # y에 대한 y_all_pred의 회귀선 계산
p = np.poly1d(z)
 
# 실제 값과 예측 값을 비교하는 산점도 및 추세선 시각화
plt.figure(figsize=(8, 8))  # 정사각형 비율 설정
plt.scatter(y, y_all_pred, alpha=0.6, label="Predicted vs Actual", color="blue")  # 예측 vs 실제 산점도
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--', color='black', label="Y = X (Ideal)")  # 이상적인 Y = X 선
plt.plot(y, p(y), color='red', label="Trend Line")  # 추세선
 
# 그래프 제목 및 레이블 추가
plt.title("Actual vs Predicted Force Capacity")
plt.xlabel("Actual Force Capacity")
plt.ylabel("Predicted Force Capacity")
plt.legend()
plt.grid(alpha=0.4)
plt.tight_layout()
 
# 그래프 표시
plt.show()
