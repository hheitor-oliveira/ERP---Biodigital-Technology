from payment_method import PaymentMethod

class Payment:
  def __init__(self,
               id,
               method: PaymentMethod,
               value) -> None:
    
    self.id = id
    self.method = method
    self.value = value