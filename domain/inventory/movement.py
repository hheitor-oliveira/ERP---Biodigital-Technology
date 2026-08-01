# lib's imports
from datetime import datetime

# internal imports
from domain.enums.movement_type import MovementType
from domain.users.system_user import SystemUser
from domain.inventory.movement_item import MovementItem


class Movement:
    """
    Classe principal responsável por representar o registro de uma movimentação de produtos realizada no sistema.
    """
    def __init__(self,
                 id: int,
                 items: list[MovementItem],
                 user: SystemUser,
                 movement_type: MovementType,
                 movement_date: datetime
                 ):
    
        self._movement_id = id
        self._items = items
        self._user = user
        self._movement_type = movement_type
        self._movement_date = movement_date
