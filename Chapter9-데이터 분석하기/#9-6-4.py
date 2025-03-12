import seaborn as sns
import matplotlib.pyplot as plt
 
# Plot histogram with KDE for Process_A, Process_B, Process_C
plt.figure(figsize=(10, 6))
sns.histplot(semiconductor_data['Process_A'], kde=True, bins=15, color='orange', label='Process A', alpha=0.6)
sns.histplot(semiconductor_data['Process_B'], kde=True, bins=15, color='blue', label='Process B', alpha=0.6)
sns.histplot(semiconductor_data['Process_C'], kde=True, bins=15, color='green', label='Process C', alpha=0.6)
 
# Add labels, title, and legend
plt.title("Distribution of Processes A, B, and C (With KDE)", fontsize=14)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.legend(title="Processes")
plt.grid(alpha=0.3)
plt.tight_layout()
 
# Show the plot
plt.show()
