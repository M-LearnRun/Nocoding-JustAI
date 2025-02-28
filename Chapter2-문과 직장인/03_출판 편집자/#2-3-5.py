# Creating a new column that sums up the sales amount from the three channels
total_market_data['전체_판매금액'] = (total_market_data['대형서점_금액'] + 
total_market_data['지역서점_금액'] + 
total_market_data['온라인_금액']) / 1e8 # Converting to 100 million units
# Creating a new column that sums up the sales amount from the three channels
essay_market_data['수필_판매금액'] = (essay_market_data['대형서점_금액'] + 
essay_market_data['지역서점_금액'] + 
essay_market_data['온라인_금액']) / 1e8 # Converting to 100 million units
 
# Merging the two datasets on the sales period ('판매일') to align for visualization
merged_data = pd.merge(total_market_data[['판매일', '전체_판매금액']], 
essay_market_data[['판매일', '수필_판매금액']], 
on='판매일')
 
# Grouping the data by month to calculate the average sales for each month (to analyze seasonality)
monthly_avg_sales = merged_data.groupby(merged_data.index.month).mean()
# Renaming the index for better clarity (월)
monthly_avg_sales.index = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
 
# Adjusting the font size for the legend and all labels for better visibility
plt.figure(figsize=(10, 6))
 
fig, ax1 = plt.subplots(figsize=(12, 8))
 
# Plotting the first line for the total market average
ax1.plot(monthly_avg_sales.index, monthly_avg_sales['전체_판매금액'], color='blue', marker='o', label='전체 출판 시장')
 
# Creating a second Y-axis for the essay market average sales data
ax2 = ax1.twinx()
ax2.plot(monthly_avg_sales.index, monthly_avg_sales['수필_판매금액'], color='red', marker='o', linestyle='--', label='수필 출판 시장')
