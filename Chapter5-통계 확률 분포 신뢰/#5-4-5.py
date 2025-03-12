# 필요한 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
 
# 데이터 불러오기
file_path = '/mnt/data/Smoothed_Smartphone_Replacement_2013_2020.csv'
data = pd.read_csv(file_path)
 
# 2013년과 2020년 데이터 필터링
data_2013 = data[data['Year'] == 2013]['Replacement Period (months)']  # 2013년 데이터
data_2020 = data[data['Year'] == 2020]['Replacement Period (months)']  # 2020년 데이터
 
# 그래프 생성
plt.figure(figsize=(10, 8))
 
# 2013년 데이터 히스토그램
plt.subplot(2, 1, 1)  # 첫 번째 서브플롯
plt.hist(data_2013, bins=10, color='green', alpha=0.7, density=True, label='2013 데이터 히스토그램')  # 히스토그램 그리기
plt.title('데이터 히스토그램 - 2013', fontsize=14)  # 그래프 제목
plt.xlabel('교체 주기 (개월)', fontsize=12)  # x축 라벨
plt.ylabel('밀도', fontsize=12)  # y축 라벨
plt.legend()  # 범례 추가
 
# 2020년 데이터 히스토그램
plt.subplot(2, 1, 2)  # 두 번째 서브플롯
plt.hist(data_2020, bins=10, color='blue', alpha=0.7, density=True, label='2020 데이터 히스토그램')  # 히스토그램 그리기
plt.title('데이터 히스토그램 - 2020', fontsize=14)  # 그래프 제목
plt.xlabel('교체 주기 (개월)', fontsize=12)  # x축 라벨
plt.ylabel('밀도', fontsize=12)  # y축 라벨
plt.legend()  # 범례 추가
 
# 레이아웃 조정 및 출력
plt.tight_layout()  # 그래프 간격 조정
plt.show()  # 그래프 출력
