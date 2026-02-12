# app.py

import streamlit as st
import joblib
import numpy as np

# โหลดโมเดล
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction App")
st.write("กรอกข้อมูลบ้านเพื่อทำนายราคา")

# -----------------------
# รับ input จาก user
# -----------------------

area = st.number_input("Area (sq.m.)", min_value=20, max_value=500, value=100)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
age = st.number_input("House Age (years)", min_value=0, max_value=100, value=5)

# -----------------------
# ปุ่มทำนาย
# -----------------------

if st.button("Predict Price"):

    features = np.array([[area, bedrooms, bathrooms, age]])
    prediction = model.predict(features)

    st.success(f"Predicted Price: {prediction[0]:,.2f} บาท")