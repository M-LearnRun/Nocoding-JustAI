import matplotlib.pyplot as plt
 
plt.figure(figsize=(10, 6))
plt.bar(data_income['Age Group'], data_income['Income'], color='blue')
plt.title('Income by Age Group (Matplotlib)', fontsize=15)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Income', fontsize=12)
plt.grid(True)
plt.show()
