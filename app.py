import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('flight_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the prediction function
def predict_price(input_data):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    # Make prediction
    prediction = model.predict(input_df)
    return prediction[0]

# Streamlit app
def main():
    st.title("Flight Price Prediction")

    # Input fields
    airline = st.selectbox("Airline", ["Air Asia", "Air India", "GoAir","Indigo","Jet Airways","Jet Airways Business","Multiple Carriers","Multiple Carriers    Premium  Economy","SpiceJet","TruJet","Vistara","Vistara Premium Economy"])  # Replace with actual airline names
    source = st.selectbox("Source", ["Bangalore", "Chennai", "Delhi","Kokata","Mumbai"])  # Replace with actual source cities
    destination = st.selectbox("Destination", ["Bangalore", "Cochin", "Delhi","Hyderabad","Kolkata","New Delhi"])  # Replace with actual destination cities
    total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])
    journey_day = st.number_input("Journey Day", min_value=1, max_value=31, step=1)
    journey_month = st.number_input("Journey Month", min_value=1, max_value=12, step=1)
    dep_hour = st.number_input("Departure Hour", min_value=0, max_value=23, step=1)
    dep_minute = st.number_input("Departure Minute", min_value=0, max_value=59, step=1)
    arrival_hour = st.number_input("Arrival Hour", min_value=0, max_value=23, step=1)
    arrival_minute = st.number_input("Arrival Minute", min_value=0, max_value=59, step=1)
    duration_hours = st.number_input("Duration Hours", min_value=0, max_value=100, step=1)
    duration_minutes = st.number_input("Duration Minutes", min_value=0, max_value=59, step=1)

    # Create input data dictionary
    input_data = {
        'Airline': airline,
        'Source': source,
        'Destination': destination,
        'Total_Stops': total_stops,
        'Journey_day': journey_day,
        'Journey_month': journey_month,
        'Dep_hour': dep_hour,
        'Dep_minute': dep_minute,
        'Arrival_hour': arrival_hour,
        'Arrival_minute': arrival_minute,
        'Duration_hours': duration_hours,
        'Duration_minutes': duration_minutes
    }

    # Predict button
    if st.button("Predict"):
        result = predict_price(input_data)
        st.success(f"Estimated Flight Price: ₹{result:.2f}")

if __name__ == '__main__':
    main()
