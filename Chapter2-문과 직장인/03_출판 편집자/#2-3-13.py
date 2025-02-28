# 출판 월에 따른 세일즈포인트 시각화를 위해 출판일을 datetime 형태로 변환
data_500['출판일'] = pd.to_datetime(data_500['출판일'], errors='coerce')
 
# 출판 월을 추출하여 새로운 컬럼 생성
data_500['출판월'] = data_500['출판일'].dt.month
 
# 출판 월별 세일즈포인트의 평균 계산
monthly_sales_points_500 = data_500.groupby('출판월')['세일즈포인트'].mean()
 
# 출판 월에 따른 세일즈포인트 시각화
plt.figure(figsize=(10, 6))
monthly_sales_points_500.plot(kind='bar', color='skyblue', edgecolor='black')
