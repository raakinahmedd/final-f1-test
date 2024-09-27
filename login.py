import streamlit as st
import pandas as pd
import numpy as np
import time
import json
import base64

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False



st.set_page_config(
    page_title="mutli=page-app",
)

def login():

    dic = {
        "name": st.text_input("Name"),
        "password": st.text_input("Password", type="password")
    }



    if st.button("Submit"):
        input_dara = json.dumps(dic, indent=4)
        process = json.loads(input_dara)
        if process["name"] == "raakin" and process["password"] == "raakin":
            st.write("Success")
            st.session_state["logged_in"] = True
            st.success("Login successful! You can now access the Home page.")
        else:
            st.error("Invalid User")


if not st.session_state['logged_in']:
    st.title("LOGIN PAGE")
    login()
else:
    st.success("You are already logged in! Go to the Home page.")

    
