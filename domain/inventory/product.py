# lib's imports
from decimal import Decimal

# internal import's
from domain.enums.product_status import ProductStatus
from domain.enums.product_categorys import Category

class Product:
    """
    A classe Product representa um produto do sistema e é responsável por proteger as regras relacionadas ao seu estoque, preços e estado.
    """
    def __init__(self,
                 name: str,
                 category: Category,
                 cost_price: Decimal,
                 sale_value: Decimal,
                 stock_quantity: int = 0,
                 product_status: ProductStatus = ProductStatus.ACTIVE,
                 id: int | None = None
                 ):
    
        self._id = id
        self._name = name
        self._category = category
        self._stock_quantity = stock_quantity
        self._sale_value = sale_value
        self._cost_price = cost_price
        self._status = product_status

    def add_stock(self, 
                  quantity: int) -> None:
        self._stock_quantity += quantity
    
    def remove_stock(self,
                     quantity: int) -> None:
        self._stock_quantity -= quantity
    
    def change_name(self,
                    new_name: str) -> None:
        self._name = new_name
        
    def change_sale_value(self,
                          new_sale_value: Decimal) -> None:
        self._sale_value = new_sale_value
        
    def change_cost_price(self,
                          new_cost_price: Decimal) -> None:
        self._cost_price = new_cost_price
        
    def change_status(self,
                          new_status: ProductStatus) -> None:
        self._status = new_status
        
    def change_category(self,
                        new_category: Category):
        self._category = new_category
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def category(self) -> Category:
        return self._category
    
    @property
    def cost_price(self) -> Decimal:
        return self._cost_price
    
    @property
    def sale_value(self) -> Decimal:
        return self._sale_value
    
    @property
    def stock_quantity(self) -> int:
        return self._stock_quantity
    
    @property
    def status(self) -> ProductStatus:
        return self._status