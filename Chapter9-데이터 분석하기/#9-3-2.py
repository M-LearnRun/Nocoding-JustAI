import matplotlib.pyplot as plt
import numpy as np
 
# 데이터 로드
cities = data['City']
population = data['Population (millions)']
area = data['Area (km²)']
gdp = data['GDP (billion USD)']
 
# 색상 및 크기 설정
colors = gdp
bubble_sizes = gdp * 15  # 크기를 적절히 조정
 
# 버블 차트 생성
plt.figure(figsize=(8, 6))
scatter = plt.scatter(population, area, s=bubble_sizes, c=colors, cmap='viridis', alpha=0.6, marker='o', edgecolors='black')
 
# 색상 막대 추가
colorbar = plt.colorbar(scatter)
colorbar.set_label('GDP (billion USD)', fontsize=12)
 
# 도시 이름 추가
for i, city in enumerate(cities):
    plt.text(population[i], area[i], city, fontsize=10, ha='center')
 
# 축 및 제목 설정
plt.xlabel('Population (millions)', fontsize=12)
plt.ylabel('Area (km²)', fontsize=12)
plt.title('City Population, Area, and GDP', fontsize=14)
 
# 그래프 표시
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
