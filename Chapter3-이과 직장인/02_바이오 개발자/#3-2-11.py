import cv2
import os
 
# 목표 수량까지 추가 증강 함수
def augment_until_target(input_dir, output_dir, current_count, target_count):
    image_files = os.listdir(input_dir)
 
    def apply_augmentations(img):
        augmented_images = []
        # 회전, 반전, 확대/축소, 밝기 조정
        for angle in [-10, 10]:
            M = cv2.getRotationMatrix2D((img.shape[1] // 2, img.shape[0] // 2), angle, 1.0)
            augmented_images.append(cv2.warpAffine(img, M, (img.shape[1], img.shape[0])))
        augmented_images.append(cv2.flip(img, 1))
        for scale in [0.95, 1.05]:
            resized = cv2.resize(img, None, fx=scale, fy=scale)
            if resized.shape != img.shape:
                resized = cv2.resize(resized, (img.shape[1], img.shape[0]))
            augmented_images.append(resized)
        for brightness in [0.8, 1.2]:
            augmented_images.append(cv2.convertScaleAbs(img, alpha=brightness, beta=0))
        return augmented_images
 
    # 목표 수량 도달까지 증강
    img_count = current_count
    while img_count < target_count:
        for file in image_files:
            img = cv2.imread(os.path.join(input_dir, file), cv2.IMREAD_GRAYSCALE)
            for aug_img in apply_augmentations(img):
                cv2.imwrite(os.path.join(output_dir, f"aug_{img_count}.png"), aug_img)
                img_count += 1
                if img_count >= target_count:
                    break
            if img_count >= target_count:
                break
 
# 정상 및 중증 데이터셋에서 목표 수량 증강 적용
augment_until_target(resized_normal_16bit_dir, '/mnt/data/Augmented_Normal/', 297, 492)
augment_until_target(resized_severe_16bit_dir, '/mnt/data/Augmented_Severe/', 204, 268)
 
# 생성된 증강 이미지 수 확인
len(os.listdir('/mnt/data/Augmented_Normal/')), len(os.listdir('/mnt/data/Augmented_Severe/'))
