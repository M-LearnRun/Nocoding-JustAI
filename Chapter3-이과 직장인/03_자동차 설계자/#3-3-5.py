def detect_outliers(data, group_name):
    # 표준화 수행
    scaler = StandardScaler()
    standardized_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
 
    # 특정 그룹의 데이터 선택
    step_freq_data = standardized_data[[col for col in data.columns if group_name in col]]
 
    # IQR 방식으로 이상치 탐지
    Q1, Q3 = step_freq_data.quantile(0.25), step_freq_data.quantile(0.75)
    IQR = Q3 - Q1
    outliers = (step_freq_data < (Q1 - 1.5 * IQR)) | (step_freq_data > (Q3 + 1.5 * IQR))
 
    return step_freq_data[outliers.any(axis=1)]
