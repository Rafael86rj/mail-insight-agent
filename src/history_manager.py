import pandas as pd
import os
from datetime import datetime


def salvar_historico(
    remetente,
    assunto,
    arquivo,
    resumo,
    insights
):

    caminho = "output/historico_analises.csv"

    registro = {
        "data_processamento": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "remetente": remetente,
        "assunto": assunto,
        "arquivo": arquivo,
        "linhas": resumo.get("linhas"),
        "colunas": resumo.get("colunas"),
        "insights": insights
    }

    df_novo = pd.DataFrame([registro])

    # Se arquivo já existir → append
    if os.path.exists(caminho):

        df_existente = pd.read_csv(caminho)

        df_final = pd.concat(
            [df_existente, df_novo],
            ignore_index=True
        )

    else:
        df_final = df_novo

    df_final.to_csv(
        caminho,
        index=False,
        encoding="utf-8-sig"
    )