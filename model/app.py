import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Marketing Campaign Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Marketing Campaign Prediction")
st.write("Enter the customer details below to get the prediction.")

st.header("Customer Details")

age = st.number_input("Age", min_value=18, max_value=100)

income = st.number_input("Annual Income")

spending = st.number_input("Spending Score")

gender = st.selectbox("Gender", ["Male", "Female"])

married = st.selectbox("Married", ["Yes", "No"])

st.header("Categorical Input Fields")

education = st.selectbox(
    "Education",
    ["Basic", "Graduation", "Master", "PhD"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Together", "Divorced", "Widow"]
)

complain = st.selectbox(
    "Complain",
    [0, 1]
)

response = st.selectbox(
    "Previous Response",
    [0, 1]
)

st.markdown("---")

if st.button("Predict Marketing Campaign"):
    st.success("Prediction Completed Successfully")

    st.subheader("Prediction Result")

prediction = "Yes"   # Abhi placeholder hai

if prediction == "Yes":
    st.success("✅ Customer is likely to respond to the marketing campaign.")
else:
    st.error("❌ Customer is not likely to respond to the marketing campaign.")