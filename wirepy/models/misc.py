import simplejson as json
from enum import Enum
from datetime import datetime

from ..utils import snake_to_camel_case
from ..settings import FundingInstrumentMethod

class WirecardGeneric(object):

    def to_dict(self):
        return self.transform_object(self.__dict__)

    def transform_dict(self, object_dict):
        return dict([(snake_to_camel_case(k), v) for k, v in object_dict.items()])

    def transform_object(self, object_dict):
        new_dict = self.transform_dict(object_dict)

        for key, value in new_dict.items():
            if isinstance(value, WirecardGeneric):
                new_dict[key] = value.to_dict()
            elif isinstance(value, dict):
                new_dict[key] = self.transform_dict(value)
            elif isinstance(value, list):
                new_dict[key] = [v.to_dict() for v in value]
            elif isinstance(value, datetime):
                new_dict[key] = value.strftime('%Y-%m-%d')
            elif isinstance(value, Enum):
                new_dict[key] = value.value

        return new_dict

class WirecardFundingInstrument(WirecardGeneric):
    
    def __init__(self, credit_card=None, boleto=None, method=FundingInstrumentMethod.CREDIT_CARD):
        self.method = method

        if method == FundingInstrumentMethod.CREDIT_CARD:
            self.credit_card = credit_card
        
        if method == FundingInstrumentMethod.BOLETO:
            self.boleto = boleto
    
    def set_boleto(self, boleto):
        self.boleto = boleto

    def set_credit_card(self, credit_card):
        self.credit_card = credit_card

class WirecardMoipAccount(WirecardGeneric):
    
    def __init__(self, _id):
        self._id = _id

class WirecardAddress(WirecardGeneric):

    def __init__(self, street, street_number, district, zip_code, city, state, country='BRA'):
        self.street = street
        self.street_number = street_number
        self.district = district
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.country = country

class WirecardPhone(WirecardGeneric):

    def __init__(self, area_code, number, country_code='55'):
        self.area_code = area_code
        self.number = number

class WirecardDocument(WirecardGeneric):

    def __init__(self, _type, number):
        self._type = _type
        self.number = number