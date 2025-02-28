# [koreanize_matplotlib, mplfinance, FinanceDataReader 테스트 코드]
import koreanize_matplotlib
import mplfinance as mpf
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
 
# 스타일 적용 (seaborn-whitegrid 스타일)
plt.style.use("seaborn-whitegrid")
 
# koreanize_matplotlib 테스트 (한글 지원 확인)
plt.figure(figsize=(5,5))
plt.title("한글 테스트")
plt.plot([1, 2, 3], [4, 3, 2])
plt.show()
 
# mplfinance 테스트 (Apple 주식 데이터로 간단한 캔들차트 그리기)
data = fdr.DataReader('AAPL', '2023')  # Apple 주식 데이터 (2023년)
 
# mplfinance를 사용한 캔들차트 시각화
mpf.plot(data, type='candle', volume=True, style='yahoo')  # 'yahoo' 스타일 적용
