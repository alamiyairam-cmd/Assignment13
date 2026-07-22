import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Load Files
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "LR_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "columns.pkl")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    columns = joblib.load(COLUMNS_PATH)
except FileNotFoundError as e:
    st.error(f"File not found:\n{e}")
    st.stop()
except EOFError:
    st.error("One of the .pkl files is empty or corrupted. Please recreate the model files.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -----------------------------
# Streamlit Page
# -----------------------------
st.set_page_config(
    page_title="Laptop Price Prediction",
    layout="centered"
)

st.title("💻 Laptop Price Prediction")
st.write("Enter laptop specifications below.")

# -----------------------------
# Inputs
# -----------------------------
ram = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8)

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
    ["Intel i3", "Intel i5", "Intel i7", "Ryzen 5", "Ryzen 7"]
)

opsys = st.selectbox(
    "Operating System",
    ["Windows", "Mac", "Linux"]
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "Company": [company],
        "Ram": [ram],
        "Weight": [weight],
        "Inches": [inches],
        "Cpu": [cpu],
        "OpSys": [opsys]
    })

    # One-hot encoding
    input_df = pd.get_dummies(input_df)

    # Match training columns
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # Scale
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)

    st.success(f"💰 Predicted Laptop Price: ₹ {prediction[0]:,.2f}")