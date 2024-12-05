import zipfile
import os
 
# 경로 및 디렉토리 설정
normal_zip_path = '/mnt/data/Normal_99.Zip'
severe_zip_path = '/mnt/data/Severe_68.Zip'
normal_dir = '/mnt/data/normal_mri/'
severe_dir = '/mnt/data/severe_mri/'
 
os.makedirs(normal_dir, exist_ok=True)
os.makedirs(severe_dir, exist_ok=True)
 
# 압축 파일 해제
with zipfile.ZipFile(normal_zip_path, 'r') as zip_ref:
    zip_ref.extractall(normal_dir)
 
with zipfile.ZipFile(severe_zip_path, 'r') as zip_ref:
    zip_ref.extractall(severe_dir)
 
# 파일 수 확인
len(os.listdir(normal_dir)), len(os.listdir(severe_dir))
