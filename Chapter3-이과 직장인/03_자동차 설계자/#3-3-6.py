# 이상치를 제거한 데이터셋 정의
cleaned_data = remove_outliers(data, 'STEP1_FREQ')
 
# 파일로 저장 후 다운로드 링크 제공
output_file_path = "/mnt/data/cleaned_car_body_data.csv"
cleaned_data.to_csv(output_file_path, index=False)
 
output_file_path
