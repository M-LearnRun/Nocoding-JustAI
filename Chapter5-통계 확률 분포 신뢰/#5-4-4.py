# 한쪽 신뢰구간(하한) 신뢰수준 90%와 99%를 순차적으로 실행
results = {}
 
for confidence_level, z_value in [("90%", 1.28), ("99%", 2.33)]:
    # 한쪽 신뢰구간(하한) 계산
    lower_bound = sample_mean - z_value * standard_error
    results[confidence_level] = lower_bound
 
    # 시각화
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='정규분포', color='orange')
    plt.axvline(sample_mean, color='red', linestyle='--', label='표본 평균')
    plt.axvline(lower_bound, color='blue', linestyle='-', label=f'{confidence_level} 하한 신뢰구간')
 
    # 하한 구간은 하늘색으로, 나머지 구간은 빨간색으로
    plt.fill_between(x, y, where=(x >= lower_bound), color='skyblue', alpha=0.5, label=f'{confidence_level} 신뢰구간 (하한)')
    plt.fill_between(x, y, where=(x < lower_bound), color='pink', alpha=0.5, label='하한 바깥 구간')
 
    # 그래프 설정
    plt.title(f"한쪽 신뢰구간과 정규분포 ({confidence_level})")
    plt.xlabel("주행 거리 (km)")
    plt.ylabel("확률 밀도 함수")
    plt.legend()
    plt.grid(True)
    plt.show()
 
# 경계치 결과 출력
results
