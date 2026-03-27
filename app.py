import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Carbon Predictor", layout="wide")

st.title("🌍 Carbon Emission Predictor")

model = joblib.load("model.pkl")

st.sidebar.header("Input Features")
inputs = {}
for i in range(5):
    inputs[f'feature_{i}'] = st.sidebar.number_input(f'Feature {i}', 0.0)

input_df = pd.DataFrame([inputs])

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Carbon Emission: {prediction}")
    inputs = {}

inputs['distance_km'] = st.sidebar.number_input("Distance (km)", 0.0)
inputs['digital_co2_pct'] = st.sidebar.number_input("Digital CO2 %", 0.0)
inputs['green_it_enabled'] = st.sidebar.selectbox("Green IT Enabled", [0,1])
inputs['lab_co2_kg'] = st.sidebar.number_input("Lab CO2 (kg)", 0.0)
inputs['lab_co2_pct'] = st.sidebar.number_input("Lab CO2 %", 0.0)

input_df = pd.DataFrame([inputs])

# VERY IMPORTANT
input_df = input_df[X.columns]
