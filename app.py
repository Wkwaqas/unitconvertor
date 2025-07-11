import time
import numpy as np
import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="WK Unit Converter", layout='wide')
st.title('Unit Converter 🔄')
st.write("Quickly convert your measurements with fun animations and clear results!")

def animate_result(text):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.code(displayed_text)
        time.sleep(0.02)
    return displayed_text

conversion_category = st.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])

if conversion_category == "Length":
    st.subheader("Length Conversion")
    value = st.number_input("Enter the length value", value=0.0, format="%.4f")
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles", "Feet"], key="length_from")
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles", "Feet"], key="length_to")
    
    if st.button("Convert Length"):
        conversion_factors = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048}
        value_in_meters = value * conversion_factors[from_unit]
        converted_value = value_in_meters / conversion_factors[to_unit]
        result_text = f"{value} {from_unit} equals {converted_value:.4f} {to_unit}"
        animate_result(result_text)

elif conversion_category == "Weight":
    st.subheader("Weight Conversion")
    value = st.number_input("Enter the weight value", value=0.0, format="%.4f", key="weight_value")
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"], key="weight_from")
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"], key="weight_to")
    
    if st.button("Convert Weight"):
        conversion_factors = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
        value_in_kg = value * conversion_factors[from_unit]
        converted_value = value_in_kg / conversion_factors[to_unit]
        result_text = f"{value} {from_unit} equals {converted_value:.4f} {to_unit}"
        animate_result(result_text)

elif conversion_category == "Temperature":
    st.subheader("Temperature Conversion")
    value = st.number_input("Enter the temperature value", value=0.0, format="%.2f", key="temp_value")
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_from")
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_to")
    
    if st.button("Convert Temperature"):
        def c_to_f(c): 
            return c * 9/5 + 32
        def c_to_k(c): 
            return c + 273.15
        def f_to_c(f): 
            return (f - 32) * 5/9
        def k_to_c(k): 
            return k - 273.15

        if from_unit == "Celsius":
            temp_c = value
        elif from_unit == "Fahrenheit":
            temp_c = f_to_c(value)
        elif from_unit == "Kelvin":
            temp_c = k_to_c(value)

        if to_unit == "Celsius":
            converted_temp = temp_c
        elif to_unit == "Fahrenheit":
            converted_temp = c_to_f(temp_c)
        elif to_unit == "Kelvin":
            converted_temp = c_to_k(temp_c)
            
        result_text = f"{value} {from_unit} equals {converted_temp:.2f} {to_unit}"
        animate_result(result_text)
print