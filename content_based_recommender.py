import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# 1. Load the original dataset
file_path = 'C:/Users/Matias/ecommerce_dataset_updated.csv'
data = pd.read_csv(file_path)

# 2. Prepare product features
# Select relevant features
product_features = data[['Category', 'Price (Rs.)', 'Discount (%)']]

# One-hot encode categorical column
product_features = pd.get_dummies(product_features, columns=['Category'])

# Standardize numerical features
scaler = StandardScaler()
product_features[['Price (Rs.)', 'Discount (%)']] = scaler.fit_transform(product_features[['Price (Rs.)', 'Discount (%)']])

# 3. Calculate product similarity
product_similarity = cosine_similarity(product_features)
product_similarity_df = pd.DataFrame(product_similarity, index=data['Product_ID'], columns=data['Product_ID'])

# Print a sample of the similarity matrix
print("Product similarity matrix:\n", product_similarity_df.head())

# 4. Recommend similar products
def recommend_products(product_id, similarity_matrix, top_n=5):
    similar_products = similarity_matrix[product_id].sort_values(ascending=False)[1:top_n+1]
    return similar_products

# Example recommendation
product_id = '003d1f09-c'  # Replace with a valid Product_ID from your dataset
recommendations = recommend_products(product_id, product_similarity_df)
print(f"Top recommendations for product {product_id}:\n", recommendations)

# 5. Retrieve details of recommended products
recommended_products = data.loc[data['Product_ID'].isin(recommendations.index)]
print("\nDetails of recommended products:")
print(recommended_products[['Product_ID', 'Category', 'Price (Rs.)', 'Discount (%)']])

# 6. Visualize recommendations
def visualize_recommendations(recommendations, product_id):
    recommendations.sort_values().plot(kind='barh', figsize=(8, 5))
    plt.title(f"Top Recommendations for Product {product_id}")
    plt.xlabel("Similarity Score")
    plt.ylabel("Product ID")
    plt.show()

# Call the visualization function
visualize_recommendations(recommendations, product_id)