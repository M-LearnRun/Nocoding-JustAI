# 일일 수익률 계산 함수
def calculate_daily_returns(df):
    df['Daily Return'] = df['Close'].pct_change()  # 'Close' 가격의 변동률 계산
    df.dropna(inplace=True)  # 결측치 제거
    return df
 
# KOSPI와 KOSDAQ 데이터에 일일 수익률 계산 적용
kospi_daily = calculate_daily_returns(kospi_data)
kosdaq_daily = calculate_daily_returns(kosdaq_data)
 
# 맞춤형 일일 투자 전략 적용 함수
def apply_custom_daily_investment_strategy(df, start_month, end_month):
    df['Investment'] = ((df.index.month >= start_month) & (df.index.month <= end_month)).astype(int) if start_month <= end_month else \
                       ((df.index.month >= start_month) | (df.index.month <= end_month)).astype(int)
    df['Strategy Return'] = df['Daily Return'] * df['Investment']  # 전략에 따른 수익률 계산
    df['Cumulative Return'] = (1 + df['Strategy Return']).cumprod()  # 누적 수익률 계산
    return df

# KOSPI와 KOSDAQ에 일일 수익률을 이용한 맞춤형 투자 전략 적용
kospi_custom_daily_strategy = apply_custom_daily_investment_strategy(kospi_daily, 1, 6)
kosdaq_custom_daily_strategy = apply_custom_daily_investment_strategy(kosdaq_daily, 1, 6)
 
# KOSPI의 12가지 전략을 하나의 그래프에 표시 (일일 수익률 사용)
plt.figure()
for start_month, end_month in month_pairs:
    kospi_strategy = apply_custom_daily_investment_strategy(kospi_daily, start_month, end_month)
    plt.plot(kospi_strategy.index, kospi_strategy['Cumulative Return'])
plt.show()
 
# KOSDAQ의 12가지 전략을 하나의 그래프에 표시 (일일 수익률 사용)
plt.figure()
for start_month, end_month in month_pairs:
    kosdaq_strategy = apply_custom_daily_investment_strategy(kosdaq_daily, start_month, end_month)
    plt.plot(kosdaq_strategy.index, kosdaq_strategy['Cumulative Return'])
plt.show()
