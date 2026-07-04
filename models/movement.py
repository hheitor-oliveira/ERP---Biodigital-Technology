from user import User
from movement_item import MovementItem

class Movement:
    def __init__(self,
                 id: int,
                 movement_item: MovementItem,
                 user_id: User,
                 type: int,
                 date
                 ):
        self.movement_id = id
        self.movement_item = movement_item
        self.user_id = user_id
        self.type = type
        self.date = date
