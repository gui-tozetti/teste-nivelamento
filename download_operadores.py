import os
import requests

# Criar diretório de downloads se não existir
os.makedirs("downloads/operadoras", exist_ok=True)

# URL do arquivo CSV das operadoras ativas
url_operadoras = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
destino = "downloads/operadoras/Operadoras_Ativas.csv"

print("📥 Baixando Operadoras_Ativas.csv...")
resposta = requests.get(url_operadoras, stream=True)

if resposta.status_code == 200:
    with open(destino, "wb") as f:
        for chunk in resposta.iter_content(chunk_size=1024):
            f.write(chunk)
    print(f"✅ Download concluído: {destino}")
else:
    print(f"❌ Erro ao baixar o arquivo. Código HTTP: {resposta.status_code}")
