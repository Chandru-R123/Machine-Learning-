import streamlit as st
import numpy as np
from hmmlearn import hmm

st.title("Simple HMM (Baum-Welch)")

# Step 1: Observations
# 0 = Low, 1 = High
data = np.array([[0], [1], [0], [1], [0]])

st.write("Observations:", data.flatten())

# Step 2: Create model (2 hidden states)
model = hmm.CategoricalHMM(n_components=2, n_iter=100)

# Step 3: Train model (Baum-Welch runs here)
model.fit(data)

# Step 4: Show learned values
st.write("Start Probabilities:", model.startprob_)
st.write("Transition Matrix:", model.transmat_)
st.write("Emission Matrix:", model.emissionprob_)

# Step 5: Predict hidden states
states = model.predict(data)
st.write("Hidden States:", states)