# lib's import's
from decimal import Decimal

# internal import's
from domain.inventory.product import Product
from domain.enums.product_categorys import Category
from repository.product_repository import ProductRepository

class ProductService:
  """Responsável por coordenar todos os processos relacionados a produtos do sistema."""
  
  def __init__(self):
    self._product_repository = ProductRepository()
  
  def create_product(self, 
                     name: str,
                     category: Category,
                     cost_price: Decimal,
                     sale_value: Decimal) -> Product:
    
    product = Product(name, category, cost_price, sale_value)
    
    self._product_repository.save(product)
    
    return product