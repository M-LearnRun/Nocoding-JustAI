import pydicom
import os
import cv2
 
# OpenCV를 사용하여 16비트 PNG 이미지 저장 함수
def resize_and_save_16bit_png_cv2(image_files, input_dir, output_dir, label, new_size=(256, 256)):
    os.makedirs(output_dir, exist_ok=True)
    
    for idx, image_file in enumerate(image_files):
        dicom_path = os.path.join(input_dir, image_file)
        dicom_data = pydicom.dcmread(dicom_path)
        
        # 윈도우잉 적용 후 이미지 조정
        adjusted_img = apply_windowing(dicom_data)
        
        # 이미지 리사이징
        resized_image = cv2.resize(adjusted_img, new_size)
        
        # 16비트 PNG로 저장
        png_filename = f"{label}_{idx}.png"
        cv2.imwrite(os.path.join(output_dir, png_filename), resized_image)
 
# 정상 및 중증 DICOM 이미지 리사이징 및 16비트 PNG로 저장
resize_and_save_16bit_png_cv2(normal_files, normal_dir, resized_normal_16bit_dir, "normal", new_size=(256, 256))
resize_and_save_16bit_png_cv2(severe_files, severe_dir, resized_severe_16bit_dir, "severe", new_size=(256, 256))
 
# 생성된 PNG 파일 확인
os.listdir(resized_normal_16bit_dir)[:5], os.listdir(resized_severe_16bit_dir)[:5]
