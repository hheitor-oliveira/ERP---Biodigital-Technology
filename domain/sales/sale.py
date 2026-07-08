from datetime import datetime
from domain.users.system_user import SystemUser
from domain.sales.sale_item import SaleItem
from domain.sales.sale_payment import SalePayment

class Sale:
    def __init__(self,
                 sale_id: int,
                 sale_item: list[SaleItem],
                 sale_payment: list[SalePayment],
                 users: SystemUser,
                 total_value: float,
                 sale_discount: int,
                 sale_date: datetime):

        self.sale_id = sale_id
        self.sale_item = sale_item
        self.sale_payment = sale_payment
        self.users = users
        self.total_value = total_value
        self.sale_discount = sale_discount
        self.sale_date = sale_date
        