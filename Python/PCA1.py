import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

st.title("PCA with Matrix Steps")


data = pd.read_csv("PCA.csv")
data = pd.get_dummies(data)

st.write("Dataset Preview:", data.head())


X = data.iloc[:, :-1]
y = data.iloc[:, -1]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

st.subheader("Step 1: Standardized Data")
st.write(X_scaled)


mean = np.mean(X_scaled, axis=0)
st.subheader("Step 2: Mean")
st.write(mean)


cov_matrix = np.cov(X_scaled, rowvar=False)
st.subheader("Step 3: Covariance Matrix")
st.write(cov_matrix)


eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

st.subheader("Step 4: Eigenvalues")
st.write(eigenvalues)

st.subheader("Step 5: Eigenvectors")
st.write(eigenvectors)


idx = np.argsort(eigenvalues)[::-1]
eigenvectors = eigenvectors[:, idx]
top_vectors = eigenvectors[:, :2]


X_pca = np.dot(X_scaled, top_vectors)

st.subheader("Step 6: PCA Transformed Data")
st.write(X_pca)


fig, ax = plt.subplots()
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("PCA Visualization")

st.pyplot(fig)