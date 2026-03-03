import tkinter as tk

from app.services.clima_service import buscar_clima
from app.services.excel_service import salvar_dados


def acao_buscar():
    cidade = entrada_cidade.get().strip()

    dados = buscar_clima(cidade)

    if not dados:
        label_resultado.config(text="❌ Cidade não encontrada.")

    label_resultado.config(
        text=(
            f"📍 Cidade: {dados['cidade']}\n"
            f"🌡 Temperatura: {dados['temperatura']} °C\n"
            f"💧 Umidade: {dados['umidade']}%\n"
            f"☁ Céu: {dados['descricao'].capitalize()}"
        )
    )

    salvar_dados(
        dados["cidade"],
        dados["temperatura"],
        dados["umidade"],
        dados["descricao"]
    )


# ================= INTERFACE =================

root = tk.Tk()
root.title("Consulta de Clima")
root.geometry("350x260")

tk.Label(root, text="Digite a cidade:", font=("Arial", 10)).pack(pady=5)
entrada_cidade = tk.Entry(root, width=30)
entrada_cidade.pack(pady=5)

tk.Button(root, text="Buscar Clima", command=acao_buscar, width=20).pack(pady=10)

label_resultado = tk.Label(root, text="", font=("Arial", 10))
label_resultado.pack(pady=10)

root.mainloop()
