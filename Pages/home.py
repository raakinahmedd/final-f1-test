import streamlit as st
import base64
import pandas as pd
import random
import time

# Ensure the user is logged in
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please log in to access the Home page.")
    st.stop()  


st.title("Welcome to the F1")
st.write("Choose respective pages")

