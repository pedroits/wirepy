from .credit_card import WirecardCreditCard

from .misc import (
    WirecardGeneric,
    WirecardDocument,
    WirecardPhone,
    WirecardAddress,
    WirecardFundingInstrument
)

class WirecardCustomer(WirecardGeneric):

    def __init__(self, own_id, fullname, email, birth_date=None, _id=None):
        self._id = _id
        self.own_id = own_id
        self.fullname = fullname
        self.email = email
        self.birth_date = birth_date

    def set_tax_document(self, _type=None, number=None, wirecard_document=None):
        if not wirecard_document:
            wirecard_document = WirecardDocument(_type, number)
        self.tax_document = wirecard_document

    def set_phone(self, area_code=None, number=None, country_code='55', wirecard_phone=None):
        if not wirecard_phone:
            wirecard_phone = WirecardPhone(area_code, number, country_code)
        self.phone = wirecard_phone

    def set_shipping_address(self, street=None, street_number=None,
                                district=None, zip_code=None, city=None,
                                state=None, country='BRA', wirecard_address=None):
        if not wirecard_address:
            wirecard_address = WirecardAddress(
                street, street_number, district, zip_code, city, state, country)
        self.shipping_address = wirecard_address
