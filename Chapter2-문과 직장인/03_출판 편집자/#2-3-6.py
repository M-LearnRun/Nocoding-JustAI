# 데이터 로드
books_data_new = pd.read_csv(file_path_new)
 # 흑백 히트맵 시각화 (데이터 존재: 검정, 결측: 흰색)
plt.figure(figsize=(12, 10))
plt.imshow(books_data_new.isnull(), aspect='auto', cmap='binary_r', interpolation='none')

missing_count_new = books_data_new.isnull().sum()
missing_percentage_new = (missing_count_new / len(books_data_new)) * 100
