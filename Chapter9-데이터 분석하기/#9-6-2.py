from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
 
# 입력 변수(X)와 출력 변수(y) 정의
X = data[['D', 'W', 'P', 'd', 'w', 'rst']]
y = data['Force capacity']
 
# 데이터를 훈련 세트와 테스트 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# 선형 회귀 모델 생성 및 훈련
model = LinearRegression()
model.fit(X_train, y_train)
 
# 테스트 세트에 대해 예측 수행
y_pred = model.predict(X_test)
 
# 모델 평가: 평균 제곱 오차(MSE) 및 결정 계수(R²) 계산
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
 
# 변수별 회귀 계수 출력
model_coefficients = pd.DataFrame({
    'Variable': X.columns,
    'Coefficient': model.coef_
})
 
# 모델 평가 결과 출력
model_evaluation = {
    'Mean Squared Error': mse,
    'R-squared': r2
}
 
model_coefficients, model_evaluation
