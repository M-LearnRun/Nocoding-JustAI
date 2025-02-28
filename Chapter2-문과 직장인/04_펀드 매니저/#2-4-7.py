# [KOSPI 및 KOSDAQ 월별 중앙값과 평균 시각화]
 
# KOSPI 및 KOSDAQ의 월별 중앙값 및 평균 계산
kospi_median = kospi_pivot.median()
kospi_mean = kospi_pivot.mean()
 
kosdaq_median = kosdaq_pivot.median()
kosdaq_mean = kosdaq_pivot.mean()
 
# 그래프 그리기
plt.figure(figsize=(7, 5))
plt.bar(kospi_median.index, kospi_median, color='blue', alpha=0.7, label='KOSPI Median')
plt.show()
 
plt.figure(figsize=(7, 5))
plt.bar(kospi_mean.index, kospi_mean, color='blue', alpha=0.4, label='KOSPI Mean')
plt.show()
 
plt.figure(figsize=(7, 5))
plt.bar(kosdaq_median.index, kosdaq_median, color='red', alpha=0.7, label='KOSDAQ Median')
plt.show()
 
plt.figure(figsize=(7, 5))
plt.bar(kosdaq_mean.index, kosdaq_mean, color='red', alpha=0.4, label='KOSDAQ Mean')
plt.show()
