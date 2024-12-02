# Personalized Product Recommendation System #

## Overview
This project implements a Content-Based Filtering approach to build a personalized product recommendation system for e-commerce platforms. Using user purchase history and product features, the system recommends similar products to users, visualizes the results, and generates a structured CSV report of recommendations.

## Data Limitations

The dataset used in this project contains anonymized product data, where products are identified by unique codes (e.g., `003d1f09-c`). These codes are not descriptive product names, which may make the visualizations less intuitive for a general audience.

## Features
* Displays user-specific recommendations based on purchase history.
* Recommends similar products using cosine similarity on product features.
* Visualizes similarity scores and product feature comparisons (e.g., price and discounts).
* Outputs a simplified, easy-to-analyze CSV file with recommendations.

## Dataset
The dataset contains e-commerce transaction data with the following columns:

* User_ID: Unique identifier for each user.
* Product_ID: Unique identifier for each product.
* Category: The category to which the product belongs (e.g., Sports, Toys).
* Price (Rs.): Original price of the product.
* Discount (%): Discount offered on the product.
* Final_Price (Rs.): Price after applying the discount.
* Payment_Method: The payment method used (e.g., UPI, Credit Card).
* Purchase_Date: The date when the product was purchased.

## Visualizations
The project provides visual insights through the following graphs:

Similarity Scores for Recommended Products (User 337c166f):

* This horizontal bar chart illustrates the similarity scores for the top recommended products for a specific user. Higher scores indicate stronger similarity to the user’s previously purchased products.

Top Recommendations for Product 003d1f09-c:

* This chart shows the similarity scores of the top recommendations for a specific product. It provides insights into how similar each recommended product is to the reference product.

Price and Discount for Recommended Products (User 337c166f):

* This grouped bar chart compares the prices and discounts of the recommended products, helping users see the relative value offered by each recommendation.

## Outputs
The system generates a CSV file user_recommendations.csv containing the following columns:

* Product_ID: Recommended product IDs.
* Category: Category of each product.
* Price (Rs.): Original price of each product.
* Discount (%): Discount offered on each product.
* Final_Price (Rs.): Final price after applying the discount.

Example output: ```csv Product_ID,Category,Price (Rs.),Discount (%),Final_Price(Rs.) 8d276b60-e,Sports,41.61,15,35.37 5e4309df-9,Sports,27.03,15,22.98 3ad00ebe-5,Sports,25.95,15,22.06 c355955a-7,Sports,61.67,15,52.42 9e1cec60-9,Sports,50.88,15,43.25 ```

## How to Run
1. Clone this repository to your local machine.
2. Ensure Python is installed with the following libraries:
* pandas
* scikit-learn
* matplotlib
3. Place the dataset file (ecommerce_dataset_updated.csv) in the same directory.
4. Run the main script: ```bash python user_based_recommender.py ```
5. View the output CSV file user_recommendations.csv and the generated visualizations.

## Future Improvements
* Add hybrid recommendation techniques combining collaborative and content-based filtering.
* Include additional user behavior data, such as product ratings.
* Optimize the visualization for larger datasets.

## License
This project is licensed under the MIT License. The dataset is sourced from Kaggle: (https://www.kaggle.com/datasets/steve1215rogg/e-commerce-dataset) and is licensed under CC BY-NC-SA 4.0. Please ensure compliance with Kaggle's dataset terms and conditions.
