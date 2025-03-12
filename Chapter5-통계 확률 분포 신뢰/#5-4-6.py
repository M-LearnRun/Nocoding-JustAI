# 필요한 라이브러리 재임포트 및 설정
import koreanize_matplotlib
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
 
# Weibull 분포 피팅 함수 정의
def fit_weibull(data):
    shape, _, scale = stats.weibull_min.fit(data, floc=0)  # 위치 고정(floc=0)
    return shape, scale
 
# 2013년, 2020년 Weibull 분포 피팅
data_2013, data_2020 = data[data['Year'] == 2013]['Replacement Period (months)'], data[data['Year'] == 2020]['Replacement Period (months)']
shape_2013, scale_2013 = fit_weibull(data_2013)
shape_2020, scale_2020 = fit_weibull(data_2020)
 
# Weibull 확률 밀도 함수 시각화
x = np.linspace(0, max(data['Replacement Period (months)']), 100)
pdf_2013, pdf_2020 = stats.weibull_min.pdf(x, shape_2013, loc=0, scale=scale_2013), stats.weibull_min.pdf(x, shape_2020, loc=0, scale=scale_2020)
