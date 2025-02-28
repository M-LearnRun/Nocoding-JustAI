# Re-plotting the same for KOSDAQ without subplots
 
# Plotting cumulative returns for KOSDAQ strategies
 
plt.figure(figsize=(10, 6))
 
plt.plot(kosdaq_all.index, kosdaq_all['Cumulative Return'], label='All Investment', color='blue')
plt.plot(kosdaq_nov_apr.index, kosdaq_nov_apr['Cumulative Return'], label='Nov-Apr', color='green')
plt.plot(kosdaq_may_oct.index, kosdaq_may_oct['Cumulative Return'], label='May-Oct', color='red')
 
plt.title('KOSDAQ: Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
 
plt.show()
 
# Plotting MDD for KOSDAQ strategies
 
plt.figure(figsize=(10, 6))
 
plt.plot(kosdaq_all.index, calculate_mdd_time_series(kosdaq_all['Cumulative Return']), label='All Investment', color='blue')
plt.plot(kosdaq_nov_apr.index, calculate_mdd_time_series(kosdaq_nov_apr['Cumulative Return']), label='Nov-Apr', color='green')
plt.plot(kosdaq_may_oct.index, calculate_mdd_time_series(kosdaq_may_oct['Cumulative Return']), label='May-Oct', color='red')
 
plt.title('KOSDAQ: Maximum Drawdown (MDD)')
plt.xlabel('Date')
plt.ylabel('MDD')
plt.legend()
 
plt.show()
