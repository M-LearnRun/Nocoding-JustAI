# Dropping rows with any NaN values to create a new dataset
cleaned_data = data.dropna()
 
# Verifying the shape of the cleaned dataset
cleaned_data_shape = cleaned_data.shape
 
# Saving the cleaned dataset to a CSV file for download
cleaned_file_path = '/mnt/data/cleaned_data.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)
