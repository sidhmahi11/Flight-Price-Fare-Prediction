import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('flight_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load feature names used during training
with open("feature_names.pkl", "rb") as f:
    feature_names = pickle.load(f)

# Define the prediction function
def predict_price(input_data):
    try:
        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # One-hot encode categorical variables
        input_df = pd.get_dummies(input_df)

        # Ensure all expected columns are present
        for col in feature_names:
            if col not in input_df.columns:
                input_df[col] = 0  # Add missing columns with 0

        # Reorder columns to match training data
        input_df = input_df[feature_names]

        # Make prediction
        prediction = model.predict(input_df)

        return round(prediction[0])  # Round the estimated price

    except Exception as e:
        return f"Error in prediction: {str(e)}"

# Streamlit app
def main():
    st.title("Flight Price Estimator")

    # User Inputs
    airlines = ["Air Asia", "Air India", "GoAir", "IndiGo", "Jet Airways", "Jet Airways Business", 
                "Multiple carriers", "Multiple carriers Premium Economy", "SpiceJet", "Trujet", "Vistara", 
                "Vistara Premium economy"]
    Airline = st.selectbox("Select Airline", airlines)

    sources = ["Bangalore", "Chennai", "Delhi", "Kolkata", "Mumbai"]
    Source = st.selectbox("Select Source", sources)

    destinations = ["Bangalore", "Cochin", "Delhi", "Hyderabad", "Kolkata", "New Delhi"]
    Destination = st.selectbox("Select Destination", destinations)

    Total_Stops = st.slider("Total Stops", 0, 4, 1)
    Journey_Day = st.number_input("Journey Day", min_value=1, max_value=31, step=1)
    Journey_Month = st.number_input("Journey Month", min_value=1, max_value=12, step=1)
    Dep_Hour = st.slider("Departure Hour", 0, 23, 10)
    Dep_Minute = st.slider("Departure Minute", 0, 59, 30)
    Arrival_Hour = st.slider("Arrival Hour", 0, 23, 15)
    Arrival_Minute = st.slider("Arrival Minute", 0, 59, 45)
    Duration_Hours = st.slider("Duration Hours", 0, 24, 2)
    Duration_Minutes = st.slider("Duration Minutes", 0, 59, 30)

    # Prepare input data dictionary
    input_data = {
        'Airline': Airline,
        'Source': Source,
        'Destination': Destination,
        'Total_Stops': Total_Stops,
        'Journey_Day': Journey_Day,
        'Journey_Month': Journey_Month,
        'Dep_Hour': Dep_Hour,
        'Dep_Minute': Dep_Minute,
        'Arrival_Hour': Arrival_Hour,
        'Arrival_Minute': Arrival_Minute,
        'Duration_Hours': Duration_Hours,
        'Duration_Minutes': Duration_Minutes
    }

    # Predict button
    if st.button("Estimate Price"):
        result = predict_price(input_data)
        st.success(f"Estimated Flight Price: ₹{result}")

if __name__ == '__main__':
    main()
