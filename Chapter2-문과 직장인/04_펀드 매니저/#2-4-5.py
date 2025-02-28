#Step1: 데이터 로드 및 날짜 처리
import pandas as pd
 
# KOSPI와 KOSDAQ 데이터를 로드
kospi_data = pd.read_csv('/mnt/data/TimeSeries_1_KOSPI_1_rawdata_full.csv')
kosdaq_data = pd.read_csv('/mnt/data/TimeSeries_1_KOSDAQ_1_rawdata_full.csv.csv')
 
# 'Date' 열을 datetime 형식으로 변환 후 인덱스로 설정
kospi_data['Date'] = pd.to_datetime(kospi_data['Date'])
kospi_data.set_index('Date', inplace=True)
 
kosdaq_data['Date'] = pd.to_datetime(kosdaq_data['Date'])
kosdaq_data.set_index('Date', inplace=True)
 
# 데이터 구조 확인
kospi_data.head(), kosdaq_data.head()
 
#Step2: 월별 수익률 계산 함수 정의
import datetime as dt
 
# 주어진 데이터프레임에서 월별 수익률을 계산하는 함수
def calculate_monthly_returns(df):
    # 월별로 마지막 날짜의 데이터를 추출
    monthly_data = df.resample('M').last()
    # 'Close' 열을 기준으로 월별 수익률 계산
    monthly_data['Monthly Return'] = (monthly_data['Close'] / monthly_data['Close'].shift(1)) - 1
    return monthly_data
 
# KOSPI와 KOSDAQ의 월별 수익률 계산
kospi_monthly_returns = calculate_monthly_returns(kospi_data)
kosdaq_monthly_returns = calculate_monthly_returns(kosdaq_data)
 
# 결과 출력
import ace_tools as tools
tools.display_dataframe_to_user(name="KOSPI Monthly Returns", dataframe=kospi_monthly_returns)
tools.display_dataframe_to_user(name="KOSDAQ Monthly Returns", dataframe=kosdaq_monthly_returns)
