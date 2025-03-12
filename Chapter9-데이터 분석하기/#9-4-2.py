# 히스토그램 생성: bins=5
plt.figure(figsize=(8, 6))
plt.hist(
    histogram_data['Error Value'],
    bins=5,  # bins를 5로 설정
    color='skyblue',
    edgecolor='black',
    alpha=0.7
)
plt.title("Histogram of Automotive Length Measurement Errors (Bins=5)")
plt.xlabel("Error Value (mm)")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)
plt.show()
 
# 히스토그램 생성: bins=30
plt.figure(figsize=(8, 6))
plt.hist(
    histogram_data['Error Value'],
    bins=30,  # bins를 30으로 설정
    color='skyblue',
    edgecolor='black',
    alpha=0.7
)
plt.title("Histogram of Automotive Length Measurement Errors (Bins=30)")
plt.xlabel("Error Value (mm)")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)
plt.show()
 
# 히스토그램 생성: bins=200
plt.figure(figsize=(8, 6))
plt.hist(
    histogram_data['Error Value'],
    bins=200,  # bins를 200으로 설정
    color='skyblue',
    edgecolor='black',
    alpha=0.7
)
plt.title("Histogram of Automotive Length Measurement Errors (Bins=200)")
plt.xlabel("Error Value (mm)")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)
plt.show()
