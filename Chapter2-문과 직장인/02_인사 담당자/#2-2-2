import re
 
# 비문 및 부적절한 표현 패턴
invalid_patterns = ['ㅋ{2,}', 'XX', '또라이', '개XX', '개', '미친', '거칠지 않냐']
 
# 욕설 및 비문 탐지 함수
def detect_invalid_text(text, profanity_list, invalid_patterns):
    for profanity in profanity_list:
        if profanity in text:
            return True
    for pattern in invalid_patterns:
        if re.search(pattern, text):
            return True
    return False
 
# '잘하는 점'과 '개선할 점'에 욕설 또는 비문이 포함된 행 필터링
invalid_rows = data[
    (data['잘하는 점'].apply(lambda x: detect_invalid_text(str(x), profanity_list, invalid_patterns))) |
    (data['개선할 점'].apply(lambda x: detect_invalid_text(str(x), profanity_list, invalid_patterns)))
]
 
# 사용자에게 필터링된 행을 보여줌
tools.display_dataframe_to_user(name="욕설 및 비문 포함 행", dataframe=invalid_rows)
