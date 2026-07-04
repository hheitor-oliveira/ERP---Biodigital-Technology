class PaymentMethod:
  def __init__(self,
               id: int,
               name: str,
               active: bool
               ) -> None:
    self.id = id
    self.name = name
    self.active = active