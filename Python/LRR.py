import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("User Preference Prediction using Regression")

# Load data
data = pd.read_csv("ratings.csv")

st.write("Dataset:", data)

# Features and target
X = data[['user', 'item']]
y = data['rating']

# Train model
model = LinearRegression()
model.fit(X, y)

# User input
user_id = st.number_input("Enter User ID", 1, 10)
item_id = st.number_input("Enter Item ID", 1, 10)

# Prediction
if st.button("Predict Rating"):
    pred = model.predict([[user_id, item_id]])
    st.write("Predicted Rating:", round(pred[0], 2))