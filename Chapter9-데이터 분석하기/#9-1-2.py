
plt.figure(figsize=(10, 6))
sns.barplot(x='Age Group', y='Income', data=data_income, palette='Blues_d')
plt.title('Income by Age Group (Seaborn)', fontsize=15)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Income', fontsize=12)
plt.show()
