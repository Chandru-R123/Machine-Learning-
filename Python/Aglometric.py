import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

st.title("Heart Data - Agglomerative Clustering")

# Load dataset
data = pd.read_csv("heart.csv")

st.write("Dataset Preview:", data.head())

# Use only 2 features for visualization
X = data[['age', 'chol']]

# Apply clustering
model = AgglomerativeClustering(n_clusters=2)
labels = model.fit_predict(X)

# Plot
fig, ax = plt.subplots()
ax.scatter(X['age'], X['chol'], c=labels)

ax.set_xlabel("Age")
ax.set_ylabel("Cholesterol")
ax.set_title("Agglomerative Clustering")

st.pyplot(fig)