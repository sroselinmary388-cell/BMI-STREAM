import streamlit as st
import requests

# FastAPI backend URL (make sure the FastAPI server is running)
API_URL = "http://127.0.0.1:8000/search/"

# Streamlit page configuration
st.title("BMI Calculator")
st.markdown("""
    This app allows you to calculate your Body Mass Index (BMI) based on your weight and height.
    Enter your weight (kg) and height (cm) to get the result.
""")

# Get user input for weight and height
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=50.0, step=1.0)

# Button to submit the form
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        # Sending request to FastAPI backend
        response = requests.post(API_URL, params={"w": weight, "h": height})

        if response.status_code == 200:
            data = response.json()
            bmi_value = data["bmi"]
            category = data["a"]

            # Display the result
            st.subheader(f"Your BMI: {bmi_value:.2f}")
            st.write(f"You are considered: **{category}**")
        else:
            st.error("Error: Unable to get response from the server.")
    else:
        st.error("Please enter valid weight and height.")
