# src/email_sender.py

# Importa a biblioteca padrão para envio de e-mails via protocolo SMTP
import smtplib
# Importa a classe para criar o corpo do texto do e-mail
from email.mime.text import MIMEText
# Importa a classe para criar mensagens com múltiplas partes (texto, anexos, etc.)
from email.mime.multipart import MIMEMultipart

# Importa as configurações de servidor e login do nosso ficheiro central
from src.config import (
    EMAIL_USER,
    EMAIL_PASS,
    SMTP_SERVER,
    SMTP_PORT
)


def enviar_resposta(destinatario, assunto_original, corpo):
    """
    Monta e envia uma resposta automática por e-mail com o resultado da análise.
    """

    # Cria o novo assunto, mantendo o original para facilitar a organização na caixa do usuário
    assunto = f"Re: {assunto_original} | Resultado da Análise"

    # Prepara o objeto da mensagem
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = destinatario
    msg["Subject"] = assunto

    # Anexa o texto (o insight da IA) ao corpo do e-mail.
    # Usamos "html" para conteúdo formatado e "utf-8" para garantir que acentos funcionem.
    msg.attach(MIMEText(corpo, "html", "utf-8"))

    try:
        # 1. Cria a conexão com o servidor SMTP (ex: smtp.gmail.com)
        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        # 2. Ativa a criptografia (TLS) para garantir que a senha e o texto viajem seguros
        servidor.starttls()

        # 3. Autentica no servidor com as credenciais do .env
        servidor.login(EMAIL_USER, EMAIL_PASS)

        # 4. Envia o e-mail propriamente dito
        servidor.sendmail(
            EMAIL_USER,
            destinatario,
            msg.as_string()  # Converte todo o objeto da mensagem para o formato de texto que o servidor entende
        )

        # 5. Encerra a conexão com o servidor
        servidor.quit()

        print("E-mail enviado com sucesso.")

    except Exception as erro:
        # Se houver falha (como senha errada ou servidor offline), captura e exibe o erro
        print("Erro ao enviar e-mail:", erro)
