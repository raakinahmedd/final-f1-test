import random
import time
import pandas as pd
import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please log in to access the Home page.")
    st.stop() 

def initial_HR(num_drivers):
    return [random.randint(60, 80) for _ in range(num_drivers)]



def update_HR(heart_rates):

    for i, x in enumerate(heart_rates):
        if random.random() > 0.5:
            heart_rates[i] += random.randint(5, 15)
        else:
            heart_rates[i] -= random.randint(1, 10)  
        heart_rates[i] = max(60, min(heart_rates[i], 200))  # Bound the heart rate


def main():
    st.title("F1 Driver Heart Rates")
    driver_names = [
        "Lewis Hamilton", "Max Verstappen", "Charles Leclerc", 
        "Fernando Alonso", "Lando Norris", "Carlos Sainz", 
        "George Russell", "Sergio Pérez"
    ]
    
    num_drivers = len(driver_names)
    heart_rates = initial_HR(num_drivers)

    df = pd.DataFrame({
        'Driver': driver_names,
        'Heart Rate (bpm)': heart_rates
    })
    
    table_placeholder = st.empty()  
    
    while True:
        update_HR(heart_rates)
        
        df['Heart Rate (bpm)'] = heart_rates
  
        table_placeholder.table(df)
        
        time.sleep(1)

if __name__ == "__main__":
    main()
