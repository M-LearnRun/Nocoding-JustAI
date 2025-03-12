# [mplfinance 모듈로 캔들스틱 차트 생성 - 60일과 120일 이동평균선 추가]
# Date 열을 datetime 형식으로 변환 및 설정
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
stock_data.set_index('Date', inplace=True)
 
# 60일 및 120일 이동평균선 추가
stock_data['SMA60'] = stock_data['Close'].rolling(window=60).mean()
stock_data['SMA120'] = stock_data['Close'].rolling(window=120).mean()
 
# 최근 1년 데이터 필터링
recent_data = stock_data.tail(252)
 
# 캔들스틱 차트 스타일 설정
custom_style = mpf.make_mpf_style(base_mpf_style='yahoo', gridcolor='lightgray')
 
# 캔들스틱 차트 생성
mpf.plot(
    recent_data,
    type='candle',
    mav=(60, 120),  # 60일과 120일 이동평균선 추가
    volume=True,  # 거래량 추가
    title='AAPL Candlestick Chart with 60-Day and 120-Day Moving Averages',
    ylabel='Price',
    ylabel_lower='Volume ($10^6$)',
    style=custom_style,
    figsize=(12, 8)
)
