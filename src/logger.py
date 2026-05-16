import logging
import os
from datetime import datetime

def setup_logger():
    """
    Configura o sistema de logs da aplicação.
    Cria automaticamente um diretório de logs e define o formato de saída.
    """

    # 1. Garantir que a pasta de destino existe para evitar erros de IO
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # 2. Obter a data atual para nomear o ficheiro (Ex: 2026-05-05.log)
    data = datetime.now().strftime("%Y-%m-%d")

    # 3. Definir o caminho relativo onde o ficheiro será guardado
    log_file = f"logs/{data}.log"

    # 4. Configuração global do logger
    logging.basicConfig(
        filename=log_file,        # Destino das mensagens
        level=logging.INFO,       # Nível mínimo: ignora DEBUG, regista INFO para cima
        # Formato: [Data/Hora] - [Nível de Erro] - [Mensagem]
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"          # Garante suporte a acentos e emojis
    )

    return logging

