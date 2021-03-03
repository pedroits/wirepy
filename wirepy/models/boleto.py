from .misc import (
    WirecardGeneric,
)

class WirecardBoletoInstrutions(WirecardGeneric):

    def __init__(self, first=None, second=None, third=None):
        if first:
            self.first = first
        if second:
            self.second = second
        if third:
            self.third = third

class WirecardBoleto(WirecardGeneric):

    def __init__(self, expiration_date=None, logo_uri=None,
                    instruction_line_1=None, instruction_line_2=None, instruction_line_3=None):

        self.expiration_date = expiration_date

        if logo_uri:
            self.logo_uri = logo_uri

        if instruction_line_1 or instruction_line_2 or instruction_line_3:
            self.instruction_lines = WirecardBoletoInstrutions(
                instruction_line_1, instruction_line_2, instruction_line_3)
    
    def set_logo_uri(self, logo_uri):
        self.logo_uri = logo_uri
    
    def set_instructions(self, line1, line2=None, line3=None):
        self.instruction_lines = WirecardBoletoInstrutions(line1, line2, line3)
