import pandas as pd
 
# CSV 파일 로드
file_path = '/mnt/data/tire_models_load_capacity_Regression Analysis.csv'
data = pd.read_csv(file_path)
 
# 데이터 구조를 이해하기 위해 첫 몇 줄 출력
data.head()
