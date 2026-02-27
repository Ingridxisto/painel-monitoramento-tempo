import streamlit as st
from datetime import datetime
import pandas as pd
import os

from app.services.clima_service import buscar_clima
from app.services.excel_service import salvar_dados

ARQUIVO_EXCEL = "data/dados_climaticos.xlsx"


def iniciar_app():

    st.set_page_config(
        page_title="Painel de Monitoramento do Tempo",
        page_icon="🌦️",
        layout="centered"
    )

    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #667eea, #764ba2);
        }

        .bloco {
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            max-width: 900px;
            margin: auto;
            margin-top: 30px;
        }

        /* 🔥 BOTÃO PERSONALIZADO */
        .stButton > button {
            background: linear-gradient(135deg, #00c6ff, #0072ff);
            color: white;
            border: none;
            padding: 14px 20px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }

        .stButton > button:active {
            transform: scale(0.98);
        }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="bloco">', unsafe_allow_html=True)

    st.markdown("""
        <h1 style='text-align: center; margin-bottom: 5px;
        color: white;'>
            🌦️ Painel de Monitoramento do Tempo
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <p style='text-align: center; color: white; margin-bottom: 30px;'>
            Consulte informações meteorológicas em tempo real
        </p>
    """, unsafe_allow_html=True)

    cidade = st.text_input(
        "Digite o nome da cidade:",
        placeholder="Ex: São Paulo",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # 🔹 BOTÃO
    if st.button("Consultar", use_container_width=True):

        if not cidade:
            st.warning("⚠️ Digite uma cidade antes de consultar.")
        else:
            dados = buscar_clima(cidade)

            if not dados:
                st.error("❌ Cidade não encontrada ou erro na API.")
            else:
                st.success(f"Tempo em {dados['cidade']}")

                # 🌤️ Ícone dinâmico
                icone_url = f"http://openweathermap.org/img/wn/{dados['icone']}@2x.png"
                st.image(icone_url, width=100)

                # 📊 Métricas
                col1, col2, col3 = st.columns(3)

                col1.metric("🌡️ Temperatura (°C)", dados["temperatura"])
                col2.metric("💧 Umidade (%)", dados["umidade"])
                col3.metric("🌬️ Vento (m/s)", dados["vento"])

                st.markdown("---")

                st.write("☁ **Condição do Céu:**", dados["descricao"].capitalize())

                # 🕒 Data e hora
                agora = datetime.now().strftime("%d/%m/%Y %H:%M")
                st.caption(f"Consulta realizada em: {agora}")

                # 💾 Salvar no Excel
                salvar_dados(
                    dados["cidade"],
                    dados["temperatura"],
                    dados["umidade"],
                    dados["descricao"]
                )

                st.info("Dados salvos no histórico com sucesso!")

    # 🔹 FECHA O CARD
    st.markdown('</div>', unsafe_allow_html=True)

    # 📁 HISTÓRICO FORA DO CARD
    if os.path.exists(ARQUIVO_EXCEL):

        st.markdown(
            "<h2 style='color: white;'>📁 Histórico de Consultas</h2>",
            unsafe_allow_html=True
        )

        df = pd.read_excel(ARQUIVO_EXCEL)

        st.dataframe(df, use_container_width=True)

        # 📈 Gráfico automático
        if "Temperatura (°C)" in df.columns:
            st.markdown(
                "<h2 style='color: white;'>📈 Evolução da Temperatura</h2>",
                unsafe_allow_html=True
            )
            st.line_chart(df["Temperatura (°C)"])


if __name__ == "__main__":
    iniciar_app()
