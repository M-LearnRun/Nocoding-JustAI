# 텍스트 데이터 분석에 사용할 열 선택
selected_columns = ["세일즈포인트", "TDA1-제목 흥미도와 창작성", "TDA2-책의 난이도 파악", 
                    "TDA3-저자의 인지도와 명성", "TDA4-논리 전개성", "TDA5-책소개로 흥미 유발"]
 
text_analysis_data = data[selected_columns]
 
# 선택한 데이터를 사용자에게 표시
tools.display_dataframe_to_user(name="텍스트 데이터 분석용 데이터", dataframe=text_analysis_data)
 
# 1. 전체 상관관계 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')
 
# 2. '세일즈포인트'와 다른 변수 간의 상관관계 추출
sales_point_correlation = correlation_data.corr().loc[["세일즈포인트"]]
 
# '세일즈포인트' 행의 상관관계만 따로 히트맵으로 시각화
plt.figure(figsize=(10, 2))
sns.heatmap(sales_point_correlation, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')
plt.show()
