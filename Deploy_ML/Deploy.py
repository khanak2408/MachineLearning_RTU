import streamlit as st
import joblib

# Load the trained model
model = joblib.load("music-recommender-model")
# Function to make predictions
def make_predictions(features):
    # Assuming features is a list containing the three input features
    prediction = model.predict([features])
    return prediction

# Streamlit UI
st.title("Music Genre Predictor")

# Textboxes for input features
Age = st.text_input("Please provide Age")
# Dropdown for Gender
Gender = st.selectbox("Gender", ["Male", "Female"])

# Convert gender to numerical value
gender_numeric = 1 if Gender == "Male" else 0

# Button to trigger prediction
if st.button("Predict"):
    # Check if all features are provided
    if Age and Gender:
        # Make predictions
        features = [Age, gender_numeric]
        prediction = make_predictions(features)
        st.success(f"The predicted genres are: {prediction}")
    else:
        st.error("Please provide values for all two features.")
