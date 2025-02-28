# CAGR(연평균 복합 성장률)을 계산하는 함수
def calculate_cagr(cumulative_returns, periods_per_year=252):  # 1년에 252일 거래 기준
    total_periods = len(cumulative_returns)
    end_value = cumulative_returns.iloc[-1]
    start_value = cumulative_returns.iloc[0]
    return (end_value / start_value) ** (periods_per_year / total_periods) - 1
 
# 각 전략에 대해 CAGR, MDD, MAC 계산
kospi_perf_results = {}
kosdaq_perf_results = {}
 
for start_month, end_month in month_pairs:
    kospi_strategy = apply_custom_daily_investment_strategy(kospi_daily, start_month, end_month)
    kospi_cagr = calculate_cagr(kospi_strategy['Cumulative Return'])
    kospi_mdd = calculate_mdd(kospi_strategy['Cumulative Return'])
    kospi_mac = kospi_cagr / abs(kospi_mdd) if kospi_mdd != 0 else float('inf')
    kospi_perf_results[f'{start_month}-{end_month}'] = {'CAGR': kospi_cagr, 'MDD': kospi_mdd, 'MAC': kospi_mac}
 
    kosdaq_strategy = apply_custom_daily_investment_strategy(kosdaq_daily, start_month, end_month)
    kosdaq_cagr = calculate_cagr(kosdaq_strategy['Cumulative Return'])
    kosdaq_mdd = calculate_mdd(kosdaq_strategy['Cumulative Return'])
    kosdaq_mac = kosdaq_cagr / abs(kosdaq_mdd) if kosdaq_mdd != 0 else float('inf')
    kosdaq_perf_results[f'{start_month}-{end_month}'] = {'CAGR': kosdaq_cagr, 'MDD': kosdaq_mdd, 'MAC': kosdaq_mac}

# KOSPI 및 KOSDAQ 성과 지표(CAGR, MDD, MAC)를 시각화하여 쉽게 비교
kospi_perf_df = pd.DataFrame.from_dict(kospi_perf_results, orient='index')
kosdaq_perf_df = pd.DataFrame.from_dict(kosdaq_perf_results, orient='index')
 
# KOSPI 성과 지표 시각화
fig, axs = plt.subplots(3, 1, figsize=(10, 15))
 
# KOSPI CAGR
kospi_perf_df['CAGR'].plot(kind='bar', ax=axs[0], color='darkred')
axs[0].set_title('KOSPI CAGR for 12 Strategies')
axs[0].set_ylabel('CAGR')
 
# KOSPI MDD
kospi_perf_df['MDD'].plot(kind='bar', ax=axs[1], color='firebrick')
axs[1].set_title('KOSPI MDD for 12 Strategies')
axs[1].set_ylabel('MDD')
 
# KOSPI MAC
kospi_perf_df['MAC'].plot(kind='bar', ax=axs[2], color='lightcoral')
axs[2].set_title('KOSPI MAC (CAGR / MDD) for 12 Strategies')
axs[2].set_ylabel('MAC')
 
plt.tight_layout()
plt.show()
 
# KOSDAQ 성과 지표 시각화
fig, axs = plt.subplots(3, 1, figsize=(10, 15))
 
# KOSDAQ CAGR
kosdaq_perf_df['CAGR'].plot(kind='bar', ax=axs[0], color='darkblue')
axs[0].set_title('KOSDAQ CAGR for 12 Strategies')
axs[0].set_ylabel('CAGR')
 
# KOSDAQ MDD
kosdaq_perf_df['MDD'].plot(kind='bar', ax=axs[1], color='royalblue')
axs[1].set_title('KOSDAQ MDD for 12 Strategies')
axs[1].set_ylabel('MDD')
 
# KOSDAQ MAC
kosdaq_perf_df['MAC'].plot(kind='bar', ax=axs[2], color='lightblue')
axs[2].set_title('KOSDAQ MAC (CAGR / MDD) for 12 Strategies')
axs[2].set_ylabel('MAC')
 
plt.tight_layout()
plt.show()
