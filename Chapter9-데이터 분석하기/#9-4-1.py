# 필요한 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt
 
# 데이터 로드
file_path_histogram_data = '/mnt/data/히스토그램 - 1000대의 자동차 전장 거리 오차 데이터.csv'
histogram_data = pd.read_csv(file_path_histogram_data)
 
# 히스토그램 생성
plt.figure(figsize=(8, 6))  # 플롯 크기 설정
plt.hist(
    histogram_data['Error Value'],  # 히스토그램 데이터
    bins=30,  # 히스토그램 빈 개수 설정
    color='skyblue',  # 히스토그램 색상
    edgecolor='black',  # 히스토그램 테두리 색상
    alpha=0.7  # 투명도 설정
)
plt.title("Histogram of Automotive Length Measurement Errors")  # 플롯 제목
plt.xlabel("Error Value (mm)")  # x축 레이블
plt.ylabel("Frequency")  # y축 레이블
plt.grid(axis='y', alpha=0.75)  # y축에 그리드 추가
plt.show()  # 플롯 표시
