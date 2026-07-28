from interface.terminal import Terminal
from interface.main_menus.inventory_menu import InventoryMenu

class MainMenu:

  def __init__(self):
    self._product_menu = InventoryMenu()  
      
  def run(self) -> None:
    
    while True:
      
      Terminal.header("Menu Principal - SGEC")
      
      print('1 - Inventário')
      print('2 - PDF (Em desenvolvimento)')
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