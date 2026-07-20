from repository.inventory.category_repository import CategoryRepository
from domain.inventory.category import Category

class CategoryService:
  def __init__(self):
    self._category_repository = CategoryRepository()
    
  def create_category(self,
                      name:str) -> Category:
    
    category = Category(name)
    
    self._category_repository.save(category)
    
    return category
  
  def list_category(self):
    
    categories = self._category_repository.reconstruct()
    
    return categories