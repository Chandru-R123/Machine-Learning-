import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.title("Regression Model (LWR-like)")

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])


model = LinearRegression()
model.fit(X, y)


y_pred = model.predict(X)


rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

st.write("RMSE:", rmse)
st.write("R2 Score:", r2)


fig, ax = plt.subplots()
ax.scatter(X, y)          # original data
ax.plot(X, y_pred)        # regression line

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Regression Line")

st.pyplot(fig)


st.subheader("Predict new value")
val = st.number_input("Enter X value")

if st.button("Predict"):
    pred = model.predict([[val]])
    st.write("Predicted Y:", pred[0])