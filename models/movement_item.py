from product import Product

class MovementItem:
  def __init__(self,
               id: int,
               product: Product,
               quantity: int
               ):
    self.id = id
    self.product = product
    self.quantity = quantity