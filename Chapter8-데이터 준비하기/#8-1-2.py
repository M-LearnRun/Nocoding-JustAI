import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
 
data_detailed = {
'Age (years)': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
'Annual Maintenance Costs ($)': [300, 300, 380, 480, 640, 760, 920, 1040, 1200, 1350, 1540, 1590, 1920, 2000, 1880, 1920, 2040, 2280, 2280, 2080, 2280]
}
 
df_detailed = pd.DataFrame(data_detailed)
# CSV 파일로 저장
file_detailed_path = '/mnt/data/js_based_car_maintenance_costs_by_age.csv'
df_detailed.to_csv(file_detailed_path, index=False)

# 시각화
plt.figure(figsize=(10, 6))
plt.plot(df_detailed['Age (years)'], df_detailed['Annual Maintenance Costs ($)'], marker='o', color='b', label='Maintenance Costs')
plt.title('Car Maintenance Costs by Age (Based on JavaScript Data)')
plt.xlabel('Age (years)')
plt.ylabel('Annual Maintenance Costs ($)')
plt.grid(True)
plt.legend()
plt.show()
 
file_detailed_path
