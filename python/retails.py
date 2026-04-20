import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

# Fill missing price
df['Price'] = df.groupby('Product')['Price'].transform(lambda x: x.fillna(x.mean()))

# Total Sales
df['Total_Sales'] = df['Quantity'] * df['Price']

# Group data
sales = df.groupby('Product')['Total_Sales'].sum()

# Highest sales
top_product = sales.idxmax()
print("Top Product:", top_product)

# -------- SIMPLE GRAPH --------
plt.bar(sales.index, sales.values)

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.show()
