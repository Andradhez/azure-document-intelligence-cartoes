import re
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from ultils.Config import Config


def analyze_credit_card(card_url: str):

    client = DocumentIntelligenceClient(
        endpoint=Config.ENDPOINT,
        credential=AzureKeyCredential(Config.KEY)
    )

    # 1️⃣ Tenta usar modelo de cartão
    poller = client.begin_analyze_document(
        "prebuilt-creditCard",
        body=AnalyzeDocumentRequest(url_source=card_url)
    )

    result = poller.result()

    if not result.documents:
        return None

    fields = result.documents[0].fields

    card_name = fields.get("CardHolderName")
    card_number = fields.get("CardNumber")
    expiry = fields.get("ExpirationDate")
    bank = fields.get("IssuingBank")

    data = {
        "card_name": card_name.content if card_name else None,
        "card_number": card_number.content if card_number else None,
        "expiry_date": expiry.content if expiry else None,
        "bank_name": bank.content if bank else None,
    }

    # 2️⃣ Se banco não veio, tenta detectar pelo OCR
    if not data["bank_name"]:

        poller = client.begin_analyze_document(
            "prebuilt-read",
            body=AnalyzeDocumentRequest(url_source=card_url)
        )

        ocr = poller.result()

        text = " ".join(
            line.content.lower()
            for page in ocr.pages
            for line in page.lines
        )

        if "bradesco" in text:
            data["bank_name"] = "Bradesco"
        elif "nubank" in text:
            data["bank_name"] = "Nubank"
        elif "pagbank" in text:
            data["bank_name"] = "PagBank"

    return data