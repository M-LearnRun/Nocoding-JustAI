import seaborn as sns
import matplotlib.pyplot as plt
 
# Select numerical columns for correlation analysis
numerical_columns = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
corr_matrix = titanic_data[numerical_columns].corr()
 
# Plot a heatmap for the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Heatmap of Numerical Variables")
plt.show()
