from .misc import (
    WirecardGeneric,
    WirecardDocument,
    WirecardPhone,
    WirecardAddress
)

class WirecardCreditCardHolder(WirecardGeneric):

    def __init__(self, fullname, birthdate=None):
        self.fullname = fullname
        self.birthdate = birthdate
    
    def set_tax_document(self, _type=None, number=None, document=None):
        if not document:
            document = WirecardDocument(_type, number)
        self.tax_document = document

    def set_billing_address(self, street=None, street_number=None,
                            district=None, zip_code=None, city=None,
                            state=None, country='BRA', address=None):
        if not address:
            address = WirecardAddress(street, street_number, district, zip_code, city, state, country)
        self.billing_address = address

    def set_phone(self, area_code=None, number=None, country_code='55', phone=None):
        if not phone:
            phone = WirecardPhone(area_code, number, country_code)
        self.phone = phone

class WirecardCreditCard(WirecardGeneric):

    def __init__(self, number=None, expiration_month=None, expiration_year=None, cvc=None, _id=None):
        self._id = _id
        self.number = number
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.cvc = cvc

    def set_holder(self, fullname=None, birthdate=None, holder=None):
        if not holder:
            holder = WirecardCreditCardHolder(fullname, birthdate)
        self.holder = holder
    
    def set_holder_tax_document(self, _type=None, number=None, document=None):
        self.holder.set_tax_document(_type, number, document)

    def set_holder_billing_address(self, street=None, street_number=None,
                            district=None, zip_code=None, city=None,
                            state=None, country='BRA', address=None):
        self.holder.set_billing_address(street, street_number, district, zip_code, city, state, country, address)

    def set_holder_phone(self, area_code=None, number=None, country_code='55', phone=None):
        self.holder.set_phone(area_code, number, country_code, phone)
