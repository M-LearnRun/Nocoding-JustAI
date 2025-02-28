rf_clf_final_threshold_strategy = RandomForestClassifier(
    n_estimators=100,
    min_samples_split=10,
    min_samples_leaf=5,
    max_depth=None,  # 깊이 제한 없음
    max_features='sqrt',
    class_weight='balanced',
    random_state=42)
# 모델 학습
rf_clf_final_threshold_strategy.fit(X_train_all, y_train_all)
# 예측 및 성능 평가 (Threshold = 0.4 적용)
y_pred_proba_final_strategy = rf_clf_final_threshold_strategy.predict_proba(X_test_all)[:, 1]
threshold = 0.4
y_pred_threshold_final_strategy = (y_pred_proba_final_strategy >= threshold).astype(int)
# 성능 평가 보고서 출력
classification_rep_final_threshold_strategy = classification_report(y_test_all, y_pred_threshold_final_strategy, target_names=["Normal", "Severe"])
