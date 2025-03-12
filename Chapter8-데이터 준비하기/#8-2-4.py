numerical_features = data_imputed.select_dtypes(include=[np.number]).columns  # 숫자형 열만 선택
 
plt.figure(figsize=(12, 10))  # 전체 그래프 크기 설정
 
# 각 숫자형 특성에 대해 박스플롯 그리기
for i, feature in enumerate(numerical_features, 1):
    plt.subplot(len(numerical_features), 1, i)  # 특성마다 서브플롯 생성
    plt.boxplot(data_imputed[feature], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))  # 박스플롯
    plt.title(f'Box Plot of {feature}')  # 그래프 제목
    plt.xlabel(feature)  # x축 라벨 설정
 
plt.tight_layout()  # 레이아웃 간격 조정
plt.show()  # 그래프 출력
