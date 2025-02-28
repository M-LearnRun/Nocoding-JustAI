import pydicom
import os
from collections import Counter
 
# DICOM 이미지 크기 수집 함수
def collect_image_sizes(image_files, input_dir):
    image_sizes = []
    for image_file in image_files:
        dicom_path = os.path.join(input_dir, image_file)
        dicom_data = pydicom.dcmread(dicom_path)
        image_sizes.append(dicom_data.pixel_array.shape)
    return image_sizes
 
# 정상 및 중증 DICOM 이미지 크기 수집
normal_image_sizes = collect_image_sizes(normal_files, normal_dir)
severe_image_sizes = collect_image_sizes(severe_files, severe_dir)
 
# 모든 이미지 크기 결합 후 빈도 확인
all_image_sizes = normal_image_sizes + severe_image_sizes
size_counts = Counter(all_image_sizes)
 
size_counts
