import zipfile
import os
 
# ZIP 파일 경로 설정
sorted_normal_dicom_zip = '/mnt/data/Sorted_Normal_T2_DICOM.zip'
sorted_severe_dicom_zip = '/mnt/data/Sorted_Severe_T2_DICOM.zip'
sorted_normal_png_zip = '/mnt/data/Sorted_Resized_Normal_T2_PNG.zip'
sorted_severe_png_zip = '/mnt/data/Sorted_Resized_Severe_T2_PNG.zip'
 
# T2 DICOM 파일 압축 (정상)
with zipfile.ZipFile(sorted_normal_dicom_zip, 'w') as normal_zip:
    for file in T2_normal_files:
        normal_zip.write(file, os.path.basename(file))
 
# T2 DICOM 파일 압축 (중증)
with zipfile.ZipFile(sorted_severe_dicom_zip, 'w') as severe_zip:
    for file in T2_severe_files:
        severe_zip.write(file, os.path.basename(file))
 
# T2 PNG 파일 압축 (정상)
with zipfile.ZipFile(sorted_normal_png_zip, 'w') as normal_png_zip:
    for dicom_file in T2_normal_files:
        png_file = normal_mapping[dicom_file]
        normal_png_zip.write(png_file, os.path.basename(png_file))
 
# T2 PNG 파일 압축 (중증)
with zipfile.ZipFile(sorted_severe_png_zip, 'w') as severe_png_zip:
    for dicom_file in T2_severe_files:
        png_file = severe_mapping[dicom_file]
        severe_png_zip.write(png_file, os.path.basename(png_file))
 
sorted_normal_dicom_zip, sorted_severe_dicom_zip, sorted_normal_png_zip, sorted_severe_png_zip
