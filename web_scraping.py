import requests
import os
import zipfile

# Novos links dos PDFs
urls = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

# Criar pasta para salvar os PDFs
os.makedirs("downloads", exist_ok=True)

# Baixar os arquivos
pdf_files = []
for index, url in enumerate(urls, start=1):
    pdf_name = url.split("/")[-1]  # Pega o nome do arquivo da URL
    pdf_path = f"downloads/{pdf_name}"
    
    response = requests.get(url, stream=True)  # Baixar o arquivo em partes
    
    if response.status_code == 200:
        with open(pdf_path, "wb") as file:
            for chunk in response.iter_content(1024):  # Baixar em pedaços de 1KB
                file.write(chunk)
        print(f"Baixado: {pdf_path}")
        pdf_files.append(pdf_path)
    else:
        print(f"Erro ao baixar {url} (Código: {response.status_code})")

# Compactar os arquivos baixados
zip_path = "downloads/anexos.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for pdf in pdf_files:
        zipf.write(pdf, os.path.basename(pdf))

print(f"Arquivos compactados em {zip_path}")
