import streamlit as st
import numpy as np
import joblib
import os

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="🚗 Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS (UI DESIGN)
# =========================
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(120deg, #f6f9fc, #eef2ff);
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        color: #1f2937;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        text-align: center;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 15px;
    }

    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px;
        border-radius: 10px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🚗 Car Price Prediction System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Predict the estimated price of a car using Machine Learning</div>',
    unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚙️ Settings")

USD_TO_INR = st.sidebar.number_input(
    "USD to INR Rate",
    min_value=1.0,
    value=83.0
)

st.sidebar.markdown("---")

st.sidebar.info(
    "This AI model predicts car prices based on vehicle specifications."
)

# =========================
# LOAD MODEL
# =========================
if not os.path.exists("lasso_model.pkl") or not os.path.exists("scaler.pkl"):
    st.error("❌ Model files not found! Keep .pkl files in same folder.")
    st.stop()

model = joblib.load("lasso_model.pkl")
scaler = joblib.load("scaler.pkl")

# =========================
# FEATURE ORDER
# =========================
carbody_list = ["convertible", "hardtop", "hatchback", "sedan", "wagon"]
drivewheel_list = ["4wd", "fwd", "rwd"]
enginelocation_list = ["front", "rear"]
enginetype_list = ["dohc", "dohcv", "l", "ohc", "ohcf", "ohcv", "rotor"]
cylinder_list = ["eight", "five", "four", "six", "three", "twelve", "two"]

# =========================
# INPUT SECTION
# =========================
st.markdown("### 📊 Enter Car Specifications")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        symboling = st.slider("Symboling", -3, 3, 0)
        wheelbase = st.number_input("Wheelbase", 80.0, 120.0, 95.0)
        carlength = st.number_input("Car Length", 140.0, 220.0, 160.0)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        carwidth = st.number_input("Car Width", 60.0, 80.0, 65.0)
        curbweight = st.number_input("Curb Weight", 1000, 4000, 2000)
        enginesize = st.number_input("Engine Size", 60, 300, 120)
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        horsepower = st.number_input("Horsepower", 40, 300, 80)
        citympg = st.number_input("City MPG", 10, 60, 25)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================
# DROPDOWNS
# =========================
st.markdown("### ⚙️ Configuration")

col4, col5, col6 = st.columns(3)

with col4:
    carbody = st.selectbox("Car Body", carbody_list)
    drivewheel = st.selectbox("Drive Wheel", drivewheel_list)

with col5:
    enginelocation = st.selectbox("Engine Location", enginelocation_list)
    enginetype = st.selectbox("Engine Type", enginetype_list)

with col6:
    cylinders = st.selectbox("Cylinder Number", cylinder_list)

# =========================
# ENCODING
# =========================
def encode(selected, categories):
    return [1 if selected == cat else 0 for cat in categories]

carbody_enc = encode(carbody, carbody_list)
drivewheel_enc = encode(drivewheel, drivewheel_list)
enginelocation_enc = encode(enginelocation, enginelocation_list)
enginetype_enc = encode(enginetype, enginetype_list)
cylinder_enc = encode(cylinders, cylinder_list)

# =========================
# FINAL INPUT
# =========================
input_data = np.array([[ 
    symboling,
    curbweight,
    wheelbase,
    carlength,
    carwidth,
    enginesize,
    horsepower,
    curbweight,
    citympg,
    *carbody_enc,
    *drivewheel_enc,
    *enginelocation_enc,
    *enginetype_enc,
    *cylinder_enc
]])

# =========================
# PREDICTION BUTTON
# =========================
st.markdown("---")

if st.button("💰 Predict Car Price"):
    try:
        scaled = scaler.transform(input_data)
        prediction = model.predict(scaled)

        price_usd = prediction[0]
        price_inr = price_usd * USD_TO_INR

        st.success("✅ Prediction Successful!")

        col7, col8 = st.columns(2)

        with col7:
            st.metric(
                label="💵 Price (USD)",
                value=f"${price_usd:,.2f}"
            )

        with col8:
            st.metric(
                label="🇮🇳 Price (INR)",
                value=f"₹ {price_inr:,.2f}"
            )

    except Exception as e:
        st.error(f"❌ Error: {e}")
