import streamlit as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.title("K-Means Clustering - Visualization")


X = [
    [1, 2], [2, 3], [3, 4],
    [8, 7], [9, 8], [10, 9]
]


k = st.slider("Select number of clusters", 1, 5, 2)


model = KMeans(n_clusters=k)
model.fit(X)

labels = model.labels_
centers = model.cluster_centers_


fig, ax = plt.subplots()

for i in range(len(X)):
    if labels[i] == 0:
        ax.scatter(X[i][0], X[i][1], marker='o')
    elif labels[i] == 1:
        ax.scatter(X[i][0], X[i][1], marker='s')
    else:
        ax.scatter(X[i][0], X[i][1], marker='^')


ax.scatter(centers[:, 0], centers[:, 1], marker='X')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Cluster Groupings")

st.pyplot(fig)
