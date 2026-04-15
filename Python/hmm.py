import streamlit as st
import numpy as np
from hmmlearn import hmm

st.title("Simple HMM Example")


data = np.array([[0], [1], [0], [1], [0]])

st.write("Observations:", data.flatten())


model = hmm.CategoricalHMM(n_components=2, n_iter=100)
model.fit(data)


states = model.predict(data)
st.write("Hidden States:", states)

st.subheader("Enter observation (0 or 1)")
val = st.number_input("Value", min_value=0, max_value=1, step=1)


if st.button("Predict"):
    result = model.predict(np.array([[val]]))
    st.write("Predicted State:", result[0])