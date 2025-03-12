import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# 타이타닉 데이터셋 불러오기
file_path_new = '/mnt/data/titanic_train.csv'
data_titanic = pd.read_csv(file_path_new)
 
# 단변량 EDA - 주요 수치형 컬럼에 대한 요약 통계
numerical_features = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
univariate_summary = data_titanic[numerical_features].describe()
 
# 요약 통계 표시
import ace_tools as tools
tools.display_dataframe_to_user(name="Univariate EDA Summary", dataframe=univariate_summary)

 
# 수치형 변수들의 분포 시각화
plt.figure(figsize=(14, 12))
 
for i, feature in enumerate(numerical_features, 1):
    plt.subplot(3, 2, i)
    sns.histplot(data_titanic[feature].dropna(), kde=True, color='skyblue', bins=30)
    plt.title(f'Distribution of {feature}')
 
plt.show()
