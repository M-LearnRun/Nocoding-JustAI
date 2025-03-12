# Process_A, Process_B, Process_C에 대해 성능 P와의 민감도 분석
plt.figure(figsize=(10, 6))
 
# Process_A vs Performance_P
sns.regplot(
    x=semiconductor_data['Process_A'], 
    y=semiconductor_data['Performance_P'], 
    color='orange', 
    label='Process A', 
    scatter_kws={'alpha': 0.6, 'marker': '+'},  # '+' 마커 적용
    line_kws={'linewidth': 2}
)
 
# Process_B vs Performance_P
sns.regplot(
    x=semiconductor_data['Process_B'], 
    y=semiconductor_data['Performance_P'], 
    color='blue', 
    label='Process B', 
    scatter_kws={'alpha': 0.6, 'marker': '+'},  # '+' 마커 적용
    line_kws={'linewidth': 2}
)
 
# Process_C vs Performance_P
sns.regplot(
    x=semiconductor_data['Process_C'], 
    y=semiconductor_data['Performance_P'], 
    color='green', 
    label='Process C', 
    scatter_kws={'alpha': 0.6, 'marker': '+'},  # '+' 마커 적용
    line_kws={'linewidth': 2}
)
 
# 그래프 제목, 축 레이블, 범례 추가
plt.title("Processes A, B, C vs Performance P (Sensitivity Analysis)", fontsize=14)
plt.xlabel("Process Value", fontsize=12)
plt.ylabel("Performance P", fontsize=12)
plt.legend(title="Processes")
plt.grid(alpha=0.3)
plt.tight_layout()
 
# 그래프 출력
plt.show()
