# Step 1: 원본 데이터에 인덱스 추가
data['인덱스'] = data.index
# Step 2: 비문이 포함된 데이터에도 인덱스를 그대로 유지
invalid_rows_selected['인덱스'] = invalid_rows_selected.index
# Step 3: 수정된 비문 포함 데이터 파일로 저장
invalid_rows_selected.to_csv('/mnt/data/비문_포함_행_수정본_인덱스_포함.csv', index=False, encoding='utf-8-sig')
# Step 4: 원본 데이터도 저장 (인덱스 추가한 상태로)
data.to_csv('/mnt/data/원본데이터_인덱스_포함.csv', index=False, encoding='utf-8-sig')
# 다운로드 링크 제공
('/mnt/data/비문_포함_행_수정본_인덱스_포함.csv', '/mnt/data/원본데이터_인덱스_포함.csv')
