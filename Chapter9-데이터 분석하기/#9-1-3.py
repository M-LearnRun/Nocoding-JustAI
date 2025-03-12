# 연령대에 따른 소득과 인구수를 시각화
fig, ax1 = plt.subplots(figsize=(10, 6))
 
# 막대그래프: 소득
ax1.bar(income_population_data['연령대'], income_population_data['소득(달러)'], color='skyblue', label='소득(달러)')
ax1.set_xlabel('연령대')  # x축 레이블
ax1.set_ylabel('소득(달러)', color='blue')  # y축 레이블
ax1.tick_params(axis='y', labelcolor='blue')  # y축 색상
 
# 선그래프: 인구수
ax2 = ax1.twinx()  # 두 번째 y축 생성
ax2.plot(income_population_data['연령대'], income_population_data['인구수(명)'], color='red', marker='o', label='인구수(명)')
ax2.set_ylabel('인구수(명)', color='red')  # 두 번째 y축 레이블
ax2.tick_params(axis='y', labelcolor='red')  # 두 번째 y축 색상
 
# 제목 및 범례 추가
plt.title('연령대별 소득과 인구수')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
 
# 그래프 표시
plt.show()
