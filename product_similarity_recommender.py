from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load the user-product matrix
user_product_matrix = pd.read_csv('user_product_matrix.csv', index_col=0)

# Calculate the cosine similarity between products
product_similarity = cosine_similarity(user_product_matrix.T)  # Transpose to compare products
product_similarity_df = pd.DataFrame(product_similarity, index=user_product_matrix.columns, columns=user_product_matrix.columns)

# Print the first few rows of the similarity matrix
print(product_similarity_df.head())

# Recommend top N similar products for a given product
def recommend_similar_products(product_id, similarity_matrix, top_n=5):
    similar_products = similarity_matrix[product_id].sort_values(ascending=False)[1:top_n+1]
    return similar_products

# Example recommendation for a specific product
product_id = '003d1f09-c'  # Replace with a valid Product_ID from your data
recommendations = recommend_similar_products(product_id, product_similarity_df)
print(f"Top recommendations for product {product_id}:\n", recommendations)