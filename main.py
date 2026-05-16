# %%
# ==========================================================
# MAIL INSIGHT AGENT - MAIN
# ==========================================================
# Responsável por:
# 1. Ler e-mails pendentes
# 2. Baixar anexos
# 3. Processar arquivos
# 4. Gerar insights com IA local
# 5. Salvar histórico das análises
# 6. Responder e-mail automaticamente
# 7. Marcar e-mail como processado
# ==========================================================


# ----------------------------------------------------------
# IMPORTAÇÃO DOS MÓDULOS INTERNOS
# ----------------------------------------------------------

# Busca e-mails pendentes e marca como lido
from src.email_reader import buscar_emails_pendentes, marcar_como_lido

# Responsável por salvar anexos recebidos
from src.attachment_handler import salvar_anexos

# Carrega arquivos CSV/XLSX e gera diagnóstico técnico
from src.data_processor import carregar_arquivo, diagnostico_df

# Gera insights utilizando IA local via Ollama
from src.ai_insights import gerar_insights

# Envia resposta por e-mail
from src.email_sender import enviar_resposta

# Sistema de logs
from src.logger import setup_logger

# Salva histórico das análises em CSV
from src.history_manager import salvar_historico

# Converte markdown da IA para HTML
import markdown


# ----------------------------------------------------------
# FUNÇÃO PRINCIPAL
# ----------------------------------------------------------
def main():

    # ------------------------------------------------------
    # INICIALIZA LOGGER
    # ------------------------------------------------------
    logger = setup_logger()

    # ------------------------------------------------------
    # BUSCA E-MAILS PENDENTES
    # ------------------------------------------------------
    mail, emails = buscar_emails_pendentes()

    logger.info(f"Emails encontrados: {len(emails)}")

    # ------------------------------------------------------
    # SE NÃO EXISTIR E-MAIL, ENCERRA
    # ------------------------------------------------------
    if not emails:

        print("Nenhum e-mail pendente para processar.")

        mail.logout()

        return

    # ------------------------------------------------------
    # LOOP PRINCIPAL DOS E-MAILS
    # ------------------------------------------------------
    for item_email in emails:

        try:

            logger.info(
                f"Processando email: {item_email['assunto']}"
            )

            # --------------------------------------------------
            # CAPTURA E LIMPA DESTINATÁRIO
            # --------------------------------------------------
            destinatario = item_email["remetente"]

            # Remove nome e mantém apenas e-mail
            if "<" in destinatario:

                destinatario = (
                    destinatario
                    .split("<")[1]
                    .replace(">", "")
                    .strip()
                )

            # --------------------------------------------------
            # BAIXA ANEXOS
            # --------------------------------------------------
            anexos = salvar_anexos(item_email)

            if not anexos:

                logger.warning(
                    "Nenhum anexo válido encontrado."
                )

                continue

            # --------------------------------------------------
            # RELATÓRIO HTML CONSOLIDADO
            # --------------------------------------------------
            relatorio_html = ""

            # --------------------------------------------------
            # LOOP DOS ARQUIVOS
            # --------------------------------------------------
            for arquivo in anexos:

                logger.info(
                    f"Arquivo processado: {arquivo}"
                )

                # ----------------------------------------------
                # CARREGA ARQUIVO
                # ----------------------------------------------
                df = carregar_arquivo(arquivo)

                # ----------------------------------------------
                # GERA DIAGNÓSTICO
                # ----------------------------------------------
                resumo = diagnostico_df(df)

                # ----------------------------------------------
                # GERA INSIGHTS IA
                # ----------------------------------------------
                insights = gerar_insights(resumo)

                # ----------------------------------------------
                # SALVA HISTÓRICO
                # ----------------------------------------------
                salvar_historico(
                    destinatario,
                    item_email["assunto"],
                    arquivo,
                    resumo,
                    insights
                )

                # ----------------------------------------------
                # CONVERTE MARKDOWN → HTML
                # ----------------------------------------------
                insights_html = markdown.markdown(insights)

                # ----------------------------------------------
                # BLOCO HTML DO ARQUIVO
                # ----------------------------------------------
                trecho = f"""
                <div style="
                    margin-bottom:30px;
                    padding:20px;
                    border:1px solid #ddd;
                    border-radius:10px;
                    background:#ffffff;
                ">

                    <h3 style="color:#0B57D0;">
                        📁 Arquivo: {arquivo}
                    </h3>

                    <table style="
                        border-collapse: collapse;
                        margin-bottom:20px;
                    ">
                        <tr>

                            <td style="
                                padding:12px;
                                border:1px solid #ddd;
                            ">
                                <b>Linhas</b><br>
                                {resumo['linhas']}
                            </td>

                            <td style="
                                padding:12px;
                                border:1px solid #ddd;
                            ">
                                <b>Colunas</b><br>
                                {resumo['colunas']}
                            </td>

                        </tr>
                    </table>

                    <div style="
                        background:#f4f6f8;
                        padding:18px;
                        border-radius:8px;
                        line-height:1.6;
                    ">
                        {insights_html}
                    </div>

                </div>
                """

                # Acumula no relatório
                relatorio_html += trecho

            # --------------------------------------------------
            # CORPO HTML FINAL
            # --------------------------------------------------
            corpo_email = f"""
            <html>

            <body style="
                font-family:Arial;
                padding:30px;
                background:#f9fafb;
                color:#222;
            ">

                <h2 style="color:#0B57D0;">
                    📊 Mail Insight Agent
                </h2>

                <p>Olá,</p>

                <p>
                    A análise solicitada foi concluída com sucesso.
                </p>

                {relatorio_html}

                <hr>

                <p style="
                    color:#777;
                    font-size:13px;
                ">
                    Mensagem automática enviada pelo
                    <b>Mail Insight Agent</b>
                </p>

            </body>

            </html>
            """

            # --------------------------------------------------
            # ENVIA RESPOSTA
            # --------------------------------------------------
            enviar_resposta(
                destinatario,
                item_email["assunto"],
                corpo_email
            )

            logger.info(
                f"Resposta enviada para: {destinatario}"
            )

            # --------------------------------------------------
            # MARCA COMO LIDO
            # --------------------------------------------------
            marcar_como_lido(
                mail,
                item_email["id"]
            )

        # ------------------------------------------------------
        # TRATAMENTO DE ERRO
        # ------------------------------------------------------
        except Exception as erro:

            logger.error(
                f"Erro no processamento: {erro}"
            )

            continue

    # ----------------------------------------------------------
    # ENCERRA CONEXÃO IMAP
    # ----------------------------------------------------------
    mail.logout()


# --------------------------------------------------------------
# PONTO DE ENTRADA
# --------------------------------------------------------------
if __name__ == "__main__":

    main()

# %%
