from product import Product

class MovementItem:
  def __init__(self,
               id: int,
               product_name: Product,
               quantity: int
               ):
    self.id = id
    self.product_name = product
    self.quantity = quantity