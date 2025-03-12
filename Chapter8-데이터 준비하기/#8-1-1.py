# 필요한 라이브러리 import
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
 
# 데이터프레임 생성
data = {
    "연도": [1970, 1980, 1990, 2000, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    "전체": [62.3, 66.1, 71.7, 76.0, 80.2, 80.6, 80.9, 81.4, 81.8, 82.1, 82.4, 82.7, 82.7, 83.3, 83.5, 83.6, 82.7, 83.5],
    "남자": [58.7, 61.9, 67.5, 72.3, 76.8, 77.3, 77.6, 78.1, 78.6, 79.0, 79.3, 79.7, 79.7, 80.3, 80.5, 80.6, 79.9, 80.6],
    "여자": [65.8, 70.4, 75.9, 79.7, 83.6, 84.0, 84.2, 84.6, 85.0, 85.2, 85.4, 85.7, 85.7, 86.3, 86.5, 86.6, 85.6, 86.4]
}
df = pd.DataFrame(data)
 
# 수명 데이터를 시각적으로 표현 (선 스타일 및 색상 변경)
plt.figure(figsize=(12, 8))
plt.plot(df['연도'], df['전체'], marker='o', label='전체 평균 기대수명', linewidth=2.5, color='black', linestyle='--', markersize=10)
plt.plot(df['연도'], df['남자'], marker='o', label='남성 기대수명', linewidth=2.5, color='blue', linestyle='-', markersize=10)
plt.plot(df['연도'], df['여자'], marker='o', label='여성 기대수명', linewidth=2.5, color='red', linestyle='-', markersize=10)
 
# 그래프 꾸미기
plt.title('1970-2023 대한민국 기대수명 추세', fontsize=18)
plt.xlabel('연도', fontsize=20, color='darkblue')
plt.ylabel('기대수명 (년)', fontsize=20, color='darkred')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
 
# 시각화 출력
plt.show()
