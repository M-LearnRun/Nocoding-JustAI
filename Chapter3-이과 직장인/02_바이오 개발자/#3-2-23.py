# 이미지 로드 함수
def load_images(image_path, label, image_size=(256, 256)):
images = []
labels = []
for filename in os.listdir(image_path):
img_path = os.path.join(image_path, filename)
img = Image.open(img_path).convert('L') # 그레이스케일 변환
img = img.resize(image_size)
img_array = np.array(img) / 255.0 # 0-1 사이로 정규화
images.append(img_array)
labels.append(label)
return np.array(images), np.array(labels)
 
# 정상 및 중증 환자 이미지 불러오기
normal_images, normal_labels = load_images(normal_extract_path, 0) 
severe_images, severe_labels = load_images(severe_extract_path, 1) 
 
# 데이터셋 합치기
X = np.concatenate((normal_images, severe_images), axis=0)
y = np.concatenate((normal_labels, severe_labels), axis=0)
X = X.reshape(-1, 256, 256, 1)
 
# 학습/테스트 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# 라벨 원-핫 인코딩
y_train = to_categorical(y_train, 2)
y_test  = to_categorical(y_test, 2)
 
# CNN 모델 정의
model = Sequential([
Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 1)),
MaxPooling2D(pool_size=(2, 2)),
Conv2D(64, (3, 3), activation='relu'),
MaxPooling2D(pool_size=(2, 2)),
Conv2D(128, (3, 3), activation='relu'),
MaxPooling2D(pool_size=(2, 2)),
Flatten(),
Dense(128, activation='relu'),
Dropout(0.5),
Dense(2, activation='softmax') # 2개의 클래스(정상 및 환자)
])
 
# 모델 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
