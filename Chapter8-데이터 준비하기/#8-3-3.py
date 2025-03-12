# Analyze categorical variables: 'Sex', 'Pclass', 'Embarked' with 'Survived'
categorical_columns = ['Sex', 'Pclass', 'Embarked']
 
# Create pivot tables for each categorical variable with respect to 'Survived'
pivot_tables = {}
for col in categorical_columns:
    pivot_tables[col] = titanic_data.pivot_table(index=col, values='Survived', aggfunc='mean')
 
# Plot bar charts for categorical variables and survival rates
for col in categorical_columns:
    plt.figure(figsize=(8, 5))
    sns.barplot(data=titanic_data, x=col, y='Survived', ci=None)
    plt.title(f"Survival Rate by {col}")
    plt.ylabel("Survival Rate")
    plt.xlabel(col)
    plt.show()
 
# Display pivot tables for reference
pivot_tables
