# 데이터 설정
sample_mean = 37000  # 샘플 평균 (km)
sample_std = 5000    # 샘플 표준편차 (km)
sample_size = 100    # 샘플 수
z_value = 1.96       # 95% 신뢰수준에 해당하는 Z값
 
# 표준오차 계산
standard_error = sample_std / (sample_size ** 0.5)
 
# 신뢰구간 계산
margin_of_error = z_value * standard_error
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
 
confidence_interval
