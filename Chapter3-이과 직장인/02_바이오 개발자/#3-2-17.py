from sklearn.metrics import confusion_matrix
 
# 혼동 행렬 생성 및 시각화
conf_matrix_final_strategy = confusion_matrix(y_test_all, y_pred_threshold_final_strategy)
plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix_final_strategy, annot=True, fmt='d', cmap='Blues', xticklabels=["Normal", "Severe"], yticklabels=["Normal", "Severe"])
plt.show()
