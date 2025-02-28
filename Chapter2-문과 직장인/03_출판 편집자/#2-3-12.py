upper_half = data[data['세일즈포인트'] >= median_value]
lower_half = data[data['세일즈포인트'] < median_value]
 
# 상위 50%와 하위 50%의 평균치를 데이터프레임으로 정리
comparison_df = pd.DataFrame({
'상위 50% 평균': upper_half_means,
'하위 50% 평균': lower_half_means
})
# 1. 남녀/세대 구분 막대 그래프 시각화
# 남녀/세대 구분 데이터프레임 생성 (상위 50%와 하위 50% 평균)
comparison_gender_age_df = pd.DataFrame({
'상위 50% 평균': upper_half[gender_age_columns].mean(),
'하위 50% 평균': lower_half[gender_age_columns].mean()
})
comparison_gender_age_df.plot(kind='bar', figsize=(12, 8), edgecolor='black')
 
# 2. 평점 분포 막대 그래프 시각화
# 평점 분포 관련 열들만 추출하여 상위 50%와 하위 50% 평균 계산
comparison_rating_df = pd.DataFrame({
'상위 50% 평균': upper_half[rating_columns].mean(),
'하위 50% 평균': lower_half[rating_columns].mean()})

# 시각화
comparison_rating_df.plot(kind='bar', figsize=(12, 8), edgecolor='black')
 
# 3. 나머지 정량 평가 가능한 컬럼들 시각화 (세일즈포인트 제외, 상대 크기만 표시)
# 세일즈포인트를 제외한 나머지 정량 평가 컬럼 선택
remaining_columns_no_sales = [col for col in remaining_columns if col != '세일즈포인트']
remaining_comparison_no_sales = pd.DataFrame({
'상위 50% 평균': upper_half[remaining_columns_no_sales].mean(),
'하위 50% 평균': lower_half[remaining_columns_no_sales].mean()
})
relative_remaining_comparison_no_sales = (remaining_comparison_no_sales['상위 50% 평균'] / 
remaining_comparison_no_sales['하위 50% 평균']) * 100
fig, ax = plt.subplots(figsize=(12, 6))
# 하위 50%를 100으로 했을 때 상위 50%의 상대 크기 막대 그래프
relative_remaining_comparison_no_sales.plot(kind='bar', color='skyblue', ax=ax, edgecolor='black')
ax.axhline(100, color='red', linestyle='--', linewidth=1, label='하위 50% 기준 (100)')
ax.bar(relative_remaining_comparison_no_sales.index, 100, color='lightcoral', alpha=0.3, label='하위 50% (기준)')
