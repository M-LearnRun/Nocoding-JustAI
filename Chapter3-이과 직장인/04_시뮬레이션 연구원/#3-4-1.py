import zipfile, os
 
# 파일 경로와 추출 위치 설정
zip_file_path = '/mnt/data/ross-main.zip'
extract_path = '/mnt/data/ross-main/'
 
# 압축 파일 추출 및 파일 목록 확인
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
 
extracted_files = os.listdir(extract_path)
extracted_files  # 파일 목록 반환
 
# 패키지 설치
!pip install /mnt/data/ross-main/ross-main
