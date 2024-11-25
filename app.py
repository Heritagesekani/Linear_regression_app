import streamlit as st
import requests
import joblib
import numpy as np

# app title and description
st. title("power output prediction")
st.write("enter the values for the following features to predict power output (PE).")

#user input for each feature
ambient_temperature = st.number_input("Ambient Temperature(AT)", value=15.0")
exhaust_vacuum = st.number_input("Exhaust Vacuum (V)", value=40.0)
ambient_pressure = st.number_input("Ambient Pressure(AP)", value=1000.0)
relative_humidity = st.number_input ("Relative_Humidity (RH)", value=75.0)

if st.button("predict"):
    #prepare data
    input_data = {
        "ambient_temperature":ambient_temperature ,
        "exhaust_vacuum":exhaust_vacuum,
        "ambient_pressure":ambient_pressure,
        "relative_humidity":relative_humidity
    }


    # make api call
    response =request.post("http://0.0.0.0:000/predict", json=input_data)
if response.status_code=200:
    prediction = response.json()["prediction"]
    st.write(f"predict power output(PE):{prediction}")
else:
    st.write("Error in prediction. please try again.")

