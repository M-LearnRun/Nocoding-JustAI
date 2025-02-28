import pandas as pd
 
# Load the uploaded CSV file to inspect the contents
file_path = '/mnt/data/2024년_동료평가 결과_전직원 100명대상_원본데이터.csv'
data = pd.read_csv(file_path)
 
# Display the first few rows of the dataset to understand its structure
data.head()
