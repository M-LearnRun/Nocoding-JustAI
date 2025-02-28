import zipfile
import os
 
# 증강된 데이터 ZIP 파일 경로
augmented_normal_zip = '/mnt/data/Augmented_Normal_492.zip'
augmented_severe_zip = '/mnt/data/Augmented_Severe_268.zip'
 
# 증강된 정상 데이터셋 압축
with zipfile.ZipFile(augmented_normal_zip, 'w') as normal_zip:
    for file in os.listdir('/mnt/data/Augmented_Normal/'):
        normal_zip.write(os.path.join('/mnt/data/Augmented_Normal/', file), file)
 
# 증강된 중증 데이터셋 압축
with zipfile.ZipFile(augmented_severe_zip, 'w') as severe_zip:
    for file in os.listdir('/mnt/data/Augmented_Severe/'):
        severe_zip.write(os.path.join('/mnt/data/Augmented_Severe/', file), file)
 
# ZIP 파일 경로 반환
augmented_normal_zip, augmented_severe_zip
