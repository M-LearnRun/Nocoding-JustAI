fig, ax = plt.subplots(1, 2, figsize=(14, 6))
 
# 정상인 성능 비교
ax[0].bar(index, normal_metrics_default, bar_width, label='Default Model')
ax[0].bar(index + bar_width, normal_metrics_final, bar_width, label='Final Tuned Model')
ax[0].set_xticks(index + bar_width / 2)
ax[0].set_xticklabels(metrics_labels)
ax[0].legend()
 
# 환자 성능 비교
ax[1].bar(index, severe_metrics_default, bar_width, label='Default Model')
ax[1].bar(index + bar_width, severe_metrics_final, bar_width, label='Final Tuned Model')
ax[1].set_xticks(index + bar_width / 2)
ax[1].set_xticklabels(metrics_labels)
ax[1].legend()
 
plt.tight_layout()
plt.show()
