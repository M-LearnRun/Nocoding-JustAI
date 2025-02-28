# [DICOM 이미지 랜덤 선택 및 시각화 코드]
import pydicom
import matplotlib.pyplot as plt
import random
import os
 
# DICOM 이미지 표시 함수
def display_dicom_image(dicom_file_path, title):
    dicom_image = pydicom.dcmread(dicom_file_path)
    plt.imshow(dicom_image.pixel_array, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()
 
# 정상 및 중증 디렉토리에서 랜덤 이미지 선택
random_normal_image = random.choice(normal_files)
random_severe_image = random.choice(severe_files)
 
# 선택된 이미지 파일 경로
normal_image_path = os.path.join(normal_dir, random_normal_image)
severe_image_path = os.path.join(severe_dir, random_severe_image)
 
# 정상 및 중증 이미지 표시
display_dicom_image(normal_image_path, "Normal (Label: 0)")
display_dicom_image(severe_image_path, "Severe (Label: 1)")
