import pickle
 
# 모델을 pickle 파일로 저장
model_filename = '/mnt/data/final_tuned_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(rf_clf_samples_strategy, file)
 
model_filename  # 파일 경로 반환
