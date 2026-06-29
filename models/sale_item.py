from .product import Product

class SaleItem:
  def __init__(self,
               product: Product,
               quantity,
               unitary_value
               ) -> None:
    
    self.product = product
    self.quantity = quantity
    self.unitary_value = unitary_value