# 필요한 모듈 불러오기
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
 
# 1. 산점도 및 회귀선 그리기 위한 선형 회귀 모델 준비
model_TDA1 = LinearRegression()
model_TDA2 = LinearRegression()
 
# 2. 'TDA1-제목 흥미도와 창작성'과 'TDA2-책의 난이도 파악'의 데이터를 준비하고 세일즈포인트에 대한 예측 수행
TDA1_x = text_analysis_data['TDA1-제목 흥미도와 창작성'].values.reshape(-1, 1)
TDA2_x = text_analysis_data['TDA2-책의 난이도 파악'].values.reshape(-1, 1)
sales_y = text_analysis_data['세일즈포인트'].values
 
# 3. 선형 회귀 모델 학습
model_TDA1.fit(TDA1_x, sales_y)
model_TDA2.fit(TDA2_x, sales_y)

# 4. 예측값 생성
TDA1_pred = model_TDA1.predict(TDA1_x)
TDA2_pred = model_TDA2.predict(TDA2_x)
 
# 5. 두 개의 산점도 및 회귀선 플롯을 그리기 위한 서브플롯 설정
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
 
# 6. 첫 번째 그래프: TDA1-제목 흥미도와 창작성 vs 세일즈포인트 (파란색 점과 빨간색 회귀선)
sns.regplot(x='TDA1-제목 흥미도와 창작성', y='세일즈포인트', data=text_analysis_data, ax=ax[0], 
            scatter_kws={'s': 50, 'alpha': 0.8, 'edgecolor': 'black', 'color': 'blue'}, 
            line_kws={'color': 'red'})
 
# 7. 두 번째 그래프: TDA2-책의 난이도 파악 vs 세일즈포인트 (초록색 점과 빨간색 회귀선)
sns.regplot(x='TDA2-책의 난이도 파악', y='세일즈포인트', data=text_analysis_data, ax=ax[1], 
            scatter_kws={'s': 50, 'alpha': 0.8, 'edgecolor': 'black', 'color': 'green'}, 
            line_kws={'color': 'red'})
 
# 8. 그래프 출력
plt.tight_layout()
plt.show()
