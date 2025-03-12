import pandas as pd
import matplotlib.pyplot as plt
 
# 데이터 로드
file_path = '/mnt/data/선 그래프-일일 기온_(2024년 7월 시계열 데이터.csv'
temperature_data = pd.read_csv(file_path)
 
# 데이터 파싱
temperature_data['Date'] = pd.to_datetime(temperature_data['Date'])
dates = temperature_data['Date']
temperatures = temperature_data['Temperature (°C)']
 
# 선 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(dates, temperatures, color='blue', linestyle='-', linewidth=2)  # 파란색 선으로 설정
 
# 축 및 제목 설정
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.title('Daily Temperature In July 2024', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
 
# 그래프 스타일 조정
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_color('#CCCCCC')
plt.gca().tick_params(colors='#666666')
 
# 그래프 표시
plt.tight_layout()
plt.show()
