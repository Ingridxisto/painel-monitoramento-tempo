import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Se não encontrar no .env, pega do secrets da Streamlit
if not API_KEY:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
