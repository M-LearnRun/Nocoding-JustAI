# [11월~4월 투자 전략 적용: KOSPI 및 KOSDAQ]
def apply_custom_strategy(df, start_month, end_month):
    df = df.copy()
    # 설정한 기간에 따른 투자 전략 생성 (투자할 경우 1, 아닐 경우 0)
    df['Investment'] = ((df.index.month >= start_month) | (df.index.month <= end_month)).astype(int)
    # 전략에 따른 수익률 계산
    df['Strategy Return'] = df['Monthly Return'] * df['Investment']
    # 누적 수익률 계산
    df['Cumulative Return'] = (1 + df['Strategy Return']).cumprod()
    return df
 
# KOSPI와 KOSDAQ의 사용자 정의 전략 적용 (1월부터 6월까지 투자)
kospi_custom_strategy = apply_custom_strategy(kospi_backtest_with_close, 1, 6)
kosdaq_custom_strategy = apply_custom_strategy(kosdaq_backtest_with_close, 1, 6)
 
# 결과 시각화
plt.figure(figsize=(10, 6))
plt.plot(kospi_custom_strategy.index, kospi_custom_strategy['Cumulative Return'], label='KOSPI', color='blue')
plt.plot(kosdaq_custom_strategy.index, kosdaq_custom_strategy['Cumulative Return'], label='KOSDAQ', color='red')
plt.title('Custom Strategy: Investing from November to April (KOSPI vs KOSDAQ)')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.show()
