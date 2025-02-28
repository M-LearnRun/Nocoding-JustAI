filtered_essay_books = books_data_new[
(books_data_new['대분류'].str.contains('에세이', na=False) |
books_data_new['중분류'].str.contains('에세이', na=False) |
books_data_new['소분류'].str.contains('에세이', na=False)) &
(books_data_new['번역서원제'].isnull()) & # 번역서가 아닌 책
(books_data_new['총_리뷰_개수'] >= 10) # 100자평개수와 마이리뷰개수의 합이 10개 이상인 책
]
