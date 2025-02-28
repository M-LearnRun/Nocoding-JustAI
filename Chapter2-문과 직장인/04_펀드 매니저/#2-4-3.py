import FinanceDataReader as fdr
import mplfinance as mpf
import matplotlib.pyplot as plt
 
# KOSPI 및 KOSDAQ 전체 데이터 다운로드
kospi_data_full = fdr.DataReader('KS11')  # KOSPI 지수 전체 데이터
kosdaq_data_full = fdr.DataReader('KQ11')  # KOSDAQ 지수 전체 데이터
 
# 스타일 설정 (seaborn-whitegrid 스타일)
plt.style.use("seaborn-whitegrid")
 
# KOSPI 캔들차트 시각화
mpf.plot(kospi_data_full, type='candle', style='charles', title='KOSPI 지수 캔들차트 (전체 데이터)', volume=True,
         figratio=(16, 9), figscale=1.2, mav=(20, 60), tight_layout=True)
 
# KOSDAQ 캔들차트 시각화
mpf.plot(kosdaq_data_full, type='candle', style='charles', title='KOSDAQ 지수 캔들차트 (전체 데이터)', volume=True,
         figratio=(16, 9), figscale=1.2, mav=(20, 60), tight_layout=True)
