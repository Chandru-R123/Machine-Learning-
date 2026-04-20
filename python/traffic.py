import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("traffic.csv")

# Replace missing values with 0
df['Vehicle_Count'] = df['Vehicle_Count'].fillna(0)

# Calculate total and average
total_vehicles = df['Vehicle_Count'].sum()
average_vehicles = df['Vehicle_Count'].mean()

print("Total Vehicle Count:", total_vehicles)
print("Average Vehicle Count:", average_vehicles)

# Find highest traffic date
highest_date = df.loc[df['Vehicle_Count'].idxmax(), 'Date']
print("Date with highest traffic:", highest_date)

# Plot line graph
plt.plot(df['Date'], df['Vehicle_Count'], marker='o')
plt.title("Daily Traffic Volume Trend")
plt.xlabel("Date")
plt.ylabel("Vehicle Count")
plt.xticks(rotation=45)
plt.show()