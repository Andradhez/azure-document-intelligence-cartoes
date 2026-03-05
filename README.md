# Azure Document Intelligence - Análise de Cartões

Projeto desenvolvido durante o bootcamp da **DIO** utilizando serviços do **Microsoft Azure**.

## 📌 Objetivo

Criar uma aplicação capaz de analisar imagens de cartões utilizando **Azure Document Intelligence**, identificando automaticamente informações presentes no documento.

---

## 🚀 Tecnologias utilizadas

- Python
- Streamlit
- Azure Blob Storage
- Azure Document Intelligence
- Git
- GitHub

---

## ⚙️ Como funciona

1. O usuário envia uma imagem de cartão.
2. A imagem é armazenada no **Azure Blob Storage**.
3. O **Azure Document Intelligence** analisa o documento.
4. O sistema extrai e apresenta as informações do cartão.

---

## 📂 Estrutura do projeto

src/
 ├── app.py
 ├── services/
 │   ├── blob_service.py
 │   └── credit_card_service.py
 ├── utils/
 │   └── Config.py


## 🔐 Variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`.

Exemplo:

ENDPOINT=seu_endpoint_azure
KEY=sua_chave_azure
AZURE_STORAGE_CONNECTION_STRING=sua_connection_string
CONTAINER_NAME=cartoes

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Integração com serviços do Azure
- Upload de arquivos para Blob Storage
- Processamento de documentos com IA
- Uso de variáveis de ambiente para segurança

## 👨‍💻 Autor

Projeto desenvolvido por **Juliano Andrade** durante o bootcamp de **Microsoft Azure AI na DIO*