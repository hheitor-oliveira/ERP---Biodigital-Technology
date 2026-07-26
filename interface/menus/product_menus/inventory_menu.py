# lib's import's

# interface import's
from interface.terminal import Terminal
from interface.menus.product_menus.create_menus import CreateMenu

# internal import's

class InventoryMenu:
  
  def __init__(self):
    self.create_menus = CreateMenu()
    pass
  
  def run(self):
    
    while True:
      
      Terminal.header('Menu Inventário | ERP-Biodigital')
      
      print('1 - Cadastros')
      print('2 - Consultas')
      print('3 - Edições')
      print('4 - Entrada/Saída')
      print('5 - Sair')
      
      Terminal.separator()
      
      user_choice = Terminal.ask_int('Escolha a opção desejada')
      
      if user_choice == 1:
        self.create_menus.main_create_menu()
        
      elif user_choice == 2:
        print('Funcionalidade em desenvolvimento.')
        Terminal.pause()
        continue
      
      elif user_choice == 3:
        continue
      
      elif user_choice == 4:
        print('Funcionalidade em desenvolvimento.')
        Terminal.pause()
        Terminal.clear()
        break
      
      elif user_choice == 5:
        print('Funcionalidade em desenvolvimento.')
        Terminal.pause()
        Terminal.clear()
        break
    
  
  