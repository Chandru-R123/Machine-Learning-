import streamlit as st
import numpy as np
from hmmlearn import hmm

st.title("Simple HMM Example")
x = np.array([[1],[0],[1],[0],[1]])

st.write("observation:",x.flatten())

model = hmm.CategoricalHMM(n_components = 2, n_iter = 100)
model.fit(x)

states = model.predict(x)
st.write("Hiden states: ", states)

st.subheader("Enter Obersevation")
val = st.number_input("value", min_value=0, max_value=1, step=1)
if st.button("Predict"):
    result = model.predict(np.array([[val]]))
    st.write("Predicted State:",result[0])
