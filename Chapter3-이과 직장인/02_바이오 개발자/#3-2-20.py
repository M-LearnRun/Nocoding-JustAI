### [정상인 MRI 이미지 판독]
# 필요한 모듈 불러오기
import pydicom
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
import pickle
 
########### Input ########################################
# DICOM 파일 경로 설정
dcm_file_path = '13317052_forTesting_0.dcm'
# 모델 불러오기 (사전 학습된 모델이 저장된 경로 지정)
with open('final_tuned_model.pkl', 'rb') as model_file:
rf_clf = pickle.load(model_file)
##########################################################

# DICOM 파일 읽기
dcm_data = pydicom.dcmread(dcm_file_path)
 
# DICOM 이미지 데이터 추출
dcm_image = dcm_data.pixel_array
 
# 이미지 시각화 (선택 사항)
plt.figure(figsize=(7, 7)) # figsize 인자로 크기 조정 (10x10 크기로 설정)
plt.imshow(dcm_image, cmap='gray')
plt.title('DICOM Image')
plt.show()
 
# PIL을 사용하여 이미지를 256x256 크기로 리사이즈
img_pil = Image.fromarray(dcm_image).convert('L') # 그레이스케일로 변환
img_resized_256 = img_pil.resize((256, 256)) # 크기 조정
img_array_256 = np.array(img_resized_256).flatten() # 1D 배열로 변환
 
# 모델 예측
img_array_reshaped_256 = img_array_256.reshape(1, -1)
prediction = rf_clf.predict(img_array_reshaped_256)
 
# 예측 결과 출력
if prediction[0] == 0:
print("정상입니다.")
else:
print("허리디스크 환자입니다.")
