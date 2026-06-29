from .product import Product

class MovementItem:
  def __init__(self,
               product: Product,
               quantity
               ) -> None:
    
    self.product = product
    self.quantity = quantity