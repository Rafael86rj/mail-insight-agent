# Importa a função para carregar arquivos de configuração .env
from dotenv import load_dotenv
# Importa o módulo 'os' para interagir com o sistema operativo (ler variáveis)
import os

# Executa a função que lê o arquivo .env e coloca os valores na memória do programa
load_dotenv()

# ==============================================================================
# CONFIGURAÇÕES DE E-MAIL
# ==============================================================================
# Procura no .env o utilizador e a senha. Se não existirem, ficam como None (vazio)
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

# Procura o servidor IMAP. Se não encontrar no .env, usa "imap.gmail.com" como padrão
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")

# Procura o servidor SMTP. Se não encontrar no .env, usa "smtp.gmail.com" como padrão
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")

# Procura a porta SMTP e converte para número inteiro (int), padrão 587 (TLS)
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

# ==============================================================================
# CONFIGURAÇÕES DE IA / OLLAMA
# ==============================================================================
# Define qual modelo de IA será usado. Caso não definido, usa o "qwen3:4b"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")

# ==============================================================================
# CONFIGURAÇÕES DE PASTAS (DIRETÓRIOS)
# ==============================================================================
# Define onde os anexos serão salvos. Padrão: pasta chamada "downloads"
DOWNLOAD_FOLDER = os.getenv("DOWNLOAD_FOLDER", "downloads")

# Define onde os resultados processados serão salvos. Padrão: pasta chamada "output"
OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER", "output")

# ==============================================================================
# REGRAS DO AGENTE (LÓGICA DE NEGÓCIO)
# ==============================================================================
# Define o termo que o script deve procurar no assunto do e-mail para começar a agir
EMAIL_SUBJECT_TRIGGER = os.getenv("EMAIL_SUBJECT_TRIGGER", "Analisar Dados")
