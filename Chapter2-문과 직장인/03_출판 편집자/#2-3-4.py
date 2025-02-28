# 월별로 시, 소설, 수필의 '판매 부수 합계'와 '판매 금액 합계'를 단위 조정하여 선그래프로 시각화
 
# 데이터 그룹화: 장르별로 월별 판매 부수 합계와 판매 금액 합계 계산
grouped_filtered_data = filtered_combined_data.groupby(['판매일', '장르'])[['판매 부수 합계', '판매 금액 합계']].sum().unstack()
 
# 시각화를 위해 인덱스를 리셋
grouped_filtered_data_reset = grouped_filtered_data.reset_index()
 
# 판매 금액 합계 선그래프 (1억 원 단위)
plt.figure(figsize=(12, 6))
for genre in ['시', '소설', '수필']:
    plt.plot(grouped_filtered_data_reset['판매일'], 
             grouped_filtered_data_reset[('판매 금액 합계', genre)] / 100000000,  # 1억 원 단위로 변환
             marker='o', label=f'{genre}')
 
plt.xlabel('판매일')
plt.ylabel('판매 금액 합계 (단위: 억 원)')
plt.title('장르별 판매 금액 합계 (억 원 단위)')
plt.legend()
plt.grid(True)
plt.show()
