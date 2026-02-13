# 🏠 House Price Prediction Web App

## 📌 Project Overview
This project is a Machine Learning web application that predicts house prices based on user input features such as area, number of bedrooms, bathrooms, and parking spaces.

The model is built using Linear Regression and deployed using Streamlit.

---

## 🎯 Objective
To build an end-to-end Machine Learning system including:
- Data preprocessing
- Model training
- Model evaluation
- Model saving
- Web application deployment

---

## 📊 Dataset Description

The dataset contains housing information used to predict house prices.

### 🔹 Target Variable
- `price` → House price (dependent variable)

### 🔹 Features
- `area` → House area (square meters)
- `bedrooms` → Number of bedrooms
- `bathrooms` → Number of bathrooms
- `age` → Number of House age

### 🔹 Dataset Size
- Samples: (ใส่จำนวน rows ของ dataset ที่คุณใช้)
- Features: 4 input features

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Splitting
- 80% Training set
- 20% Testing set

### 2️⃣ Model Used
- Linear Regression (Scikit-learn)

### 3️⃣ Model Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

### 4️⃣ Model Saving
The trained model is saved as:


---

## 🌐 Web Application

The web application is built using Streamlit.

### User Inputs:
- Area
- Bedrooms
- Bathrooms
- age

### Output:
- Predicted House Price

Run the app with: