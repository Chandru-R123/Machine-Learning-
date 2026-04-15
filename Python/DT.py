import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

st.title("Decision Tree Classifier")


data = pd.read_csv("DT.csv")
data = pd.get_dummies(data)

st.write("Dataset Preview:", data.head())

x = data.iloc[:, :-1]
y = data.iloc[:, -1]


model = DecisionTreeClassifier()
model.fit(x, y)

st.write("Accuracy on training data:", model.score(x, y))

st.write("Prediction for row 3:", model.predict(x.iloc[[3]])[0])


st.subheader("Decision Tree Visualization")
plt.figure(figsize=(8,6))
tree.plot_tree(model, feature_names=x.columns, class_names=['No','Yes'], filled=True)
st.pyplot(plt)
