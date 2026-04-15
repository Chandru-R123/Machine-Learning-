import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.title("PCA Visualization")


data = pd.read_csv("PCA.csv")
data = pd.get_dummies(data)

st.write("Dataset Preview:", data.head())

X = data.iloc[:, :-1]
y = data.iloc[:, -1]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

st.write(f"Explained variance ratio: {pca.explained_variance_ratio_}")


fig, ax = plt.subplots()
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_title("PCA Visualization")
st.pyplot(fig)