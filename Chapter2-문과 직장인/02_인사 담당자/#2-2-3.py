# 저장할 파일 경로 지정
output_file_path = '/mnt/data/2024년_동료평가_비문여부_추가.csv'
# 수정된 데이터프레임을 CSV 파일로 저장
data.to_csv(output_file_path_bom, index=False, encoding='utf-8-sig')
# 다운로드 링크 제공
output_file_path
