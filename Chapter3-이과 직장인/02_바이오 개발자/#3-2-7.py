import zipfile
import os
 
# ZIP 파일 경로 설정
resized_normal_16bit_zip = '/mnt/data/Resized_Normal_256_16bit_PNG.zip'
resized_severe_16bit_zip = '/mnt/data/Resized_Severe_256_16bit_PNG.zip'
 
# 정상 이미지 압축
with zipfile.ZipFile(resized_normal_16bit_zip, 'w') as normal_zip:
    for file in os.listdir(resized_normal_16bit_dir):
        normal_zip.write(os.path.join(resized_normal_16bit_dir, file), file)
 
# 중증 이미지 압축
with zipfile.ZipFile(resized_severe_16bit_zip, 'w') as severe_zip:
    for file in os.listdir(resized_severe_16bit_dir):
        severe_zip.write(os.path.join(resized_severe_16bit_dir, file), file)
 
# 압축된 파일 경로 반환
resized_normal_16bit_zip, resized_severe_16bit_zip
