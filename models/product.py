class Product:
  def __init__(self, 
               id, 
               name, 
               price_buy, 
               price_sell, 
               category,
               quantity):
    
    self.id = id
    self.name = name
    self.price_buy = price_buy
    self.price_sell = price_sell
    self.category = category
    self.quantity = quantity
    
    