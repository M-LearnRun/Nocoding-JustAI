import cv2
import os
 
# 수동 증강 및 이미지 저장 함수
def manual_augment_and_save_images(input_dir, output_dir, target_count):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
 
    image_files = os.listdir(input_dir)
    current_count = len(image_files)
    multiplier = target_count // current_count  # 필요한 증강 횟수 계산
 
    def apply_augmentations(img):
        augmented_images = []
        # 랜덤 회전 적용
        for angle in [-10, 10]:
            (h, w) = img.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated = cv2.warpAffine(img, M, (w, h))
            augmented_images.append(rotated)
        # 좌우 반전
        flipped = cv2.flip(img, 1)
        augmented_images.append(flipped)
        # 랜덤 확대/축소 (5% 비율로)
        for scale in [0.95, 1.05]:
            resized = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
            if resized.shape != img.shape:
                resized = cv2.resize(resized, (img.shape[1], img.shape[0]))
            augmented_images.append(resized)
        # 밝기 조정
        for brightness in [0.8, 1.2]:
            bright = cv2.convertScaleAbs(img, alpha=brightness, beta=0)
            augmented_images.append(bright)
 
        return augmented_images

# 이미지 증강 및 저장
    img_count = 0
    for file in image_files:
        img = cv2.imread(os.path.join(input_dir, file), cv2.IMREAD_GRAYSCALE)
 
        # 원본 이미지 저장
        cv2.imwrite(os.path.join(output_dir, f"original_{img_count}.png"), img)
        img_count += 1
 
        # 증강 적용 및 저장
        augmented_imgs = apply_augmentations(img)
        for aug_img in augmented_imgs[:multiplier-1]:  # 필요한 증강 횟수만 적용
            cv2.imwrite(os.path.join(output_dir, f"aug_{img_count}.png"), aug_img)
            img_count += 1
            if img_count >= target_count:
                break
        if img_count >= target_count:
            break
 
# 정상 및 중증 데이터셋에 수동 증강 적용
manual_augment_and_save_images(resized_normal_16bit_dir, '/mnt/data/Augmented_Normal/', 370)
manual_augment_and_save_images(resized_severe_16bit_dir, '/mnt/data/Augmented_Severe/', 240)
 
# 생성된 증강 이미지 수 확인
len(os.listdir('/mnt/data/Augmented_Normal/')), len(os.listdir('/mnt/data/Augmented_Severe/'))
