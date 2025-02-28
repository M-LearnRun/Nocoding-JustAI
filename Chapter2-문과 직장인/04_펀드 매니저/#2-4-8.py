# 4x3 그리드를 사용하여 KOSPI 및 KOSDAQ의 월별 수익률 분포를 시각화
# KOSPI 분포
plt.figure(figsize=(18, 12))
for month in range(1, 13):
    plt.subplot(4, 3, month)
    kospi_data_month = kospi_pivot[month].dropna()  # 해당 월의 KOSPI 수익률
    plt.hist(kospi_data_month, bins=20, color='blue', edgecolor='black', alpha=0.7)
    plt.title(f'KOSPI {month_names[month-1]}')
    plt.xlim(lower_bound, upper_bound)  # X축 한계를 동일하게 설정
    plt.axvline(x=0, color='red', linestyle='dashed')  # 0 기준선을 빨간색 점선으로 표시
plt.tight_layout()
plt.show()
 
# KOSDAQ 분포
plt.figure(figsize=(18, 12))
for month in range(1, 13):
    plt.subplot(4, 3, month)
    kosdaq_data_month = kosdaq_pivot[month].dropna()  # 해당 월의 KOSDAQ 수익률
    plt.hist(kosdaq_data_month, bins=20, color='red', edgecolor='black', alpha=0.7)
    plt.title(f'KOSDAQ {month_names[month-1]}')
    plt.xlim(lower_bound, upper_bound)  # X축 한계를 동일하게 설정
    plt.axvline(x=0, color='red', linestyle='dashed')  # 0 기준선을 빨간색 점선으로 표시
plt.tight_layout()
plt.show()
