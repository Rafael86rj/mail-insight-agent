# Importa o módulo do sistema operativo para lidar com pastas e caminhos de arquivos
import os
# Importa a variável que define onde os arquivos devem ser guardados (do nosso config.py)
from src.config import DOWNLOAD_FOLDER


def salvar_anexos(email_data):
    """
    Recebe os dados de um e-mail, percorre a sua estrutura
    e guarda no computador apenas os anexos .csv ou .xlsx.
    """

    # Cria a pasta de downloads se ela ainda não existir.
    # 'exist_ok=True' evita que o programa dê erro caso a pasta já esteja lá.
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    # Extrai o objeto da mensagem original que guardámos no dicionário
    msg = email_data["mensagem"]

    # Lista para registar o caminho de todos os arquivos que conseguirmos salvar
    arquivos_salvos = []

    # O e-mail é como uma árvore com vários ramos (texto, html, anexos).
    # O comando .walk() percorre todos esses ramos um por um.
    for part in msg.walk():

        # Se esta parte for apenas um "contentor" de outras partes, ignoramos e seguimos
        if part.get_content_maintype() == "multipart":
            continue

        # Se esta parte não tiver uma "disposição de conteúdo", significa que não é um anexo
        if part.get("Content-Disposition") is None:
            continue

        # Tenta capturar o nome do arquivo anexo
        filename = part.get_filename()

        # Se por algum motivo o anexo não tiver nome, ignoramos
        if not filename:
            continue

        # Convertemos o nome para minúsculas para facilitar a verificação da extensão
        nome_lower = filename.lower()

        # Verificamos se o arquivo é uma planilha (CSV ou Excel)
        if nome_lower.endswith(".csv") or nome_lower.endswith(".xlsx"):

            # Cria o caminho completo: "pasta_downloads/nome_do_arquivo.xlsx"
            caminho = os.path.join(DOWNLOAD_FOLDER, filename)

            # Abre (ou cria) o arquivo no modo "wb" (write binary - escrita binária)
            # Isso é necessário porque arquivos Excel/CSV são dados binários, não apenas texto puro.
            with open(caminho, "wb") as f:
                # Decodifica o conteúdo do anexo e escreve-o no arquivo físico no disco
                f.write(part.get_payload(decode=True))

            # Adiciona o caminho do arquivo salvo à nossa lista de sucesso
            arquivos_salvos.append(caminho)

    # Retorna a lista com os endereços de onde os arquivos foram guardados
    return arquivos_salvos
