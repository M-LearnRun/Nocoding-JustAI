import matplotlib.pyplot as plt
 
# 예측값과 실제값 비교 플롯 함수
def plot_predictions_vs_actuals(y_actual, y_pred, model_name):
    plt.figure(figsize=(6, 6))
    plt.scatter(y_pred, y_actual, alpha=0.5, label=f"{model_name} Predictions")
    plt.plot([y_actual.min(), y_actual.max()], [y_actual.min(), y_actual.max()], 'r--', lw=2, label="y=x Line")
    plt.xlabel("Predicted Values")
    plt.ylabel("Actual Values (Test Set)")
    plt.title(f"{model_name} Predictions vs Actuals")
    plt.legend()
    plt.grid(True)
    plt.show()
 
# 각 모델의 예측 결과 시각화
plot_predictions_vs_actuals(y_val, y_pred_linear, "Linear Regression")
plot_predictions_vs_actuals(y_val, y_pred_rf, "Random Forest")
plot_predictions_vs_actuals(y_val, y_pred_svm, "SVM")
plot_predictions_vs_actuals(y_val, y_pred_nn, "Neural Network")
plot_predictions_vs_actuals(y_val, y_pred_knn, "KNN")
