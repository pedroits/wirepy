from enum import Enum

API_URL = 'https://api.moip.com.br/v2'
API_URL_SANDBOX = 'https://sandbox.moip.com.br/v2'

CONNECT_URL = 'https://connect.moip.com.br/oauth'
CONNECT_URL_SANDBOX = 'https://connect-sandbox.moip.com.br/oauth'

CUSTOMER_URI = '/customers'
CREDIT_CARD_URI = '/fundinginstruments'
ORDER_URI = '/orders'
TRANSACTION_URI = '/payments'
TOKEN_URI = '/token'

def get_urls(sandbox=False):
    BASE_API = API_URL
    BASE_CONNECT = CONNECT_URL

    if sandbox:
        BASE_API = API_URL_SANDBOX
        BASE_CONNECT = CONNECT_URL_SANDBOX

    return {
        'CUSTOMER_URL': BASE_API+CUSTOMER_URI,
        'CREDIT_CARD_URL': BASE_API+CREDIT_CARD_URI,
        'ORDER_URL': BASE_API+ORDER_URI,
        'TRANSACTION_URL': BASE_API+TRANSACTION_URI,
        'TOKEN_URL': BASE_CONNECT+TOKEN_URI
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
