import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.title("User Clustering")

# Load data
data = pd.read_csv("ratings.csv")

# Convert to user-item matrix
matrix = data.pivot(index='user', columns='item', values='rating').fillna(0)

st.write("User-Item Matrix:", matrix)

# Apply clustering
model = KMeans(n_clusters=2)
labels = model.fit_predict(matrix)

# Add cluster labels
matrix['Cluster'] = labels

st.write("Clustered Users:", matrix)

# Plot
fig, ax = plt.subplots()
ax.scatter(matrix[1], matrix[2], c=labels)
ax.set_xlabel("Item 1 Rating")
ax.set_ylabel("Item 2 Rating")
st.pyplot(fig)