# Import necessary libraries
import pandas as pd

# Specify the dataset path
file_path = 'C:/Users/Matias/ecommerce_dataset_updated.csv'

# Load the dataset
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Display basic information about the dataset
print("\nDataset information:")
print(data.info())

# Check for missing values
print("\nMissing values in the dataset:")
print(data.isnull().sum())