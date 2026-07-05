from user import User
from sale_item import SaleItem
from models.sale_payment import SalePayment

class Sale:
    def __init__(self,
                 id: int,
                 sale_item: SaleItem,
                 sale_payment: SalePayment,
                 user_id: User,
                 total_value: float,
                 discount: int,
                 date):
        self.id = id
        self.sale_item = sale_item
        self.sale_payment = sale_payment
        self.user_id = user_id
        self.total_value = total_value
        self.discount = discount
        self.date = date
        