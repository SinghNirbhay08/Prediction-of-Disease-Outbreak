# HealthGuard - Disease Prediction System

\
*A Clinical Decision Support System for Predicting Diabetes, Heart Disease, and Parkinson's Disease*

## 🚀 Overview

HealthGuard is an AI-powered disease prediction system that helps users assess their risk levels for **Diabetes**, **Heart Disease**, and **Parkinson's Disease** based on input medical parameters. Built with **Streamlit**, this project leverages **machine learning models** to provide instant health assessments.

## 🏆 Features

- **Diabetes Risk Assessment**: Predicts the likelihood of diabetes using relevant health indicators.
- **Heart Disease Assessment**: Evaluates cardiac health based on clinical parameters.
- **Parkinson's Disease Assessment**: Analyzes neurological data to determine Parkinson's risk.
- **Modern UI**: Intuitive and responsive interface designed with custom CSS.
- **Real-Time Predictions**: Instant results with color-coded risk assessments.
- **Multi-Disease Prediction**: Choose from multiple disease assessments via a sidebar menu.

## 📸 Project Screenshot
### Figure -1 : Diabetes risk assessment interface (Negative result)
 ![HealthGuard - Disease Prediction System - Google Chrome 16-02-2025 16_23_14](https://github.com/user-attachments/assets/32153969-ed37-46b3-a3c1-8913ff12a991)

-------


### Figure - 2 : Diabetes risk assessment interface (Positive result)
![HealthGuard - Disease Prediction System - Google Chrome 16-02-2025 16_24_02](https://github.com/user-attachments/assets/e0be907e-48e1-4976-8036-653598480188)

------


 
### Figure - 3 : Cardiac risk assessment interface (Negative result)
![HealthGuard - Disease Prediction System - Google Chrome 16-02-2025 16_25_47](https://github.com/user-attachments/assets/09647747-6243-4564-b0a2-682787f0614c)

--------

 

### Figure -4 : Cardiac risk assessment interface (Positive result)
![HealthGuard - Disease Prediction System - Google Chrome 16-02-2025 16_26_44](https://github.com/user-attachments/assets/4c95a337-f6ce-49d9-adae-07a98e991a8d)


-------

### Figure - 5 : Parkinsons disease assessment interface (Negative result)
![HealthGuard - Disease Prediction System - Google Chrome 16-02-2025 16_36_26](https://github.com/user-attachments/assets/f019dbdc-bd29-4109-b0e8-8c327c046fc7)


-------
 

### Figure – 6 : Parkinsons disease assessment interface (Positive result)

![HealthGuard - Disease Prediction System - Google Chrome 16-02-2025 16_31_20](https://github.com/user-attachments/assets/bd386f5b-c9ca-4663-98ff-e79ff056984f)


 ---------------------





## 🏗️ Tech Stack

- **Python**
- **Streamlit** (for UI & interactivity)
- **Scikit-Learn** (for ML models)
- **Pickle** (for model serialization)
- **CSS** (for UI customization)

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
https://github.com/SinghNirbhay08/Prediction-of-Disease-Outbreak
cd HealthGuard
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run web.py
```

## 📊 Machine Learning Models Used

The system uses **pre-trained machine learning models** to predict diseases:

- **Diabetes Prediction Model** (Trained on the PIMA Indian Diabetes Dataset)
- **Heart Disease Prediction Model** (Based on UCI Heart Disease Dataset)
- **Parkinson's Disease Model** (Trained on Parkinson’s dataset)

## 📜 Usage

1. **Choose a Disease** from the sidebar menu.
2. **Enter the required health parameters** (e.g., glucose levels, blood pressure, BMI, etc.).
3. **Click the "Assess Risk" button** to get instant results.
4. **Interpret Results:**
   - ✅ **Green:** Low risk (Maintain healthy habits)
   - 🚨 **Red:** High risk (Consult a medical professional)

## 📁 Project Structure

```
HealthGuard/
│── models/  # Serialized ML models (.sav files)
│── app.py   # Main Streamlit app script
│── requirements.txt  # Dependencies
│── README.md  # Project documentation
```

## 💡 Future Enhancements

- 🏥 **Integration with Health APIs** (e.g., Fitbit, Apple Health)
- 📊 **Enhanced Data Visualization** for better risk analysis
- 🔍 **Improved Model Accuracy** using Deep Learning techniques

## 🤝 Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Commit changes and push to your fork.
4. Submit a pull request.

## 📜 Disclaimer

This tool is for **research and educational purposes only**. It is not a substitute for professional medical advice. Always consult a healthcare provider for medical concerns.

## ⭐ Show Some Support

If you found this project helpful, give it a ⭐ on GitHub!

---

*Developed by **Nirbhay Singh ** 💙*

