def weibull_prob_transform_log10(cdf):
    # log10을 사용해 cdf 값을 Weibull 확률축에 맞게 변환
    return np.log10(np.log10(1 / (1 - cdf)))
 
# 2013년과 2020년 데이터에 Weibull 확률 변환 적용 (log10)
y_transformed_2013_log10 = weibull_prob_transform_log10(cdf_2013)
y_transformed_2020_log10 = weibull_prob_transform_log10(cdf_2020)
 
# 실제 데이터의 변환된 Y축 값 (log10 변환)
y_transformed_data_2013_log10 = weibull_prob_transform_log10(cdf_data_2013)
y_transformed_data_2020_log10 = weibull_prob_transform_log10(cdf_data_2020)
