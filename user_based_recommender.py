import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Load dataset
file_path = 'C:/Users/Matias/ecommerce_dataset_updated.csv'
data = pd.read_csv(file_path)

# Prepare product features
product_features = data[['Category', 'Price (Rs.)', 'Discount (%)']]
product_features = pd.get_dummies(product_features, columns=['Category'])
scaler = StandardScaler()
product_features[['Price (Rs.)', 'Discount (%)']] = scaler.fit_transform(product_features[['Price (Rs.)', 'Discount (%)']])

# Calculate product similarity
product_similarity = cosine_similarity(product_features)
product_similarity_df = pd.DataFrame(product_similarity, index=data['Product_ID'], columns=data['Product_ID'])

# Function to get user-specific recommendations
def recommend_for_user(user_id, user_product_data, similarity_matrix, top_n=5):
    # Get products purchased by the user
    user_purchases = user_product_data[user_product_data['User_ID'] == user_id]
    purchased_products = user_purchases['Product_ID'].unique()

    # Aggregate similarity scores for products the user has not purchased
    similarity_scores = similarity_matrix[purchased_products].mean(axis=1)
    similarity_scores = similarity_scores.drop(index=purchased_products, errors='ignore')  # Remove already purchased products

    # Get top N recommendations
    top_recommendations = similarity_scores.sort_values(ascending=False).head(top_n)
    return top_recommendations

# Example user and dataset for purchases
user_product_data = data[['User_ID', 'Product_ID']]
user_id = '337c166f'  # Replace with a valid User_ID

# Get recommendations for the user
user_recommendations = recommend_for_user(user_id, user_product_data, product_similarity_df)
print(f"Top recommendations for user {user_id}:\n", user_recommendations)

# Retrieve details of recommended products
recommended_products = data.loc[data['Product_ID'].isin(user_recommendations.index)]
print("\nDetails of recommended products for the user:")
print(recommended_products[['Product_ID', 'Category', 'Price (Rs.)', 'Discount (%)']])

# Visualize recommended products
def visualize_recommendations(recommendations, recommended_products, user_id):
    # Plot similarity scores
    recommendations.sort_values().plot(kind='barh', figsize=(8, 5))
    plt.title(f"Similarity Scores for Recommended Products (User {user_id})")
    plt.xlabel("Similarity Score")
    plt.ylabel("Product ID")
    plt.show()

    # Plot product details (price and discount comparison)
    plt.figure(figsize=(8, 5))
    plt.bar(recommended_products['Product_ID'], recommended_products['Price (Rs.)'], label='Price', alpha=0.7)
    plt.bar(recommended_products['Product_ID'], recommended_products['Discount (%)'], label='Discount', alpha=0.7)
    plt.title(f"Price and Discount for Recommended Products (User {user_id})")
    plt.xlabel("Product ID")
    plt.ylabel("Value")
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Call the visualization function
visualize_recommendations(user_recommendations, recommended_products, user_id)

# Simplify the saved file by selecting only relevant columns
recommended_products[['Product_ID', 'Category', 'Price (Rs.)', 'Discount (%)', 'Final_Price(Rs.)']].to_csv('user_recommendations.csv', index=False)
print("Simplified recommendations saved to user_recommendations.csv")