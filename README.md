# 🚗 Car Price Prediction App

A Machine Learning web application built using **Streamlit** that predicts the estimated price of a car based on its specifications.
The model is trained using **Lasso Regression** and deployed as an interactive web interface.
 
---

## 📌 Project Overview

This project uses Machine Learning to estimate the price of a car using various features such as:
 
* Symboling
* Wheelbase
* Car Length
* Car Width
* Curb Weight
* Engine Size
* Horsepower
* City MPG
* Car Body Type
* Drive Wheel
* Engine Location
* Engine Type
* Number of Cylinders

The predicted price is displayed in:

* 💵 US Dollars (USD)
* 🇮🇳 Indian Rupees (INR)

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* Scikit-learn
* Joblib
* Machine Learning (Lasso Regression)

---

## 📂 Project Structure

```
car_price_prediction/
│
├── app2.py              # Streamlit application
├── lasso_model.pkl      # Trained ML model
├── scaler.pkl           # Scaler used during training
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation

Follow these steps to run the project locally:

### Step 1: Clone the repository

```
git clone https://github.com/your-username/car_price_prediction.git
```

### Step 2: Navigate to the project folder

```
cd car_price_prediction
```

### Step 3: Install dependencies

```
pip install -r requirements.txt
```

### Step 4: Run the Streamlit app

```
streamlit run app2.py
```

---

## 📦 Requirements

The project requires the following libraries:

```
streamlit
numpy
pandas
scikit-learn
joblib
```

---

## 🎯 Features

* User-friendly web interface
* Real-time car price prediction
* Automatic currency conversion (USD → INR)
* Clean and responsive UI
* Machine Learning model integration
* Deployment-ready project

---

## 🚀 How It Works

1. User enters car specifications
2. Data is processed and scaled
3. Model predicts the car price
4. Result is displayed instantly

---

## 📊 Model Information

Model Used:

**Lasso Regression**

Why Lasso?

* Reduces overfitting
* Performs feature selection
* Improves model performance

---

## 🌐 Deployment

This project can be deployed using:

* Streamlit Cloud
* Render
* Hugging Face Spaces

---

## 👨‍💻 Author

**Atish Kushwaha**

Machine Learning & Data Science Enthusiast

---

## ⭐ If you like this project

Please give this repository a **star** on GitHub!



## 🌐 Live Demo

Click the link below to use the application:

🔗 https://carpriceprediction-js9jk2lve2by7v4gpb84ua.streamlit.app/


## 📸 Screenshots
### Home Page

![App Screenshot](screenshot.png)<img width="1903" height="916" alt="Screenshot 2026-03-28 000938" src="https://github.com/user-attachments/assets/177d12ac-7792-4282-8943-1129cce16470" />
