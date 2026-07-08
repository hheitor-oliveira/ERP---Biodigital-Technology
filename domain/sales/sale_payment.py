from domain.sales.payment_method import PaymentMethod
from decimal import Decimal

class SalePayment:
    def __init__(self,
                 id: int,
                 payment_method: PaymentMethod,
                 payment_value: Decimal):
        
        self.id = id
        self.payment_method = payment_method
        self.payment_value = payment_value