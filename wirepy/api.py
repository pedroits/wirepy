import logging
import requests

from base64 import b64encode
from simplejson.errors import JSONDecodeError

from .models import WirecardFundingInstrument
from .settings import get_urls

logger = logging.getLogger()

class Wirecard(object):
    
    def __init__(self, token, key, sandbox=False):
        self.token = token
        self.key = key

        self.CUSTOMER_URL = get_urls(sandbox)['CUSTOMER_URL']
        self.CREDIT_CARD_URL = get_urls(sandbox)['CREDIT_CARD_URL']
        self.ORDER_URL = get_urls(sandbox)['ORDER_URL']
        self.TRANSACTION_URL = get_urls(sandbox)['TRANSACTION_URL']

    def auth_header(self):
        return {'Authorization': str(b64encode(b'{}:{}'.format(self.token, self.key)))}

    def get(self, url):
        return requests.get(url, headers=self.auth_header())

    def post(self, url, data=None):
        return requests.post(url, json=data, headers=self.auth_header())

    def delete(self, url):
        return requests.delete(url, headers=self.auth_header())

    def list_customer(self):
        return self.get(self.CUSTOMER_URL).json()

    def create_customer(self, customer):
        return self.post(self.CUSTOMER_URL, customer.to_dict()).json()

    def get_customer(self, customer_id):
        return self.get(self.CUSTOMER_URL+'/'+customer_id).json()
    
    def create_customer_credit_card(self, customer_id, credit_card):
        return self.post(
            self.CUSTOMER_URL+'/'+customer_id+'/fundinginstruments', WirecardFundingInstrument(credit_card=credit_card).to_dict()
        ).json()

    def delete_credit_card(self, credit_card_id):
        try:
            return self.delete(self.CREDIT_CARD_URL+'/'+credit_card_id).json()
        except JSONDecodeError:
            return {'error': None}

    def list_order(self):
        return self.get(self.ORDER_URL).json()

    def create_order(self, order):
        return self.post(self.ORDER_URL, order.to_dict()).json()

    def get_order(self, order_id):
        return self.get(self.ORDER_URL+'/'+order_id).json()

    def create_transaction(self, order_id, transaction):
        return self.post(self.ORDER_URL+'/'+order_id+'/payments', transaction.to_dict()).json()

    def get_transaction(self, transaction_id):
        return self.get(self.TRANSACTION_URL+'/'+transaction_id).json()
        
class WirecardMarketPlace(Wirecard):

    def __init__(self, access_token, sandbox=False):
        super().__init__(None, None, sandbox)

        self.access_token = access_token
        self.TOKEN_URL = get_urls(sandbox)['TOKEN_URL']

    def auth_header(self):
        return {'Authorization': 'Bearer '+self.access_token}

    def get_oauth_token(self, client_id, client_secret, code=None, redirect_uri=None, grant_type='authorization_code'):
        parameters = '?client_id={}&client_secret={}&grant_type={}'.format(client_id, client_secret, grant_type)

        if code:
            parameters += '&code={}'.format(code)
        
        if redirect_uri:
            parameters += '&redirect_uri={}'.format(redirect_uri)

        return self.post(self.TOKEN_URL+parameters).json()
