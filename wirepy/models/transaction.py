from .credit_card import WirecardCreditCard
from .boleto import WirecardBoleto

from .misc import (
    WirecardGeneric,
    WirecardDocument,
    WirecardPhone,
    WirecardAddress,
    WirecardMoipAccount,
    WirecardFundingInstrument
)

from ..settings import FundingInstrumentMethod

class WirecardTransaction(WirecardGeneric):

    def __init__(self,
                method=FundingInstrumentMethod.BOLETO,
                statement_descriptor='Loja Online',
                installment_count=1,
                delay_capture=False):

        self.installment_count = installment_count
        self.statement_descriptor = statement_descriptor
        self.funding_instrument = WirecardFundingInstrument(method=method)

    def set_credit_card(self, _id=None, cvc=None):
        self.funding_instrument.set_credit_card(
            WirecardCreditCard(_id=_id, cvc=cvc))
    
    def set_boleto(self, expiration_date=None, logo_uri=None,
                    instruction_line_1=None, instruction_line_2=None, instruction_line_3=None):
        self.funding_instrument.set_boleto(
            WirecardBoleto(expiration_date, logo_uri,
                instruction_line_1, instruction_line_2, instruction_line_3))
