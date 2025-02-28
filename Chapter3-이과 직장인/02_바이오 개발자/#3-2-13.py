import numpy as np
import os
 
# 이미지 정규화 함수 호출
normalize_images('/mnt/data/Augmented_Normal/', normalized_normal_dir)
normalize_images('/mnt/data/Augmented_Severe/', normalized_severe_dir)
 
# 정규화된 이미지 개수 확인
len(os.listdir(normalized_normal_dir)), len(os.listdir(normalized_severe_dir))
