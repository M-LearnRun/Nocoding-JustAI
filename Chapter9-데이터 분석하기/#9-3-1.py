# [직원의 근무 시간과 생산성에 대한 산점도 전체 코드]
import pandas as pd
import matplotlib.pyplot as plt
 
# 데이터 로드
file_path = '/mnt/data/산점도 - 직원의 근무시간과 생산성 상관관계 데이터.csv'
employee_productivity_data = pd.read_csv(file_path)
 
# 산점도 생성
plt.figure(figsize=(8, 6))
 
# 산점도 그리기
plt.scatter(
    employee_productivity_data['Working Hours'],
    employee_productivity_data['Productivity'],
    alpha=0.7,
    edgecolor='black',
    color='skyblue'
)
 
# 축 레이블 및 제목 추가
plt.xlabel('Working Hours per Week', fontsize=12)
plt.ylabel('Productivity', fontsize=12)
plt.title('Scatter Plot of Working Hours vs Productivity', fontsize=14)
 
# 그래프 표시
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
