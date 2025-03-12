from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
 
# 의사결정 나무를 위해 데이터 준비
# 클래스 레이블 추가: 높은 출루율/연봉과 낮은 출루율/연봉 기준
threshold_obp = data_for_plot['출루율'].mean()
threshold_salary = data_for_plot['log_salary'].mean()
 
data_for_plot['class'] = data_for_plot.apply(
    lambda x: f"높은 출루율, 높은 연봉" if x['출루율'] > threshold_obp and x['log_salary'] > threshold_salary else
              f"낮은 출루율, 높은 연봉" if x['출루율'] <= threshold_obp and x['log_salary'] > threshold_salary else
              f"높은 출루율, 낮은 연봉" if x['출루율'] > threshold_obp and x['log_salary'] <= threshold_salary else
              f"낮은 출루율, 낮은 연봉", axis=1
)
 
# 독립변수와 종속변수 분리
X = data_for_plot[['출루율', 'log_salary']]
y = data_for_plot['class']
 
# 의사결정 나무 모델 생성 및 학습
tree_model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
tree_model.fit(X, y)
 
# 의사결정 나무 시각화
plt.figure(figsize=(12, 8))
plot_tree(tree_model, 
          feature_names=['출루율', '연봉(최근)_log'], 
          class_names=tree_model.classes_, 
          filled=True, 
          rounded=True, 
          fontsize=10)
plt.title('Decision Tree for Player Clustering', fontsize=16)
plt.show()
