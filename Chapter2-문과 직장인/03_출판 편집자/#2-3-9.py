# 다변량 EDA: 전체 히트맵 시각화
plt.figure(figsize=(15, 12))
corr = books_data_new.corr()  # 수치형 열에 대한 상관관계 계산
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='gray')
plt.title('전체 히트맵 (상관관계)')
plt.show()
