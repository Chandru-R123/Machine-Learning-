import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ratings.csv")

# Remove missing values
df = df.dropna()

# Calculate average rating
average_rating = df['Customer_Rating'].mean()
print("Average Rating:", average_rating)

# Top 3 products
top3 = df.sort_values(by='Customer_Rating', ascending=False).head(3)
print("Top 3 Products:\n", top3)

# Top 5 visualization
top5 = df.sort_values(by='Customer_Rating', ascending=False).head(5)

plt.bar(top5['Product_Name'], top5['Customer_Rating'])
plt.title("Top 5 Product Ratings")
plt.xlabel("Product")
plt.ylabel("Rating")
plt.show()