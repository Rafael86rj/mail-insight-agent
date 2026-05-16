# src/data_processor.py

# Importa a biblioteca pandas (apelidada de pd), a ferramenta principal para análise de dados
import pandas as pd
# Importa o módulo os para manipular caminhos de arquivos
import os
# Importa a biblioteca json para converter o diagnóstico em formato JSON, que é mais legível para a IA
import json


def carregar_arquivo(caminho):
    """
    Identifica o tipo de arquivo pela extensão e utiliza 
    o motor de leitura correto do Pandas.
    """

    # Extrai a extensão do arquivo (ex: .csv ou .xlsx) do caminho fornecido
    # splitext divide o caminho em (nome, extensão)
    ext = os.path.splitext(caminho)[1].lower()

    # Se for um arquivo de texto separado por vírgulas (CSV)
    if ext == ".csv":
        return pd.read_csv(caminho)

    # Se for uma planilha do Excel
    elif ext == ".xlsx":
        # Nota: Requer a biblioteca 'openpyxl' instalada (que colocamos no requirements.txt)
        return pd.read_excel(caminho)

    # Caso o arquivo tenha uma extensão diferente (como .pdf ou .txt)
    else:
        # Lança um erro personalizado para avisar que o formato não é válido
        raise ValueError("Formato não suportado")


def diagnostico_df(df):
    """
    Cria um "raio-x" completo da planilha para que possamos 
    explicar à IA como os dados estão estruturados.
    """

    # Criamos um dicionário que resume as características mais importantes da tabela
    info = {
        # Conta quantas linhas existem (índice 0 do shape)
        "linhas": df.shape[0],
        # Conta quantas colunas existem (índice 1 do shape)
        "colunas": df.shape[1],
        # Cria uma lista com os títulos das cabeceiras (nomes das colunas)
        "nomes_colunas": list(df.columns),
        # Conta quantos valores vazios existem em cada coluna e converte para dicionário
        "nulos": df.isnull().sum().to_dict(),
        # Identifica o tipo de dado de cada coluna (texto, número inteiro, decimal, etc)
        "tipos": df.dtypes.astype(str).to_dict(),
        # Numero de colunas duplicadas
        "Colunas_duplicadas": df.T.duplicated().sum(),
        # Numero de linhas duplicadas
        "linhas_duplicadas": df.duplicated().sum(),
        # Amostrar as primeiras 5 linhas do dataframe para a IA entender melhor a estrutura dos dados
        "Amostra dos dado": df.head(3).astype(str).to_dict()
    }

    # Retorna este resumo técnico
    return info
