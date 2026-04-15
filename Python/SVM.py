import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

st.title("SVM Classifier with Decision Boundary")


data = pd.read_csv("svm.csv")
data = pd.get_dummies(data)

st.write("Dataset Preview:", data.head())


x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values


model = svm.SVC(kernel='linear')
model.fit(x, y)

st.write("Model trained successfully!")


fig, ax = plt.subplots()
ax.scatter(x[:, 0], x[:, 1], c=y, cmap='coolwarm')

xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 50)
yy = np.linspace(ylim[0], ylim[1], 50)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = model.decision_function(xy).reshape(XX.shape)

ax.contour(XX, YY, Z, levels=[0], colors='k')
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_title("SVM Decision Boundary")

st.pyplot(fig)