import streamlit as st
import requests
import json

st.set_page_config(
    page_title="ML Model Prediction App",
    page_icon="🤖",
    layout="wide"
)

st.title("Machine Learning Model Prediction")
st.markdown("Enter your input data below for prediction:")

# Inputs for the user
age = st.number_input("Age", min_value=1, max_value=120, step=1)
height = st.number_input("Height (cm)", min_value=50, max_value=300, step=1)
weight = st.number_input("Weight (kg)", min_value=10, max_value=300, step=1)
waist = st.number_input("Waist Circumference (cm)", min_value=30, max_value=200, step=1)
eyesight_left = st.number_input("Eyesight (Left Eye)", min_value=0.0, max_value=5.0, step=0.1)
eyesight_right = st.number_input("Eyesight (Right Eye)", min_value=0.0, max_value=5.0, step=0.1)
hearing_left = st.number_input("Hearing (Left Ear)", min_value=0.0, max_value=10.0, step=0.1)
hearing_right = st.number_input("Hearing (Right Ear)", min_value=0.0, max_value=10.0, step=0.1)
systolic = st.number_input("Systolic BP", min_value=50, max_value=250, step=1)
relaxation = st.number_input("Relaxation BP", min_value=30, max_value=150, step=1)
fasting_blood_sugar = st.number_input("Fasting Blood Sugar (mg/dL)", min_value=50, max_value=500, step=1)
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=500, step=1)
triglyceride = st.number_input("Triglyceride (mg/dL)", min_value=50, max_value=500, step=1)
hdl = st.number_input("HDL (mg/dL)", min_value=20, max_value=150, step=1)
ldl = st.number_input("LDL (mg/dL)", min_value=20, max_value=300, step=1)
hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=5.0, max_value=20.0, step=0.1)
urine_protein = st.number_input("Urine Protein (g/dL)", min_value=0.0, max_value=10.0, step=0.1)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=10.0, step=0.1)
ast = st.number_input("AST (U/L)", min_value=10, max_value=500, step=1)
alt = st.number_input("ALT (U/L)", min_value=10, max_value=500, step=1)
gtp = st.number_input("GTP (U/L)", min_value=10, max_value=500, step=1)
dental_caries = st.selectbox("Dental Caries (Yes=1, No=0)", options=[0, 1])

# Prediction button
if st.button("Get Prediction"):
    data = {
        "age": age,
        "height": height,
        "weight": weight,
        "waist": waist,
        "eyesight_left": eyesight_left,
        "eyesight_right": eyesight_right,
        "hearing_left": hearing_left,
        "hearing_right": hearing_right,
        "systolic": systolic,
        "relaxation": relaxation,
        "fasting_blood_sugar": fasting_blood_sugar,
        "cholesterol": cholesterol,
        "triglyceride": triglyceride,
        "hdl": hdl,
        "ldl": ldl,
        "hemoglobin": hemoglobin,
        "urine_protein": urine_protein,
        "serum_creatinine": serum_creatinine,
        "ast": ast,
        "alt": alt,
        "gtp": gtp,
        "dental_caries": dental_caries,
    }

    try:
        api_url = "http://localhost:8000/predict"  # Ensure this matches your FastAPI endpoint
        response = requests.post(api_url, json=data)
        
        if response.status_code == 200:
            result = response.json()
            st.subheader("Prediction Result:")
            st.json(result)
        else:
            st.error(f"Error: API request failed with status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
