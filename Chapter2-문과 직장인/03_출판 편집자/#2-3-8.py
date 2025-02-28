# 수치형 및 범주형 열 확인
numeric_columns_new = books_data_new.select_dtypes(include=[np.number]).columns
categorical_columns_new = books_data_new.select_dtypes(include=['object']).columns
 
# 수치형 열의 기초 통계량 확인 및 범주형 열의 유일 값 개수 확인
numeric_summary_new = books_data_new[numeric_columns_new].describe()
categorical_summary_new = books_data_new[categorical_columns_new].nunique()
 
# 수치형 열의 분포를 히스토그램으로 시각화 (한글 폰트 적용)
import koreanize_matplotlib
plt.figure(figsize=(15, 10))
books_data_new[numeric_columns_new].hist(bins=20, figsize=(15, 10))
plt.suptitle('수치형 열의 분포', fontsize=16)
plt.tight_layout(pad=2.0)
plt.show()
 
# 범주형 열 중 일부를 막대 그래프로 시각화 (상위 5개 열만)
for col in categorical_columns_new[:5]:
    plt.figure(figsize=(8, 6))
    books_data_new[col].value_counts().plot(kind='bar')
    plt.title(f'{col}의 분포')
    plt.xlabel(col)
    plt.ylabel('개수')
    plt.show()
 
# 수치형 및 범주형 요약 데이터를 사용자에게 표시
tools.display_dataframe_to_user(name="Numeric Summary (New Data)", dataframe=numeric_summary_new)
tools.display_dataframe_to_user(name="Categorical Summary (New Data)", dataframe=categorical_summary_new)
