# UNSUPERVISED LEARNING - CLUSTERING + PCA (LARGE DATA + UI)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.decomposition import PCA

st.title("🌾 Farm Clustering (Large Dataset)")

# -------------------------
# GENERATE LARGE DATASET
# -------------------------
np.random.seed(42)

n = 1000

data = pd.DataFrame({
    'soil_quality': np.random.randint(5, 10, n),
    'rainfall': np.random.randint(60, 150, n),
    'temperature': np.random.randint(25, 40, n),
    'fertilizer': np.random.randint(20, 80, n)
})

st.write("Dataset Size:", data.shape)
st.dataframe(data.head())

# -------------------------
# HIERARCHICAL CLUSTERING
# -------------------------
st.subheader("Hierarchical Clustering Dendrogram")

Z = linkage(data, method='ward')

fig, ax = plt.subplots()
dendrogram(Z, ax=ax)
ax.set_title("Dendrogram")
ax.set_xlabel("Farms")
ax.set_ylabel("Distance")

st.pyplot(fig)

# -------------------------
# PCA
# -------------------------
st.subheader("PCA Visualization")

pca = PCA(n_components=2)
reduced = pca.fit_transform(data)

fig2, ax2 = plt.subplots()
ax2.scatter(reduced[:, 0], reduced[:, 1])
ax2.set_title("PCA Clusters")
ax2.set_xlabel("PC1")
ax2.set_ylabel("PC2")

st.pyplot(fig2)
