from sklearn.preprocessing import StandardScaler
 
def grouped_standardized_boxplot(data):
    # 그룹핑 규칙 설정 (비슷한 이름들끼리 그룹화)
    groups = {
        'ROOF_RAIL': [col for col in data.columns if 'ROOF_RAIL' in col],
        'ROOF_XMBR': [col for col in data.columns if 'ROOF_XMBR' in col],
        'BPOST': [col for col in data.columns if 'BPOST' in col],
        'R_SUPT': [col for col in data.columns if 'R_SUPT' in col],
        # (...) 나머지 그룹 생략
    }
 
    # 표준화 수행
    scaler = StandardScaler()
    standardized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
 
    # 각 그룹에 대해 박스 플롯 그리기
    for group_name, group_columns in groups.items():
        if group_columns:
            standardized_data[group_columns].boxplot()
            plt.show()
 
# 박스 플롯 실행 예시 생략 
