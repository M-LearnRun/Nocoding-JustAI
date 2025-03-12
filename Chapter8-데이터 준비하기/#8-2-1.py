import pandas as pd
import matplotlib.pyplot as plt
 
# 데이터셋 로드
file_path = '/mnt/data/titanic_train.csv'  # 데이터 파일 경로
data = pd.read_csv(file_path)              # CSV 파일을 읽어서 데이터프레임 
 
# 결측치 시각화 (검정색 = 데이터 존재, 흰색 = 결측 데이터)
plt.figure(figsize=(12, 8))              # 플롯의 크기 설정
plt.imshow(data.isnull(), aspect='auto', # 데이터의 결측 여부를 
           cmap='gray', interpolation='nearest')   
plt.title('결측 데이터 히트맵 (검정색 = 존재, 흰색 = 결측)')  # 플롯 제목 설정
plt.ylabel('행')                                   # y축 라벨 설정
plt.xlabel('열')                                   # x축 라벨 설정
plt.xticks(ticks=range(len(data.columns)),         # x축의 열 이름 라벨 설정
           labels=data.columns, rotation=45)       # 열 이름 회전하여 표시
plt.tight_layout()                                 # 레이아웃 자동 조정
plt.show()
