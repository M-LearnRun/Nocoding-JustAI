# pandas 라이브러리 불러오기
import pandas as pd
 
# 파일 경로 지정
file_path = '/mnt/data/ML_1_자동차 차체 설계 제원과 강성 성능_원본데이터.csv'
 
# CSV 파일을 pandas 데이터프레임으로 읽기
data = pd.read_csv(file_path)
 
# 데이터의 첫 5개 행 확인
data.head()
