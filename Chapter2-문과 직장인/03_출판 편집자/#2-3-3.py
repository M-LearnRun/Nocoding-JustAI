def clean_data(df, genre):
    # 1. 컬럼 이름 설정
    df.columns = ['판매일', '대형서점_부수', '대형서점_금액', '지역서점_부수', '지역서점_금액', '온라인_부수', '온라인_금액']
    
    # 2. 첫 번째 행(헤더)을 제거하고 인덱스 재설정
    df = df[1:].reset_index(drop=True)
    
    # 3. 장르 정보 추가
    df['장르'] = genre
    
    # 4. 콤마 제거 후 숫자 데이터를 정수형으로 변환
    df.iloc[:, 1:7] = df.iloc[:, 1:7].replace(',', '', regex=True).astype(int)
    
    return df
 
# 각 장르별 데이터프레임 정리
poetry_data_cleaned = clean_data(poetry_data, '시')
novel_data_cleaned = clean_data(novel_data, '소설')
essay_data_cleaned = clean_data(essay_data, '수필')
 
# 5. 세 개의 데이터프레임을 하나로 합치기
combined_data = pd.concat([poetry_data_cleaned, novel_data_cleaned, essay_data_cleaned], ignore_index=True)
 
# 6. 전체 판매 부수와 금액 합계 계산
combined_data['판매 부수 합계'] = combined_data[['대형서점_부수', '지역서점_부수', '온라인_부수']].sum(axis=1)
combined_data['판매 금액 합계'] = combined_data[['대형서점_금액', '지역서점_금액', '온라인_금액']].sum(axis=1)
