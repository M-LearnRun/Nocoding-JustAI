# 파일 경로 설정 및 데이터 불러오기
file_path_new = '/mnt/data/출판시장마이크로_분석_3_all_books_data_CID55889_snum500_20241008.csv'
 
# 데이터 로드
books_data_new = pd.read_csv(file_path_new)
 
# 흑백 히트맵 시각화 (데이터 존재: 검정, 결측: 흰색)
plt.figure(figsize=(12, 10))
plt.imshow(books_data_new.isnull(), aspect='auto', cmap='binary_r', interpolation='none')
plt.title('Missing Data Heatmap (White: Missing, Black: Data Present)')
plt.xlabel('Columns')
plt.ylabel('Records')
plt.show()
 
# 각 컬럼별 결측치 비율 계산
missing_count_new = books_data_new.isnull().sum()
missing_percentage_new = (missing_count_new / len(books_data_new)) * 100
 
# 결측치 비율을 데이터프레임으로 정리
missing_data_summary_new = pd.DataFrame({
    'Missing Count': missing_count_new,
    'Missing Percentage (%)': missing_percentage_new
})
 
import ace_tools as tools; tools.display_dataframe_to_user(name="Missing Data Summary (New Data)", dataframe=missing_data_summary_new)
