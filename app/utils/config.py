import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

if "OPENWEATHER_API_KEY" in st.secrets:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
else:
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
