from interface.terminal import Terminal
from services.inventory.product_service import ProductService

class ConsultMenu:
  
  def __init__(self) -> None:
    self._product_service = ProductService()
  
  def run(self) -> None:
   
   while True:
      
      Terminal.header('Estoque | Inventário | ERP-Biodigital 2026 ')
      print('1 - Listar Produtos')
      print('2 - Desenvolvendo')
      print('3 - Sair')
      Terminal.separator()
      option = Terminal.ask_int('Digite a opção desejada')
      
      if option == 1:
        products = self._product_service.list_products()
        
        for x, product in enumerate(products, start=1):
          print(f'{x} - {product.name.title()} | {product.sale_value}')
        Terminal.pause()
        
      elif option == 2:
        pass
      elif option == 3:
        break