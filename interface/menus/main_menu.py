from interface.terminal import Terminal
from interface.menus.product_menu import ProductMenu

class MainMenu:

  def __init__(self):
    self._product_menu = ProductMenu()  
      
  def run(self) -> None:
    
    while True:
      
      Terminal.header("Menu Principal - SGEC")
      
      print('1 - Produtos')
      print('2 - Vendas (Em desenvolvimento)')
      print('3 - Sair')
      
      Terminal.separator()
      
      user_choice = Terminal.ask_int('Escolha a opção desejada')
      
      if user_choice == 1:
        self._product_menu.run()
        
      elif user_choice == 2:
        print('Em desenvolvimento, clique qualquer tecla para continuar.')
        input()
        Terminal.clear()
        continue
      
      elif user_choice == 3:
        break