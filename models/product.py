class Product:
    def __init__(self,
                 id: int,
                 name: str,
                 category: str,
                 quantity: int,
                 value: float,
                 buy_price: float
                 ):
        self.id = id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.value = value
        self.buy_price = buy_price
        
