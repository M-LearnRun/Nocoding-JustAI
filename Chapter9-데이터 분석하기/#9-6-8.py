# 의사결정 나무로부터 예측값 생성
data_for_plot['predicted_class'] = tree_model.predict(X)
 
# 클래스별 색상 매핑 정의
quadrant_colors = {
    "높은 출루율, 높은 연봉": 'green',
    "낮은 출루율, 높은 연봉": 'red',
    "높은 출루율, 낮은 연봉": 'blue',
    "낮은 출루율, 낮은 연봉": 'purple'
}
data_for_plot['color'] = data_for_plot['predicted_class'].map(quadrant_colors)
 
# 시각화
plt.figure(figsize=(12, 8))
for predicted_class, color in quadrant_colors.items():
    class_data = data_for_plot[data_for_plot['predicted_class'] == predicted_class]
    plt.scatter(class_data['출루율'], class_data['log_salary'], c=color, label=predicted_class, alpha=0.7)
 
# 평균값 기준선 추가
plt.axvline(threshold_obp, color='black', linestyle='--', label='평균 출루율')
plt.axhline(threshold_salary, color='gray', linestyle='--', label='평균 로그 연봉')
 
# 그래프 제목과 축 설정
plt.title('출루율과 로그 변환된 연봉(최근) 기반 의사결정 나무 군집화 (영역 변경)', fontsize=14)
plt.xlabel('출루율', fontsize=12)
plt.ylabel('로그 변환 연봉 (만원)', fontsize=12)
plt.legend(title='Predicted Quadrant')
plt.grid(True)
plt.show()
