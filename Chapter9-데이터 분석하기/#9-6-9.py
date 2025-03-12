import numpy as np
 
# Clean and preprocess data
data.rename(columns=lambda x: x.strip(), inplace=True)  # Remove extra whitespaces in column names
data['log_salary'] = np.log(data['연봉(2018)'])  # Create a log-transformed salary column
 
# Select relevant columns for clustering
clustering_data = data[['출루율', 'log_salary']].dropna()
 
# Check data types and basic statistics for clustering data
clustering_data.describe()
 
from sklearn.cluster import KMeans
 
# Perform K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
clustering_data['cluster'] = kmeans.fit_predict(clustering_data)
 
# Add cluster labels back to the original data
data = data.join(clustering_data['cluster'])
 
# Identify the cluster with high OBP and low salary
cluster_means = clustering_data.groupby('cluster').mean()
target_cluster = cluster_means[(cluster_means['출루율'] > clustering_data['출루율'].mean()) &
                                (cluster_means['log_salary'] < clustering_data['log_salary'].mean())].index
 
# Filter players in the target cluster
high_obp_low_salary_group = data[data['cluster'].isin(target_cluster)]
 
# Filter out players with games below the 25th percentile
threshold_games = high_obp_low_salary_group['경기'].quantile(0.25)
filtered_players = high_obp_low_salary_group[high_obp_low_salary_group['경기'] > threshold_games]
 
# Prepare data for visualization
filtered_players = filtered_players[['선수명', '출루율', 'log_salary', '경기']].dropna()
filtered_players['composite_score'] = filtered_players['출루율'] - 0.01 * filtered_players['log_salary']
filtered_players = filtered_players.sort_values(by='composite_score', ascending=False).reset_index(drop=True)
filtered_players['rank'] = filtered_players.index + 1
 
# Display the filtered players with rankings
import ace_tools as tools; tools.display_dataframe_to_user(name="Filtered High OBP Low Salary Players with Rankings", dataframe=filtered_players)
 
# Check data for visualization
filtered_players.head()
 
mport matplotlib.pyplot as plt
from scipy.interpolate import griddata
 
# Data for contour plot
x = filtered_players['출루율']
y = filtered_players['log_salary']
z = filtered_players['composite_score']
 
# Create grid for contour plot
X, Y = np.meshgrid(np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100))
Z = griddata(points=(x, y), values=z, xi=(X, Y), method='linear')
 
# Plot the contour
plt.figure(figsize=(12, 8))
contour = plt.contourf(X, Y, Z, levels=20, cmap="RdYlBu_r", alpha=0.8)
plt.colorbar(contour, label="Composite Score")
 
# Scatter plot with player labels
for i, player in filtered_players.iterrows():
    plt.scatter(player['출루율'], player['log_salary'], color='red', edgecolor='black', zorder=10)
    plt.text(player['출루율'], player['log_salary'], f"{player['선수명']} ({player['rank']})", fontsize=10, color='black')
 
# Axis labels and title
plt.title("2D Contour Plot of Filtered Player Rankings Based on 출루율 and 연봉(최근)", fontsize=14)
plt.xlabel("출루율", fontsize=12)
plt.ylabel("로그(연봉)", fontsize=12)
plt.grid(True)
plt.show()
