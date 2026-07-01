from .user import User
from .movement_item import MovementItem

class Movement:
  def __init__(self,
               movement_items: MovementItem,
               user: User,
               id,
               type
               ) -> None:
    
    self.movement_items = movement_items
    self.user = user
    self.id = id
    self.type = type