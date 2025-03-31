import pdfplumber
import pandas as pd

# Caminho do arquivo PDF
pdf_path = "downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Lista para armazenar os dados das tabelas
data = []

# Abrir o PDF e extrair tabelas
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                data.append(row)

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

# Salvar como CSV
csv_path = "downloads/anexo_I_extraido.csv"
df.to_csv(csv_path, index=False, header=False)

print(f"Arquivo CSV salvo em: {csv_path}")
