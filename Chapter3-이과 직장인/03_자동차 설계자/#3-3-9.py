import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
 
# 데이터 로드
file_path_knn = '/mnt/data/ML_2-2_자동차 차체 설계 제원과 강성 성능_이상치제거.csv'
data_knn = pd.read_csv(file_path_knn)
 
# 입력 및 출력 변수 설정
input_columns = [col for col in data_knn.columns if col != 'STEP1_FREQ_1ST']
output_column = 'STEP1_FREQ_1ST'
 
# 데이터 필터링 및 결측치 제거
data_filtered_knn = data_knn[input_columns + [output_column]].dropna()
X = data_filtered_knn[input_columns]
y = data_filtered_knn[output_column]

# 데이터 분할 (70% 훈련, 30% 검증)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)
 
# 모델 초기화 및 학습
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(random_state=42),
    "SVM": SVR(),
    "Neural Network": MLPRegressor(random_state=42, max_iter=1000),
    "KNN": KNeighborsRegressor()
}
 
# 각 모델에 대한 MSE 계산
mse_results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    mse = mean_squared_error(y_val, y_pred)
    mse_results[name] = mse
 
# 결과를 데이터프레임으로 생성 및 출력
mse_df = pd.DataFrame(list(mse_results.items()), columns=["Model", "MSE"])
import ace_tools as tools; tools.display_dataframe_to_user(name="MSE Comparison Results", dataframe=mse_df)
 
# MSE 결과 시각화 (옵션)
plt.figure(figsize=(10, 6))
plt.bar(mse_results.keys(), mse_results.values(), color='skyblue')
plt.title("MSE of Different Models")
plt.ylabel("MSE")
plt.show()
