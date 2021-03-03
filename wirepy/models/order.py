from .credit_card import WirecardCreditCard

from .misc import (
    WirecardGeneric,
    WirecardDocument,
    WirecardPhone,
    WirecardAddress,
    WirecardMoipAccount
)

from ..settings import ReceiverType

class WirecardOrderReceiverAmount(WirecardGeneric):
    
    def __init__(self, percentual=None, fixed=None):
        if fixed:
            self.fixed = int(float(fixed)*100)
        
        if percentual:
            self.percentual = int(percentual)
    
    def set_moip_account(self, moip_account_id, moip_account=None):
        if not moip_account:
            moip_account = WirecardMoipAccount(moip_account_id)
        self.moip_account = moip_account

class WirecardOrderReceiver(WirecardGeneric):
    
    def __init__(self, _type, moip_account_id=None, amount_percentual=None, amount_fixed=None, fee_payor=True):
        self._type = _type
        self.fee_payor = fee_payor

        if moip_account_id:
            self.moip_account = WirecardMoipAccount(moip_account_id)
        
        if amount_fixed or amount_percentual:
            self.amount = WirecardOrderReceiverAmount(amount_percentual, amount_fixed)
    
    def set_moip_account(self, moip_account_id, moip_account=None):
        if not moip_account:
            moip_account = WirecardMoipAccount(moip_account_id)
        self.moip_account = moip_account

class WirecardOrderItem(WirecardGeneric):

    def __init__(self, name, quantity, price, detail=None, category=None):
        self.product = name
        self.quantity = int(quantity)
        self.price = int(float(price or 0)*100)
        self.detail = detail
        self.category = category
    
class WirecardOrderCustomer(WirecardGeneric):

    def __init__(self, _id):
        self._id = _id

class WirecardOrderSubtotals(WirecardGeneric):

    def __init__(self, shipping=0, addition=0, discount=0):
        self.shipping = int(float(shipping or 0)*100)
        self.addition = int(float(addition or 0)*100)
        self.discount = int(float(discount or 0)*100)

class WirecardOrderAmount(WirecardGeneric):
    def __init__(self, shipping=0, addition=0, discount=0, currency='BRL'):
        self.currency = currency

        if shipping or addition or discount:
            self.subtotals = WirecardOrderSubtotals(shipping, addition, discount)

    def set_subtotals(self, shipping=0, addition=0, discount=0, subtotals=None):
        if not subtotals:
            subtotals = WirecardOrderSubtotals(shipping, addition, discount)
        self.subtotals = subtotals

class WirecardOrder(WirecardGeneric):

    def __init__(self, own_id, customer_id=None, shipping_amount=None, addition_amount=None, discount_amount=None):
        self.own_id = own_id

        self.items = []
        self.receivers = []

        if customer_id:
            self.customer = WirecardOrderCustomer(customer_id)

        if shipping_amount or addition_amount or discount_amount:
            self.amount = WirecardOrderAmount(shipping_amount, addition_amount, discount_amount)

    def set_amount(self, shipping=0, addition=0, discount=0, currency='BRL', amount=None):
        if not amount:
            amount = WirecardOrderAmount(shipping, addition, discount, currency)
        self.amount = amount

    def set_customer(self, customer_id=None, customer=None):
        if not customer:
            customer = WirecardOrderCustomer(customer_id)
        self.customer = customer

    def add_item(self, name, quantity, price, detail=None, category=None, item=None):
        if not item:
            item = WirecardOrderItem(name, quantity, price, detail, category)
        self.items.append(item)

    def set_primary_receiver(self, moip_account_id=None, amount_percentual=100,
                                amount_fixed=None, fee_payor=True, receiver=None):
        if not receiver:
            receiver = WirecardOrderReceiver(
                ReceiverType.PRIMARY, moip_account_id, amount_percentual, amount_fixed, fee_payor)
        self.receivers.append(receiver)

    def add_secondary_receiver(self, moip_account_id=None, amount_percentual=None,
                                amount_fixed=None, fee_payor=False, receiver=None):
        if not receiver:
            receiver = WirecardOrderReceiver(
                ReceiverType.SECONDARY, moip_account_id, amount_percentual, amount_fixed, fee_payor)
        self.receivers.append(receiver)
