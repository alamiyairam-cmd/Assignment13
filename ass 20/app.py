import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "LR_ford_car.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
encoded_columns = joblib.load(os.path.join(BASE_DIR, "columns.pkl"))

st.set_page_config(
    page_title="Ford Car Price Predictor",
    layout="centered"
)
st.title("Ford Car Price Predictor")
st.write("Enter the car details below to predict its selling price.")

year = st.number_input(
    "Manufacturing Year",
    min_value=2000,
    max_value=2026,
    value=2018
)

mileage = st.number_input(
    "Mileage",
    min_value=0,
    max_value=50000,
    value=5000
)

tax = st.number_input(
    "Road Tax (tax)",
    min_value=0,
    max_value=200,
    value=100
)

mpg = st.number_input(
    "MPG",
    min_value=10,
    max_value=100,
    value=55
)

engine = st.number_input(
    "Engine Size",
    min_value=1,
    max_value=7,
    value=2
)
# Dropdowns for categorical inputs
transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual", "Semi-Auto"]
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Other"]
)

car_model = st.text_input("Enter Car Model Name...")

if st.button("Predict Price", key="predict_btn"):

    input_data = pd.DataFrame({
        "model": [car_model],
        "year": [year],
        "transmission": [transmission],
        "mileage": [mileage],
        "fuelType": [fuel_type],
        "tax": [tax],
        "mpg": [mpg],
        "engineSize": [engine]
    })

    # One-Hot Encoding
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(
        columns=encoded_columns,
        fill_value=0
    )

    # Scale numerical columns
    numerical_columns = ["year", "mileage", "tax", "mpg", "engineSize"]

    input_data[numerical_columns] = scaler.transform(
        input_data[numerical_columns]
    )

    # Prediction
    prediction = model.predict(input_data)

    st.success(f"Predicted Price: £{prediction[0]:,.2f}")
    import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("ford_car_dataset.csv")

df = pd.get_dummies(df)

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)

print("R2 score:", r2)