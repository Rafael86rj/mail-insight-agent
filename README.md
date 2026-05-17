# 📊 Mail Insight Agent

Agente autônomo em Python com IA local capaz de:

* Ler e-mails automaticamente
* Baixar anexos CSV/XLSX
* Processar datasets com Pandas
* Gerar insights utilizando LLM local via Ollama
* Responder automaticamente o remetente com relatório HTML
* Registrar logs e histórico das análises

---

# 🚀 Visão Geral

O objetivo do projeto foi construir um pipeline completo de automação analítica utilizando Python + IA local.

O agente monitora e-mails recebidos, identifica anexos de dados, executa análises estruturais do DataFrame e utiliza modelos LLM executados localmente via Ollama para gerar insights automáticos.

O foco principal do projeto foi aprendizado prático de:

* arquitetura modular
* automação
* integração com IA local
* engenharia de prompts
* logs
* persistência histórica
* versionamento Git/GitHub

---

# 🧠 Fluxo do Agente

```text
E-mail recebido
        ↓
Download do anexo
        ↓
Leitura CSV/XLSX
        ↓
Diagnóstico do DataFrame
        ↓
Geração de insights com IA local
        ↓
Criação do relatório HTML
        ↓
Resposta automática por e-mail
        ↓
Persistência em histórico CSV
```

---

# 🖼️ Demonstração

## 📥 Entrada do E-mail

![Entrada Email](Imagens/entrada-email.png)

---

## 📧 Resposta Automática Gerada

![Saída Email](Imagens/saida-email.png)

---

## 💻 Repositório GitHub

![GitHub](Imagens/github.png)

---

# 🏗️ Estrutura do Projeto

```text
mail-insight-agent/
│
├── src/
│   ├── __init__.py
│   ├── ai_insights.py
│   ├── attachment_handler.py
│   ├── config.py
│   ├── data_processor.py
│   ├── email_reader.py
│   ├── email_sender.py
│   ├── history_manager.py
│   └── logger.py
│
├── downloads/
├── logs/
├── output/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

# ⚙️ Tecnologias Utilizadas

* Python
* Pandas
* Ollama
* Qwen 2.5
* IMAP
* SMTP
* Markdown
* Logging
* dotenv

---

# 🤖 IA Local

O projeto utiliza modelos executados localmente via Ollama.

Exemplo utilizado:

```bash
qwen2.5:3b
```

Também foram realizados testes com:

* llama3.2
* gemma2
* phi3
* qwen3

---

# 📊 Funcionalidades

## ✔ Leitura automática de e-mails

Filtra mensagens com assunto:

```text
Analisar Dados
```

---

## ✔ Download automático de anexos

Suporte para:

* `.csv`
* `.xlsx`

---

## ✔ Diagnóstico automático do DataFrame

Extrai informações como:

* linhas
* colunas
* tipos
* valores nulos
* duplicados
* amostra dos dados

---

## ✔ Insights gerados por IA local

A IA produz:

* resumo executivo
* insights principais
* possíveis problemas
* recomendações práticas

---

## ✔ Resposta automática em HTML

O remetente recebe um relatório visual estruturado automaticamente.

---

## ✔ Logs

Logs de execução armazenados em:

```text
logs/
```

---

## ✔ Histórico das análises

Persistência automática em:

```text
output/historico_analises.csv
```

---

# 🔐 Variáveis de Ambiente (.env)

Exemplo:

```env
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_app

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

IMAP_SERVER=imap.gmail.com

OLLAMA_MODEL=qwen2.5:3b
```

---

# ▶️ Como Executar

## 1. Clonar repositório

```bash
git clone https://github.com/Rafael86rj/mail-insight-agent.git
```

---

## 2. Criar ambiente virtual

```bash
python -m venv venv
```

---

## 3. Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 5. Instalar Ollama

[https://ollama.com/](https://ollama.com/)

---

## 6. Baixar modelo

```bash
ollama pull qwen2.5:3b
```

---

## 7. Executar aplicação

```bash
python main.py
```

---

# 📚 Principais Aprendizados

Durante o desenvolvimento foram praticados conceitos como:

* Modularização de aplicações Python
* Integração com IA local via Ollama
* Engenharia de prompts para LLMs locais
* Automação de e-mails com IMAP/SMTP
* Tratamento de erros
* Logs e rastreabilidade
* Persistência histórica
* Variáveis de ambiente (.env)
* Versionamento com Git/GitHub

---

# 📈 Possíveis Evoluções

* Dashboard Streamlit
* Agendamento automático
* Multi-modelos LLM
* Banco de dados
* API REST
* Classificação automática de datasets
* Deploy em servidor

---

# 👨‍💻 Autor

Rafael Fernandes dos Santos

Projeto desenvolvido para aprendizado prático de automação, análise de dados e IA local utilizando Python.
