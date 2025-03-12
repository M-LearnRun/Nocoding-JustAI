import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# CSV 파일 읽기
titanic_data = pd.read_csv('/mnt/data/titanic_train.csv')
 
# 데이터의 첫 5행 확인
print(titanic_data.head())
 
# 성별에 따른 생존율 시각화
plt.figure(figsize=(8, 6))
sns.countplot(data=titanic_data, x='Sex', hue='Survived')
plt.title('Survival Count by Gender')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right')
plt.show()
