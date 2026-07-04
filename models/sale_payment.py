from payment_method import PaymentMethod

class SalePayment:
    def __init__(self,
                 id: int,
                 payment_method: PaymentMethod,
                 value: float):
        self.id = id
        self.payment_method = payment_method
        self.value = value