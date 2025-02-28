normal_zip_path = r'IDC_Normalized_Augmented_Normal_492.zip'
severe_zip_path = r'IDC_Normalized_Augmented_Severe_268.zip'
normal_extract_path = r'/normal_images'
severe_extract_path = r'/severe_images'
 
# 압축 파일 해제
with zipfile.ZipFile(normal_zip_path, 'r') as normal_zip_ref:
normal_zip_ref.extractall(normal_extract_path)
 
with zipfile.ZipFile(severe_zip_path, 'r') as severe_zip_ref:
severe_zip_ref.extractall(severe_extract_path)
