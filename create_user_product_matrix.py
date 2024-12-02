import pandas as pd

# Load the dataset
file_path = 'C:/Users/Matias/ecommerce_dataset_updated.csv'
data = pd.read_csv(file_path)

# Create a pivot table for user-product interactions
user_product_matrix = data.pivot_table(
    index='User_ID',       # Rows: Users
    columns='Product_ID',  # Columns: Products
    values='Final_Price(Rs.)',  # Values: Final price of purchased products
    aggfunc='sum',         # Aggregation function: Sum up the values
    fill_value=0           # Fill missing values with 0
)

# Save the pivot table as a CSV file
user_product_matrix.to_csv('user_product_matrix.csv')

# Print the first few rows of the matrix
print(user_product_matrix.head())  # Print the first few rows of the matrix