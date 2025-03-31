import os
import requests

# Criar diretório de downloads
os.makedirs("downloads/demonstrativos", exist_ok=True)

# URL base
url_base = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

# Definir os anos e trimestres
anos = ["2023", "2024"]
trimestres = ["1T", "2T", "3T", "4T"]

# Loop para baixar os arquivos trimestrais de cada ano
for ano in anos:
    for trimestre in trimestres:
        arquivo = f"{trimestre}{ano}.zip"  # Nome correto do arquivo
        url = f"{url_base}{ano}/{arquivo}"  # URL completa do arquivo dentro da pasta do ano
        destino = os.path.join("downloads/demonstrativos", arquivo)

        print(f"📥 Baixando {arquivo}...")
        resposta = requests.get(url, stream=True)

        if resposta.status_code == 200:
            with open(destino, "wb") as f:
                for chunk in resposta.iter_content(chunk_size=1024):
                    f.write(chunk)
            print(f"✅ Download concluído: {destino}")
        else:
            print(f"❌ Erro ao baixar {arquivo}. Código HTTP: {resposta.status_code}")
            