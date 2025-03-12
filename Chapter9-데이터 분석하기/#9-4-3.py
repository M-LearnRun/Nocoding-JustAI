# 데이터 설정
labels = ['도장 결함', '조립 오류', '부품 불량', '전기 시스템 오류', '기타']
sizes = [35, 25, 20, 15, 5]  # 각 항목의 비율
colors = ['yellow', 'green', 'red', 'blue', 'grey']  # 섹션 색상
 
# 파이 차트 생성
plt.figure(figsize=(8, 6))
plt.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%',  # 비율 라벨 표시 형식
    startangle=90,  # 차트 시작 각도
    wedgeprops={'edgecolor': 'black'}  # 경계선 설정
)
plt.title("자동차 제조 공정 불량 유형 분석")  # 제목 추가
plt.show()
