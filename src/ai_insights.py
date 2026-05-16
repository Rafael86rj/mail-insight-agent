# Importa a biblioteca para interagir com o Ollama (IA local)
import ollama
# Importa o nome do modelo (ex: 'qwen2.5') definido no ficheiro de configuração
from src.config import OLLAMA_MODEL


def gerar_insights(resumo):
    """
    Envia o resumo dos dados para a IA e garante que o modelo
    seja removido da memória RAM após a execução.
    """

    # Criação do comando (Prompt) usando as informações extraídas pelo Pandas
    prompt = f"""
Você é um analista de dados sênior.

Analise o dataset com base nas informações abaixo.

📊 Estrutura:
- Linhas: {resumo.get('linhas', 'N/A')}
- Colunas: {resumo.get('colunas', 'N/A')}
- Campos: {resumo.get('nomes_colunas', [])}

📊 Qualidade dos dados:
- Nulos: {resumo.get('nulos', {})}
- Tipos: {resumo.get('tipos', {})}
- Linhas duplicadas: {resumo.get('linhas_duplicadas', 0)}

📊 Amostra:
{resumo.get('amostra_dados', {})}

Regras:
- NÃO inventar dados
- NÃO extrapolar além das informações
- Ser objetivo

Gere:

1. Resumo executivo (máx 3 linhas)
2. Principais insights (máx 3 bullets)
3. Problemas identificados (máx 3 bullets)
4. Recomendações práticas (máx 3 bullets)
"""

    # O bloco 'try' tenta executar o código principal
    try:
        # Envia o prompt para o Ollama e aguarda a resposta
        resposta = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            options={
                "temperature": 0.2,
                "num_predict": 600,
                "num_thread": 8
            }


        )

        # Retorna apenas o texto da resposta gerada pela IA
        conteudo = resposta.get("message", {}).get("content", "")

        if not conteudo.strip():
            return "⚠️ IA não conseguiu gerar resposta. Tente reduzir o tamanho do input."

        return conteudo

    # O bloco 'finally' é executado SEMPRE, quer o código acima funcione ou dê erro
    finally:
        # DOCUMENTAÇÃO: Limpeza de Memória RAM
        # Por padrão, o Ollama mantém o modelo na memória por 5 minutos após o uso.
        # Ao enviar mensagens vazias com 'keep_alive=0', forçamos o Ollama a
        # descarregar o modelo da RAM imediatamente.
        ollama.chat(
            model=OLLAMA_MODEL,
            messages=[],
            keep_alive=0
        )
