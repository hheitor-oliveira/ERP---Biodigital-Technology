from .user import User
from .sale_item import SaleItem
from .payment import Payment

class Sale:
  def __init__(self,
               id,
               user: User,
               items: list[SaleItem],
               payment_methods: list[Payment],
               date,
               total_value
               ) -> None:
    
    self.id = id
    self.user = user
    self.items = items
    self.payment_methods = payment_methods
    self.date = date
    self.total_value = total_value