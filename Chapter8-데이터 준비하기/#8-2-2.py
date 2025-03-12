# 각 피처에 대한 결측치 비율 계산
missing_percentage = data.isnull().sum() / len(data) * 100  
 
# 결측치가 있는 피처만 필터링하여 표시
missing_percentage = missing_percentage[missing_percentage > 0]
 
# 결과를 테이블 형태로 사용자에게 표시
import ace_tools as tools
tools.display_dataframe_to_user(name="Missing Data Percentage", dataframe=missing_percentage)
 
# 결측치 비율 출력
missing_percentage  # 결과 출력
