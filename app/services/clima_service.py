import requests
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

API_KEY = os.getenv("OPENWEATHER_API_KEY") or st.secrets.get("OPENWEATHER_API_KEY")


def buscar_clima(cidade: str):
    if not cidade:
        cidade = "São Paulo"

    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(BASE_URL, params=params)

    print("API_KEY:", API_KEY)
    print("Status code:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:
        return None

    dados = response.json()

    return {
        "cidade": dados["name"],
        "temperatura": dados["main"]["temp"],
        "descricao": dados["weather"][0]["description"],
        "umidade": dados["main"]["humidity"],
        "vento": dados["wind"]["speed"],
        "icone": dados["weather"][0]["icon"]
    }
