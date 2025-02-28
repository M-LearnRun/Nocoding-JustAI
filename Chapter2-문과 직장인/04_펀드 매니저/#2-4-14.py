# Applying the strategies for 'All-Investment', 'Nov-Apr', and 'May-Oct' for both KOSPI and KOSDAQ
 
# All Investment strategy (no specific months, always invested)
def apply_all_investment_strategy(df):
    df = df.copy()
    df['Investment'] = 1  # Always invested
    df['Strategy Return'] = df['Daily Return'] * df['Investment']
    df['Cumulative Return'] = (1 + df['Strategy Return']).cumprod()
    return df
 
# Nov-Apr strategy
def apply_nov_apr_strategy(df):
    return apply_custom_daily_investment_strategy(df, 11, 4)
 
# May-Oct strategy
def apply_may_oct_strategy(df):
    return apply_custom_daily_investment_strategy(df, 5, 10)
 
# KOSPI strategies
kospi_all = apply_all_investment_strategy(kospi_daily)
kospi_nov_apr = apply_nov_apr_strategy(kospi_daily)
kospi_may_oct = apply_may_oct_strategy(kospi_daily)
 
# KOSDAQ strategies
kosdaq_all = apply_all_investment_strategy(kosdaq_daily)
kosdaq_nov_apr = apply_nov_apr_strategy(kosdaq_daily)
kosdaq_may_oct = apply_may_oct_strategy(kosdaq_daily)
 
# Function to calculate MDD time series for plotting
def calculate_mdd_time_series(cumulative_returns):
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown
 
# Re-plotting the same as before but for KOSPI without subplots
 
# Plotting cumulative returns for KOSPI strategies
 
plt.figure(figsize=(10, 6))
 
plt.plot(kospi_all.index, kospi_all['Cumulative Return'], label='All Investment', color='blue')
plt.plot(kospi_nov_apr.index, kospi_nov_apr['Cumulative Return'], label='Nov-Apr', color='green')
plt.plot(kospi_may_oct.index, kospi_may_oct['Cumulative Return'], label='May-Oct', color='red')
 
plt.title('KOSPI: Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
 
plt.show()
 
# Plotting MDD for KOSPI strategies
 
plt.figure(figsize=(10, 6))
 
plt.plot(kospi_all.index, calculate_mdd_time_series(kospi_all['Cumulative Return']), label='All Investment', color='blue')
plt.plot(kospi_nov_apr.index, calculate_mdd_time_series(kospi_nov_apr['Cumulative Return']), label='Nov-Apr', color='green')
plt.plot(kospi_may_oct.index, calculate_mdd_time_series(kospi_may_oct['Cumulative Return']), label='May-Oct', color='red')
 
plt.title('KOSPI: Maximum Drawdown (MDD)')
plt.xlabel('Date')
plt.ylabel('MDD')
plt.legend()
 
plt.show()
