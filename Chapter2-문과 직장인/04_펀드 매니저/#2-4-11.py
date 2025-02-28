# 투자 전략의 월별 시작-종료 조건을 정의
month_pairs = [
    (1, 6), (2, 7), (3, 8), (4, 9), (5, 10), (6, 11), 
    (7, 12), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5)
]
 
# KOSPI 전략 결과 시각화
plt.figure(figsize=(10, 6))
for start_month, end_month in month_pairs:
    kospi_strategy = apply_custom_investment_strategy(kospi_backtest_with_close, start_month, end_month)
    plt.plot(kospi_strategy.index, kospi_strategy['Cumulative Return'], label=f'{start_month}-{end_month}')
 
plt.title('KOSPI 누적 수익률 (12가지 전략)')
plt.legend(loc='upper left')
plt.show()
 
# KOSDAQ 전략 결과 시각화
plt.figure(figsize=(10, 6))
for start_month, end_month in month_pairs:
    kosdaq_strategy = apply_custom_investment_strategy(kosdaq_backtest_with_close, start_month, end_month)
    plt.plot(kosdaq_strategy.index, kosdaq_strategy['Cumulative Return'], label=f'{start_month}-{end_month}')
 
plt.title('KOSDAQ 누적 수익률 (12가지 전략)')
plt.legend(loc='upper left')
plt.show()
