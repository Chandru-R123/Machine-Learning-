import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.title("Heart Disease Prediction - Random Forest")

# Load dataset
data = pd.read_csv("heart.csv")

st.write("Dataset Preview:", data.head())

# Features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
st.write("Accuracy:", accuracy_score(y_test, y_pred))

# 🔽 USER INPUT SECTION
st.subheader("Enter Patient Details")

age = st.number_input("Age", 20, 100)
sex = st.selectbox("Sex (1=Male, 0=Female)", [1, 0])
cp = st.selectbox("Chest Pain Type (0-3)", [0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200)
chol = st.number_input("Cholesterol", 100, 400)
fbs = st.selectbox("Fasting Blood Sugar >120 (1=True, 0=False)", [1,0])
restecg = st.selectbox("Rest ECG (0-2)", [0,1,2])
thalach = st.number_input("Max Heart Rate", 60, 220)
exang = st.selectbox("Exercise Angina (1=Yes, 0=No)", [1,0])
oldpeak = st.number_input("Oldpeak (0.0 - 6.0)", 0.0, 6.0)
slope = st.selectbox("Slope (0-2)", [0,1,2])
ca = st.selectbox("Number of vessels (0-3)", [0,1,2,3])
thal = st.selectbox("Thal (1-3)", [1,2,3])

# Predict button
if st.button("Predict"):
    input_data = [[age, sex, cp, trestbps, chol, fbs, restecg,
                   thalach, exang, oldpeak, slope, ca, thal]]
    
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("⚠️ High Chance of Heart Disease")
    else:
        st.success("✅ Low Chance of Heart Disease")