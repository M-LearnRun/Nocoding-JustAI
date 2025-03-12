import matplotlib.pyplot as plt
import numpy as np
 
# 데이터 준비
countries = sales_data['Country']
male_sales = sales_data['Male']
female_sales = sales_data['Female']
x = np.arange(len(countries))  # 국가별 위치 설정
 
# 그래프 생성
plt.figure(figsize=(10, 6))
bar_width = 0.35
 
# 막대 추가
plt.bar(x - bar_width/2, male_sales, width=bar_width, label='Male', color='orange')
plt.bar(x + bar_width/2, female_sales, width=bar_width, label='Female', color='gold')
 
# 축 및 제목 설정
plt.xlabel('Country', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.title('Product Sales by Country and Gender', fontsize=14)
plt.xticks(x, countries, rotation=45)
plt.legend(title='Gender')
 
# 그래프 표시
plt.tight_layout()
plt.show()
