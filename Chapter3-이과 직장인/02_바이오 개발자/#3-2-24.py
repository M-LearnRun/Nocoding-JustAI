# 데이터 증강을 위한 ImageDataGenerator
datagen = ImageDataGenerator(rotation_range=10, zoom_range=0.1, width_shift_range=0.1, height_shift_range=0.1)
datagen.fit(X_train)
 
# 모델 학습
history = model.fit(datagen.flow(X_train, y_train, batch_size=32), validation_data=(X_test, y_test), epochs=10)
 
# 모델 성능 시각화
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
 
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
 
# 모델 저장
model.save('cnn_image_classification_model.h5')
 
# 테스트 데이터로 예측
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)
 
# 성능 평가
from sklearn.metrics import classification_report, confusion_matrix
print("Classification Report:")
print(classification_report(true_classes, predicted_classes, target_names=["Normal", "Severe"]))
 
print("Confusion Matrix:")
print(confusion_matrix(true_classes, predicted_classes))
