import pandas as pd
 
# Load the uploaded file to inspect and analyze missing values
file_path = '/mnt/data/출판시장마이크로_분석_3_all_books_data_CID55889_snum500_20241008.csv'
data = pd.read_csv(file_path)
 
# Calculate the percentage of missing values for each column
missing_percentage = (data.isnull().sum() / len(data)) * 100
 
# Sort the missing percentages in descending order
missing_percentage_sorted = missing_percentage.sort_values(ascending=False)
 
# Display the missing percentages for the user
missing_percentage_sorted
