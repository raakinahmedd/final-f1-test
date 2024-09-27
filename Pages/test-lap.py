import streamlit as st
import pandas as pd
import random
import time

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please log in to access the Home page.")
    st.stop() 
    
# Function to highlight the first row 
def highlight_first_row(x):
    df_style = pd.DataFrame('', index=x.index, columns=x.columns)
    df_style.iloc[0, :] = 'background-color: rgba(255, 255, 0, 0.5)'  
    return df_style


def generate_lap_data(lap_id):
    lap_record = {
        'lap_id': [],      
        'driver_id': [],        
        'sector1_time': [],  
        'sector2_time': [], 
        'sector3_time': [],  
        'total_time': []      
    }
    
    driver_names = ['HAM', 'LEC', 'SAI', 'VER', 'RUS', 'PIA', 'NOR', 'PER']
    drivers = [f"{x}" for x in driver_names]

    for i in drivers:
        sector1_time = round(random.uniform(25, 30), 3)  
        sector2_time = round(random.uniform(30, 35), 3)  
        sector3_time = round(random.uniform(20, 25), 3)  
        
        total_time = round(sector1_time + sector2_time + sector3_time, 3) 
        
    
        lap_record['lap_id'].append(f'Lap-{lap_id}')    
        lap_record['driver_id'].append(i)        
        lap_record['sector1_time'].append(sector1_time)  
        lap_record['sector2_time'].append(sector2_time)   
        lap_record['sector3_time'].append(sector3_time)  
        lap_record['total_time'].append(total_time)      

    return pd.DataFrame(lap_record)

st.title('F1 Lap Data')

placeholder = st.empty()

lap_message_placeholder = st.empty()

# Initialize an empty DataFrame to hold lap data
df = pd.DataFrame(columns=['lap_id', 'driver_id', 'sector1_time', 'sector2_time', 'sector3_time', 'total_time'])

lap_id = 1
previous_fastest_driver = None  

while True:
    new_data = generate_lap_data(lap_id)
    new_data_sorted = new_data.sort_values(by="total_time", ascending=True)

    fastest_lap_index = new_data_sorted['total_time'].idxmin()
    fastest_driver = new_data_sorted.loc[fastest_lap_index, 'driver_id']

    styled_df = new_data_sorted.style.apply(highlight_first_row, axis=None)
    placeholder.dataframe(styled_df)

   
    if previous_fastest_driver is not None:
        lap_message_placeholder.success(f"End of Lap-{lap_id-1} - Fastest lap: {previous_fastest_driver}")
    

    previous_fastest_driver = fastest_driver

    lap_id += 1

    time.sleep(5) 
    lap_message_placeholder.empty()
    time.sleep(1)
