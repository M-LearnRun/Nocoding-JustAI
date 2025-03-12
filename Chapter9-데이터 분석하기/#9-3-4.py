import numpy as np
 
# Create a mask for the upper triangle
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
 
# Generate the heatmap with the mask applied
plt.figure(figsize=(10, 8))
sns.heatmap(
    correlation_matrix, 
    mask=mask,          # Mask the upper triangle
    annot=True,         # Display correlation coefficients
    fmt=".2f",          # Format the coefficients
    cmap="RdYlBu_r",    # Red-Yellow-Blue reversed colormap
    cbar=True,          # Display the colorbar
    square=True,        # Keep the cells square
    vmin=-1, vmax=1     # Set the color scale range
)
plt.title("Correlation Matrix of Variables (Masked Upper Triangle)")
plt.xlabel("Design Variables")
plt.ylabel("Design Variables")
plt.show()
