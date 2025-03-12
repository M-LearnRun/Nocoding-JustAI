from sklearn.experimental import enable_iterative_imputer  # IterativeImputer 활성화
from sklearn.impute import IterativeImputer
import numpy as np
 
# 'Age' 열에서 원래 결측치 개수 확인
original_missing_age = data['Age'].isnull().sum()
 
# IterativeImputer로 'Age' 결측치 채우기 ('Pclass', 'Fare'를 기준으로 대체)
imputer = IterativeImputer(max_iter=10, random_state=0)  # 10번 반복, 랜덤 시드 고정
# 'Age', 'Pclass', 'Fare' 열에 imputer 적용
data_imputed = data.copy()  # 원본 데이터 복사본 생성
age_imputed = imputer.fit_transform(data[['Age', 'Pclass', 'Fare']])  
 
# 'Age' 열을 대체된 값으로 업데이트
data_imputed['Age'] = age_imputed[:, 0]
 
# 대체 후 'Age' 열의 결측치 개수 확인
imputed_missing_age = data_imputed['Age'].isnull().sum()
 
# 대체된 값 확인 (원래 결측치였던 행들만 필터링)
imputed_samples = data_imputed[data['Age'].isnull()] 
 
# 사용자에게 대체된 데이터 표시
import ace_tools as tools
tools.display_dataframe_to_user(name="Imputed Age Samples", dataframe=imputed_samples)
 
imputed_samples[['Age', 'Pclass', 'Fare']]
