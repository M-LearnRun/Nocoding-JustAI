import os
import zipfile
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
 
# 압축 파일 경로 및 압축 해제 경로 설정
normal_zip_path = '/mnt/data/IDC_4_Normalized_Augmented_Normal_492.zip'
severe_zip_path = '/mnt/data/IDC_4_Normalized_Augmented_Severe_268.zip'
normal_extract_path = '/mnt/data/normal_images'
severe_extract_path = '/mnt/data/severe_images'
 
# 압축 파일 해제
with zipfile.ZipFile(normal_zip_path, 'r') as normal_zip_ref:
    normal_zip_ref.extractall(normal_extract_path)
with zipfile.ZipFile(severe_zip_path, 'r') as severe_zip_ref:
    severe_zip_ref.extractall(severe_extract_path)
 
# 이미지를 로드하여 그레이스케일로 변환 후 1D 배열로 변환하는 함수
def process_image_no_resize(image_path):
    img = Image.open(image_path).convert('L')  # 그레이스케일 변환
    return np.array(img).flatten()  # 1D 배열로 변환

# 정상 및 중증 이미지 불러오기
normal_files = os.listdir(normal_extract_path)
normal_images_all = [process_image_no_resize(os.path.join(normal_extract_path, file)) for file in normal_files]
 
severe_files = os.listdir(severe_extract_path)
severe_images_all = [process_image_no_resize(os.path.join(severe_extract_path, file)) for file in severe_files]
 
# 데이터 및 라벨 합치기
X_all = np.array(normal_images_all + severe_images_all)  # 데이터 합치기
y_all = np.array([0] * len(normal_images_all) + [1] * len(severe_images_all))  # 라벨 (0: 정상, 1: 중증)
 
# 학습 및 테스트 데이터 분리 (80% 학습, 20% 테스트)
X_train_all, X_test_all, y_train_all, y_test_all = train_test_split(X_all, y_all, test_size=0.2, random_state=42)
 
# 랜덤포레스트 분류기 학습
rf_clf_all = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf_all.fit(X_train_all, y_train_all)
 
# 테스트 데이터 예측 및 성능 평가
y_pred_all = rf_clf_all.predict(X_test_all)
classification_rep_all = classification_report(y_test_all, y_pred_all, target_names=["Normal", "Severe"])
 
classification_rep_all  # 결과 출력
