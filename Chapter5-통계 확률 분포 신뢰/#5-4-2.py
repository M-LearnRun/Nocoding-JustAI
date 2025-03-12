# 정규분포 및 신뢰구간 시각화를 생성하기 위한 코드
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
 
# 데이터 설정
sample_mean = 37000  # 샘플 평균
sample_std = 5000    # 샘플 표준편차
sample_size = 100
z_value = 1.96       # 95% 신뢰수준
 
# 신뢰구간 계산
standard_error = sample_std / np.sqrt(sample_size)
lower_bound = sample_mean - z_value * standard_error
upper_bound = sample_mean + z_value * standard_error
 
# 가상의 데이터 분포 생성
x = np.linspace(35000, 39000, 500)
y = (1 / (np.sqrt(2 * np.pi) * standard_error)) * np.exp(-0.5 * ((x - sample_mean) / standard_error) ** 2)
 
# 시각화
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='정규분포', color='orange')
plt.axvline(sample_mean, color='red', linestyle='--', label='표본 평균')
plt.fill_between(x, y, where=(x >= lower_bound) & (x <= upper_bound), color='skyblue', alpha=0.5, label='95% 신뢰구간')
 
# 그래프 설정
plt.title("신뢰구간과 정규분포")
plt.xlabel("주행 거리 (km)")
plt.ylabel("확률 밀도 함수")
plt.legend()
plt.grid(True)
plt.show()
