from enum import Enum

BASE_URL = 'https://api.moip.com.br/v2'
BASE_URL_SANDBOX = 'https://sandbox.moip.com.br/v2'

CUSTOMER_URI = '/customers'
CREDIT_CARD_URI = '/fundinginstruments'
ORDER_URI = '/orders'
TRANSACTION_URI = '/payments'

def get_urls(sandbox=False):
    BASE = BASE_URL

    if sandbox:
        BASE = BASE_URL_SANDBOX

    return {
        'CUSTOMER_URL': BASE+CUSTOMER_URI,
        'CREDIT_CARD_URL': BASE+CREDIT_CARD_URI,
        'ORDER_URL': BASE+ORDER_URI,
        'TRANSACTION_URL': BASE+TRANSACTION_URI,
    }

class DocumentType(Enum):
    CPF = 'CPF'
    CNPJ = 'CNPJ'

class FundingInstrumentMethod(Enum):
    CREDIT_CARD = 'CREDIT_CARD'
    BOLETO = 'BOLETO'

class ReceiverType(Enum):
    PRIMARY = 'PRIMARY'
    SECONDARY = 'SECONDARY'
