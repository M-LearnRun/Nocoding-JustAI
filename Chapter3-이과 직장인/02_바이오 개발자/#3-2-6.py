import random
import os
import pydicom
import cv2
import matplotlib.pyplot as plt
 
# 정상 및 중증 샘플을 랜덤으로 선택
random_normal_index = random.randint(0, len(normal_files) - 1)
random_severe_index = random.randint(0, len(severe_files) - 1)
 
# DICOM 및 PNG 파일 경로 설정
random_normal_png_file = f"normal_{random_normal_index}.png"
random_severe_png_file = f"severe_{random_severe_index}.png"
random_normal_dicom_file = os.path.join(normal_dir, normal_files[random_normal_index])
random_severe_dicom_file = os.path.join(severe_dir, severe_files[random_severe_index])
 
# DICOM 파일 및 메타데이터 로드
normal_dicom_data = pydicom.dcmread(random_normal_dicom_file)
severe_dicom_data = pydicom.dcmread(random_severe_dicom_file)
 
# PNG 이미지 로드
normal_png_image = cv2.imread(os.path.join(resized_normal_16bit_dir, random_normal_png_file), cv2.IMREAD_GRAYSCALE)
severe_png_image = cv2.imread(os.path.join(resized_severe_16bit_dir, random_severe_png_file), cv2.IMREAD_GRAYSCALE)
 
# DICOM 및 PNG 이미지 비교 시각화
plt.figure(figsize=(10, 8))
 
plt.subplot(2, 2, 1)
plt.imshow(normal_dicom_data.pixel_array, cmap='gray')
plt.axis('off')
 
plt.subplot(2, 2, 2)
plt.imshow(normal_png_image, cmap='gray')
plt.axis('off')
 
plt.subplot(2, 2, 3)
plt.imshow(severe_dicom_data.pixel_array, cmap='gray')
plt.axis('off')
 
plt.subplot(2, 2, 4)
plt.imshow(severe_png_image, cmap='gray')
plt.axis('off')
 
plt.show()
 # DICOM 메타데이터 확인
normal_dicom_data, severe_dicom_data
