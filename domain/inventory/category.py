from typing import Self

class Category:
  def __init__(self,
               name: str,
               id: None | int = None):
    self._id = id
    self._name = name
    
  @property
  def category_name(self) -> str:
    return self._name
  
  @property
  def category_id(self) -> None | int:
    return self._id
  
  @classmethod
  def restore(cls,
              name: str,
              id: int | None) -> Self:
    
    category = object.__new__(cls)
    
    category._name = name
    category._id = id
    
    return category