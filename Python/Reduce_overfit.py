import streamlit as st
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

st.title("Overfitting vs Reduced Overfitting (Decision Tree)")

data = load_iris()
X, y = data.data, data.target


np.random.seed(42)
X = X + np.random.normal(0, 1.5, X.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.7, random_state=42
)


model1 = DecisionTreeClassifier(max_depth=None)
model1.fit(X_train, y_train)


model2 = DecisionTreeClassifier(max_depth=3)
model2.fit(X_train, y_train)

# Predictions
y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)

st.subheader("Overfitting Model (No Depth Limit)")
st.write("Train Accuracy:", model1.score(X_train, y_train))
st.write("Test Accuracy:", model1.score(X_test, y_test))

st.subheader("Reduced Overfitting Model (max_depth=3)")
st.write("Train Accuracy:", model2.score(X_train, y_train))
st.write("Test Accuracy:", model2.score(X_test, y_test))