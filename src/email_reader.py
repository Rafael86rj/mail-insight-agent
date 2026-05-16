# src/email_reader.py
# %%
# Importa a biblioteca para conexão segura com servidores de e-mail (IMAP)
import imaplib
# Importa ferramentas para processar o conteúdo das mensagens de e-mail
import email
# Importa a ferramenta específica para traduzir cabeçalhos (como o Assunto) de bytes para texto
from email.header import decode_header

# Importa as configurações que definimos no arquivo anterior (config.py)
from src.config import (
    EMAIL_USER,
    EMAIL_PASS,
    IMAP_SERVER,
    EMAIL_SUBJECT_TRIGGER
)

def decodificar_texto(texto):
    """
    Transforma o texto bruto do e-mail (que vem em formato de máquina)
    em texto legível, tratando acentos e caracteres especiais.
    """
    # Quebra o cabeçalho em partes e identifica a codificação (ex: UTF-8)
    partes = decode_header(texto)
    texto_final = ""

    for parte, encoding in partes:
        # Se a parte do texto estiver em formato de 'bytes', precisamos decodificar
        if isinstance(parte, bytes):
            # Tenta decodificar usando o padrão encontrado ou assume UTF-8
            texto_final += parte.decode(encoding or "utf-8", errors="ignore")
        else:
            # Se já for texto comum, apenas adiciona ao resultado
            texto_final += parte

    return texto_final

def buscar_emails_pendentes():
    """
    Faz o trabalho pesado: conecta ao e-mail, procura mensagens 
    não lidas e filtra as que têm o assunto correto.
    """

    try:
        # 1. Conecta ao servidor usando SSL (conexão segura/criptografada)
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        # 2. Faz o login com as credenciais do .env
        mail.login(EMAIL_USER, EMAIL_PASS)

        # 3. Seleciona a Caixa de Entrada (inbox)
        mail.select("inbox")

        # 4. Busca por e-mails que ainda não foram lidos (UNSEEN)
        status, mensagens = mail.search(None, '(UNSEEN)')

        # Converte a lista de IDs de e-mail de uma string única para uma lista individual
        ids = mensagens[0].split()

        resultados = []

        # 5. Loop para processar cada e-mail encontrado
        for email_id in ids:
            # Busca o conteúdo completo do e-mail pelo seu ID
            status, dados = mail.fetch(email_id, "(RFC822)")
            # Converte os dados brutos em um objeto de mensagem tratável pelo Python
            msg = email.message_from_bytes(dados[0][1])

            # Decodifica o assunto para podermos ler corretamente
            assunto = decodificar_texto(msg["Subject"])

            # Obtém quem enviou o e-mail
            remetente = msg["From"]

            # 6. Verifica se a "palavra-chave" configurada está no assunto (ignora maiúsculas/minúsculas)
            if EMAIL_SUBJECT_TRIGGER.lower() in assunto.lower():
                # Se for o e-mail certo, guarda as informações na nossa lista de resultados
                resultados.append({
                    "id": email_id,
                    "assunto": assunto,
                    "remetente": remetente,
                    "mensagem": msg,
                    "uid": email_id.decode()  # Decodifica o ID para string legível
                })

        # 7. Marca os e-mails como lidos para evitar reprocessamento
        return mail, resultados
    
    

    except Exception as erro:
        # Se algo der errado (senha errada, sem internet), avisa o erro
        print("Erro ao ler e-mails:", erro)
        return []
    
def marcar_como_lido(mail, uid):
    """
    Marca o e-mail como lido para evitar reprocessamento.
    """
    mail.store(uid, '+FLAGS', '\\Seen')
    
