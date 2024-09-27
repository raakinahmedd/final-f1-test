import streamlit as st
import pandas as pd
import random
import time

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please log in to access the Home page.")
    st.stop() 

def generate_car_data():
    cars = ['001', '002', '003']  # Car IDs
    data = {
        'Car ID': [],
        'Gear': [],
        'Brake Percentage': [],
        'Speed (km/h)': [],
        'RPM': []
    }

    for car in cars:
        gear = random.randint(1, 6)
        brake_percentage = random.uniform(70, 100) if gear == 1 else random.uniform(0, 12)
        speed = random.randint(30, 70) * gear
        rpm = random.randint(1000, 2000) * gear if speed > 0 else 0

        if brake_percentage > 0:
            speed = max(0, speed - int(brake_percentage / 2))
            rpm = max(800, rpm - int(brake_percentage * 10))

        data['Car ID'].append(car)
        data['Gear'].append(gear)
        data['Brake Percentage'].append(round(brake_percentage, 2))
        data['Speed (km/h)'].append(speed)
        data['RPM'].append(rpm)

    return pd.DataFrame(data)


st.title("Real-Time Car Data Dashboard")

# Placeholder for DataFrame
data_placeholder = st.empty()


df = pd.DataFrame(columns=['Car ID', 'Gear', 'Brake Percentage', 'Speed (km/h)', 'RPM'])
df['Car ID'] = ['001', '002', '003']  # Fixed car IDs``


while True:
    
    new_data = generate_car_data()

    # Overwrite the existing data with new data for each car
    df.update(new_data)

    # Display the updated DataFrame in the Streamlit app
    data_placeholder.dataframe(df)

    time.sleep(1)  # Simulate real-time data collection
