# 📊 Mail Insight Agent

Agente autônomo em Python com IA local capaz de:

* Monitorar e-mails automaticamente
* Baixar anexos CSV/XLSX
* Processar datasets com Pandas
* Gerar insights utilizando LLM local via Ollama
* Responder automaticamente o remetente com análises estruturadas em HTML
* Registrar logs e histórico das análises

---

# 🚀 Visão Geral

O projeto foi desenvolvido com foco em aprendizado prático de:

* Arquitetura modular em Python
* Integração com IA local (Ollama)
* Automação de e-mails (IMAP/SMTP)
* Processamento de dados com Pandas
* Logs e rastreabilidade
* Persistência histórica
* Engenharia de Prompt para LLMs locais

---

# 🧠 Fluxo do Agente

```text
E-mail recebido
        ↓
Leitura da caixa de entrada
        ↓
Download do anexo
        ↓
Leitura CSV/XLSX
        ↓
Diagnóstico do DataFrame
        ↓
Geração de insights com IA local
        ↓
Criação de relatório HTML
        ↓
Resposta automática por e-mail
        ↓
Registro de logs e histórico
```

---

# 🏗️ Estrutura do Projeto

```text
Mail Insight Agent/
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
├── .env
└── README.md
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

# 🤖 Modelo Utilizado

O projeto utiliza modelos locais via Ollama.

Exemplo:

```bash
qwen2.5:3b
```

---

# 📧 Funcionalidades

## ✔ Leitura automática de e-mails

Filtra mensagens com assunto:

```text
Analisar Dados
```

---

## ✔ Download automático de anexos

Suporta:

* `.csv`
* `.xlsx`

---

## ✔ Diagnóstico automático do DataFrame

Extrai:

* linhas
* colunas
* tipos
* nulos
* duplicados
* amostra dos dados

---

## ✔ Geração de insights com IA local

A IA gera:

* resumo executivo
* oportunidades
* problemas encontrados
* recomendações práticas

---

## ✔ Resposta automática em HTML

O remetente recebe um relatório estruturado por e-mail.

---

## ✔ Sistema de Logs

Os logs ficam armazenados em:

```text
logs/
```

---

## ✔ Histórico das análises

As análises ficam registradas em:

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
git clone https://github.com/seuusuario/mail-insight-agent.git
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

https://ollama.com/

---

## 6. Baixar modelo

```bash
ollama pull qwen2.5:3b
```

---

## 7. Executar projeto

```bash
python main.py
```

---

# 📌 Aprendizados do Projeto

Durante o desenvolvimento foram praticados conceitos como:

* modularização
* automação de processos
* integração com IA local
* manipulação de arquivos
* tratamento de erros
* logs
* persistência de dados
* engenharia de prompts
* arquitetura de aplicações Python

---

# 📈 Possíveis Evoluções

* Dashboard Streamlit
* Agendamento automático
* Múltiplos modelos de IA
* Classificação automática de datasets
* Banco de dados
* API REST
* Deploy em servidor

---

# 👨‍💻 Autor

Rafael Fernandes dos Santos

Projeto desenvolvido para aprendizado prático de automação, análise de dados e IA local com Python.
