from user import User
from movement_item import MovementItem
from datetime import datetime

class Movement:
    def __init__(self,
                 id: int,
                 items: list[MovementItem],
                 user: User,
                 type: int,
                 date: datetime
                 ):
        self.movement_id = id
        self.items = items
        self.user_id = user_id
        self.type = type
        self.date = date
