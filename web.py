import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set the page configuration
st.set_page_config(
    page_title="HealthGuard - Disease Prediction System",
    layout="wide",
    page_icon="🏥"
)

# Custom CSS Styling
st.markdown("""
    <style>
    :root {
        --primary-color: #2c3e50;
        --secondary-color: #3498db;
        --background-color: #f8f9fa;
        --success-color: #27ae60;
        --danger-color: #e74c3c;
    }
    
    .main {
        background-color: var(--background-color);
    }
    
    .stTextInput input, .stSelectbox select, .stNumberInput input {
        border: 2px solid #dcdde1;
        border-radius: 8px;
        padding: 12px;
        font-size: 16px;
        transition: all 0.3s;
    }
    
    .stTextInput input:focus, .stSelectbox select:focus {
        border-color: var(--secondary-color);
        box-shadow: 0 0 8px rgba(52, 152, 219, 0.3);
    }
    
    .stButton button {
        background-color: var(--secondary-color);
        color: white;
        border-radius: 25px;
        padding: 14px 28px;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.3s;
        border: none;
        width: 100%;
    }
    
    .stButton button:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .title-text {
        color: var(--primary-color);
        border-bottom: 3px solid var(--secondary-color);
        padding-bottom: 10px;
        margin-bottom: 30px;
    }
    
    .result-card {
        padding: 25px;
        border-radius: 15px;
        margin: 25px 0;
        color: white;
        text-align: center;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .sidebar .sidebar-content {
        background-color: var(--primary-color) !important;
        padding: 20px;
    }
    
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: var(--primary-color);
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Load models
# Define correct file paths
diabetes_model_path = os.path.join("models", "diabetes_model.sav")
heart_model_path = os.path.join("models", "Heart_model.sav")
parkinsons_model_path = os.path.join("models", "pakinsons_model.sav")

# Check if files exist before loading
if os.path.exists(diabetes_model_path):
    with open(diabetes_model_path, "rb") as f:
        diabetes_model = pickle.load(f)
else:
    st.error(f"Diabetes model file not found: {diabetes_model_path}")

if os.path.exists(heart_model_path):
    with open(heart_model_path, "rb") as f:
        heart_model = pickle.load(f)
else:
    st.error(f"Heart model file not found: {heart_model_path}")

if os.path.exists(parkinsons_model_path):
    with open(parkinsons_model_path, "rb") as f:
        parkinsons_model = pickle.load(f)
else:
    st.error(f"Parkinsons model file not found: {parkinsons_model_path}")

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="HealthGuard",
        options=["Diabetes", "Heart Disease", "Parkinson's Disease"],
        icons=["activity", "heart", "person"],
        menu_icon="hospital",
        default_index=0,
        styles={
            "container": {"background-color": "#2c3e50"},
            "nav-link": {
                "color": "white",
                "font-size": "16px",
                "margin": "10px 0",
                "border-radius": "8px"
            },
            "nav-link-selected": {"background-color": "#3498db"}
        }
    )

# Diabetes Prediction
if selected == "Diabetes":
    st.markdown("<h1 class='title-text'>Diabetes Risk Assessment</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        glucose = st.text_input("Glucose Level")
    with col3:
        blood_pressure = st.text_input("Blood Pressure")
    with col1:
        skin_thickness = st.text_input("Skin Thickness")
    with col2:
        insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function")
    with col2:
        age = st.text_input("Age of the Person")

    if st.button("Assess Diabetes Risk"):
        user_input = [Pregnancies, glucose, blood_pressure, skin_thickness, insulin, 
                     BMI, diabetes_pedigree_function, age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        
        if diab_prediction[0] == 1:
            st.markdown(f"""
                <div class='result-card' style='background-color: #e74c3c;'>
                    <h3>🚨 High Diabetes Risk</h3>
                    <p>Consult a healthcare professional immediately</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='result-card' style='background-color: #27ae60;'>
                    <h3>✅ Low Diabetes Risk</h3>
                    <p>Maintain healthy lifestyle habits</p>
                </div>
            """, unsafe_allow_html=True)

# Heart Disease Prediction
if selected == "Heart Disease":
    st.markdown("<h1 class='title-text'>Cardiac Health Assessment</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex (0=Female, 1=Male)")
    with col3:
        cp = st.text_input("Chest Pain Type (0-3)")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholesterol")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar")
    with col1:
        restecg = st.text_input("Resting ECG")
    with col2:
        thalach = st.text_input("Max Heart Rate")
    with col3:
        exang = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("ST Depression")
    with col2:
        slope = st.text_input("Slope of Peak Exercise")
    with col3:
        ca = st.text_input("Major Vessels")
    with col1:
        thal = st.text_input("Thalassemia")

    if st.button("Assess Cardiac Risk"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, 
                     thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = Heart_model.predict([user_input])
        
        if heart_prediction[0] == 1:
            st.markdown(f"""
                <div class='result-card' style='background-color: #e74c3c;'>
                    <h3>🚨 Cardiac Risk Detected</h3>
                    <p>Immediate medical consultation recommended</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='result-card' style='background-color: #27ae60;'>
                    <h3>✅ Healthy Cardiac Profile</h3>
                    <p>Continue with regular checkups</p>
                </div>
            """, unsafe_allow_html=True)

# Parkinson's Prediction
if selected == "Parkinson's Disease":
    st.markdown("<h1 class='title-text'>Neurological Health Assessment</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP = st.text_input("Mean Fundamental Frequency (Hz)")
    with col2:
        mdvp2 = st.text_input("Maximum Fundamental Frequency (Hz)")
    with col3:
        MDVP3 = st.text_input("Minimum Fundamental Frequency (Hz)")
    with col1:
        MDVP4 = st.text_input("Jitter Percentage")
    with col2:
        MDVP5 = st.text_input("Absolute Jitter")
    with col3:
        MDVP6 = st.text_input("Relative Average Perturbation")
    with col1:
        MDVP7 = st.text_input("Pitch Period Perturbation")
    with col2:
        jitter = st.text_input("Difference of Differences of Pitch")
    with col3:
        MDVP8 = st.text_input("Shimmer (Amplitude Variation)")
    with col1:
        MDVP9 = st.text_input("Shimmer (dB)")
    with col2:
        Shimme1 = st.text_input("3-point Amplitude Perturbation")
    with col3:
        Shimme2 = st.text_input("5-point Amplitude Perturbation")
    with col1:
        MDVP10 = st.text_input("Amplitude Perturbation Quotient")
    with col2:
        Shimme3 = st.text_input("Degree of Amplitude Perturbation")
    with col3:
        NHR = st.text_input("Noise-to-Harmonics Ratio")
    with col1:
        HNR = st.text_input("Harmonics-to-Noise Ratio")
    with col2:
        RPDE = st.text_input("Recurrence Period Density Entropy")
    with col3:
        DFA = st.text_input("Detrended Fluctuation Analysis")
    with col1:
        spread1 = st.text_input("Fundamental Frequency Variation 1")
    with col2:
        spread2 = st.text_input("Fundamental Frequency Variation 2")
    with col3:
        D2 = st.text_input("Correlation Dimension")
    with col1:
        PPE = st.text_input("Pitch Period Entropy")

    if st.button("Assess Neurological Health"):
        user_input = [MDVP, mdvp2, MDVP3, MDVP4, MDVP5, MDVP6, MDVP7, jitter,
                     MDVP8, MDVP9, Shimme1, Shimme2, MDVP10, Shimme3, NHR, HNR,
                     RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        park_prediction = pakinsons_model.predict([user_input])
        
        if park_prediction[0] == 1:
            st.markdown(f"""
                <div class='result-card' style='background-color: #e74c3c;'>
                    <h3>🚨 Neurological Risk Detected</h3>
                    <p>Consult a neurologist immediately</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='result-card' style='background-color: #27ae60;'>
                    <h3>✅ Normal Neurological Profile</h3>
                    <p>Maintain regular health monitoring</p>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        <p>HealthGuard - Clinical Decision Support System | For research purposes only | Consult a healthcare professional for medical advice</p>
    </div>
""", unsafe_allow_html=True)
