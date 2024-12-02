import pandas as pd

# Load the user-product matrix
user_product_matrix = pd.read_csv('user_product_matrix.csv', index_col=0)

# 1. Analyze purchases per product
product_purchases = user_product_matrix.astype(bool).sum(axis=0)
print("Number of purchases per product:")
print(product_purchases.describe())

# Optional: Least purchased products
print("\nProducts with the least purchases:")
print(product_purchases[product_purchases == 0])

# 2. Analyze purchases per user
user_purchases = user_product_matrix.astype(bool).sum(axis=1)
print("\nNumber of purchases per user:")
print(user_purchases.describe())

# Optional: Least active users
print("\nUsers with the least purchases:")
print(user_purchases[user_purchases == 0])

# 3. Calculate sparsity
total_elements = user_product_matrix.size
non_zero_elements = user_product_matrix.astype(bool).sum().sum()
sparsity = 1 - (non_zero_elements / total_elements)
print(f"\nMatrix sparsity: {sparsity:.2%}")

# Optional: Filter matrix
filtered_matrix = user_product_matrix.loc[user_purchases > 0, product_purchases > 0]
print(f"\nFiltered matrix size: {filtered_matrix.shape}")