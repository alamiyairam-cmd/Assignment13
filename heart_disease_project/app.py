import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load("heart_model.pkl")
columns = joblib.load("columns.pkl")

st.title("Heart Disease Prediction")

age = st.number_input("Age", min_value=1, max_value=120)
bp = st.number_input("Resting BP")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
hr = st.number_input("Max Heart Rate")
oldpeak = st.number_input("Oldpeak")

if st.button("Predict"):

    sample = {
        "Age": age,
        "RestingBP": bp,
        "Cholesterol": chol,
        "FastingBS": fbs,
        "MaxHR": hr,
        "Oldpeak": oldpeak
    }

    sample_df = pd.DataFrame([sample])

    sample_df = pd.get_dummies(sample_df)

    sample_df = sample_df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(sample_df)

    if prediction[0] == 1:
        st.success("❤️ Heart Disease: YES")
    else:
        st.success("💚 Heart Disease: NO")