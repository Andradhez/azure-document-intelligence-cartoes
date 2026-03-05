import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card


def configure_interface():
    st.title("upload de arquivos Dio - desafio 1 - Azure - fake Docs")

    uploaded_file = st.file_uploader(
        "Escolha um arquivo",
        type=["jpg", "jpeg", "png"],
        key="upload_cartao"
    )

    if uploaded_file is not None:
        file_name = uploaded_file.name

        # Enviar para o blob storage e receber SAS URL
        blob_url = upload_blob(uploaded_file, file_name)

        if blob_url:
            st.success(f"Arquivo '{file_name}' enviado com sucesso para o Azure Blob Storage")

            # Analisar cartão via Document Intelligence
            credit_card_info = analyze_credit_card(blob_url)

            show_imagem_and_validation(blob_url, credit_card_info)
        else:
            st.error(f"Erro ao enviar o arquivo {file_name} para o Azure Blob Storage")


def show_imagem_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", width="stretch")

    st.write("Resultados de validação:")

    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown("<h1 style='color:green;'>Cartão de crédito válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome: {credit_card_info.get('card_name')}")
        st.write(f"Número: {credit_card_info.get('card_number')}")
        st.write(f"Validade: {credit_card_info.get('expiry_date')}")
        st.write(f"Banco: {credit_card_info.get('bank_name')}")
    else:
        st.markdown("<h1 style='color:red;'>Cartão de crédito inválido</h1>", unsafe_allow_html=True)
        st.write("Não foi possível extrair dados do cartão (verifique se a imagem é legível e se o serviço tem acesso ao arquivo).")


if __name__ == "__main__":
    configure_interface()