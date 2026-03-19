# SUPERVISED LEARNING - RANDOM FOREST (LARGE DATA + UI)

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

st.title("🌱 Crop Yield Prediction (Large Dataset)")

# -------------------------
# GENERATE LARGE DATASET
# -------------------------
np.random.seed(42)

n = 2000  # large dataset

data = pd.DataFrame({
    'soil_quality': np.random.randint(5, 10, n),
    'rainfall': np.random.randint(60, 150, n),
    'temperature': np.random.randint(25, 40, n),
    'fertilizer': np.random.randint(20, 80, n),
    'seed_type': np.random.randint(1, 3, n)
})

# Create realistic yield formula
data['yield'] = (
    data['soil_quality'] * 0.5 +
    data['rainfall'] * 0.02 -
    data['temperature'] * 0.03 +
    data['fertilizer'] * 0.01 +
    data['seed_type'] * 0.2 +
    np.random.normal(0, 0.3, n)
)

st.write("Dataset Size:", data.shape)
st.dataframe(data.head())

# -------------------------
# TRAIN MODEL
# -------------------------
X = data.drop('yield', axis=1)
y = data['yield']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=300, max_depth=12)
model.fit(X_train, y_train)

pred = model.predict(X_test)
mse = mean_squared_error(y_test, pred)

st.subheader("Model Accuracy (MSE)")
st.write(mse)

# -------------------------
# USER INPUT
# -------------------------
st.subheader("Enter New Data")

soil = st.number_input("Soil Quality", 1, 10)
rain = st.number_input("Rainfall", 0, 200)
temp = st.number_input("Temperature", 0, 50)
fert = st.number_input("Fertilizer", 0, 100)
seed = st.number_input("Seed Type", 1, 2)

if st.button("Predict Yield"):
    new_data = [[soil, rain, temp, fert, seed]]
    result = model.predict(new_data)
    st.success(f"Predicted Yield: {result[0]:.2f}")
