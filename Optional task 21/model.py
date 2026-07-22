import streamlit as st
import pandas as pd
import joblib

# ==========================
# Load Model, Scaler & Columns

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="centered"
)

# ==========================
# Title
# ==========================
st.title("💻 Laptop Price Prediction")
st.write("Enter the laptop details to predict the price.")

# ==========================
# User Inputs
# ==========================
ram = st.number_input(
    "RAM (GB)",
    min_value=2,
    max_value=64,
    value=8
)

weight = st.number_input(
    "Weight (kg)",
    min_value=0.5,
    max_value=5.0,
    value=1.5
)

inches = st.number_input(
    "Screen Size (Inches)",
    min_value=10.0,
    max_value=20.0,
    value=15.6
)

company = st.selectbox(
    "Company",
    ["Dell", "HP", "Lenovo", "Asus", "Acer", "Apple"]
)

cpu = st.selectbox(
    "CPU",
    ["Intel i3", "Intel i5", "Intel i7", "AMD Ryzen 5", "AMD Ryzen 7"]
)

os = st.selectbox(
    "Operating System",
    ["Windows", "Mac", "Linux"]
)

# ==========================
# Prediction
# ==========================
if st.button("Predict Price"):

    # Create DataFrame
    input_data = pd.DataFrame({
        "ram": [ram],
        "weight": [weight],
        "inches": [inches],
        "company": [company],
        "cpu": [cpu],
        "os": [os]
    })

    # One-Hot Encoding
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(
        columns= encoded_columns,
        fill_value=0
    )

    # Scale numerical columns
    numerical_columns = ["ram", "weight", "inches"]

    input_data[numerical_columns] = scaler.transform(
        input_data[numerical_columns]
    )

    # Prediction
    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Laptop Price: ₹{prediction[0]:,.2f}")