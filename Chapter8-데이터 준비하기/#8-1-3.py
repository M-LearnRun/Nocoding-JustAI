import pandas as pd
 
# 업로드된 엑셀 파일 경로
file_path = '/mnt/data/출판통계_kobic_2011to2021_annual.xlsx'
 
# 엑셀 파일 읽기
data_excel = pd.read_excel(file_path, sheet_name=None) # 모든 시트 읽기
 
# 시트 이름 확인 및 첫 번째 시트 데이터 확인
sheet_names = data_excel.keys()
first_sheet_data = data_excel[list(sheet_names)[0]] # 첫 번째 시트의 데이터 확인
 
first_sheet_data.head(), sheet_names # 첫 번째 시트 데이터 미리보기, 시트 이름 출력
