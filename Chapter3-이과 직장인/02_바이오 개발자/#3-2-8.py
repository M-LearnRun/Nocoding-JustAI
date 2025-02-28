import pydicom
import os
 
# 'T2'가 시리즈 설명에 있는지 여부에 따른 파일 수를 세는 함수
def count_T2_files(dicom_files):
    T2_count = 0
    non_T2_count = 0
 
    for dicom_file in dicom_files:
        dicom_data = pydicom.dcmread(dicom_file)
        
        # 시리즈 설명에 'T2' 포함 여부 확인
        if 'T2' in dicom_data.SeriesDescription:
            T2_count += 1
        else:
            non_T2_count += 1
 
    return T2_count, non_T2_count
 
# 정상 및 중증 디렉토리에서 모든 DICOM 파일 리스트 수집
all_dicom_files = [os.path.join(normal_dir, file) for file in normal_files] + \
                  [os.path.join(severe_dir, file) for file in severe_files]
 
# 'T2'가 포함된 파일 수 계산
T2_count, non_T2_count = count_T2_files(all_dicom_files)
T2_count, non_T2_count
