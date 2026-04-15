import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage

st.title("Hierarchical Clustering - Agglomerative")

# Sample dataset
data = pd.DataFrame({
    'X': [1, 2, 3, 8, 9, 10],
    'Y': [2, 3, 4, 7, 8, 9]
})

st.write("Dataset:", data)

# Apply Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=2)
labels = model.fit_predict(data)

# Plot clusters
fig1, ax1 = plt.subplots()
ax1.scatter(data['X'], data['Y'], c=labels)
ax1.set_title("Cluster Result")
st.pyplot(fig1)

# Silhouette Score
score = silhouette_score(data, labels)
st.write("Silhouette Score:", score)

# Dendrogram
st.subheader("Dendrogram")

linked = linkage(data, method='ward')

fig2, ax2 = plt.subplots()
dendrogram(linked)
ax2.set_title("Dendrogram")
st.pyplot(fig2)