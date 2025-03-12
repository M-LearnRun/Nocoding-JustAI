# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
# Load the dataset
file_path = '/mnt/data/히트맵, 페어 플롯 - 엔진 시험 평가 데이터.csv'
data = pd.read_csv(file_path)
 
# Calculate the correlation matrix
correlation_matrix = data.corr()
 
# Generate the heatmap with the "RdYlBu_r" colormap and range from -1 to 1
plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix, 
    annot=True,          # Display correlation coefficients
    fmt=".2f",           # Format the coefficients
    cmap="RdYlBu_r",     # Red-Yellow-Blue reversed colormap
    cbar=True,           # Display the colorbar
    square=True,         # Keep the cells square
    vmin=-1, vmax=1      # Set the color scale range
)
plt.title("Correlation Matrix of Variables (RdYlBu_r Colormap)")
plt.xlabel("Design Variables")
plt.ylabel("Design Variables")
plt.show()
