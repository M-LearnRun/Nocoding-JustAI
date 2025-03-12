import zipfile
import os
# Zip 파일 경로 및 추출 경로 정의
zip_file_path = '/mnt/data/Data20ea_compressed.Zip'
extract_dir = '/mnt/data/extracted_files/'
# Zip 파일 추출 및 파일 개수 계산
os.makedirs(extract_dir, exist_ok=True)
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)
file_count = len(os.listdir(extract_dir))
file_count 
