# internal import's
from interface.terminal import Terminal
from services.inventory.category_service import CategoryService
from decimal import InvalidOperation

class CreateMenu:
  
  def __init__(self) -> None:
    self._category_service = CategoryService()
    
     
  def main_create_menu(self):
    
      while True:
        Terminal.header('Cadastro | Inventário | ERP-Biodigital')
        print('1 - Cadastrar Produto')
        print('2 - Cadastrar Categoria')
        print('3 - Sair')
        Terminal.separator()
        try:
          
          option = Terminal.ask_int('Digite a opção desejada')
          Terminal.separator()
    
          if option == 1:
            self.create_product_screen()
          elif option == 2:
            self.create_category_screen()
          elif option == 3:
            break
          else:
            Terminal.error('Insira uma opção válida e tente novamente.')
            Terminal.pause()
            Terminal.clear()
            continue
          
        except ValueError:
          Terminal.error('Insira uma opção válida e tente novamente.')
          Terminal.pause()
          Terminal.clear()
          continue
  
  def create_product_screen(self) -> None:
    '''Interface de criação de um produto no terminal.'''
    name = None
    selected_category = None
    cost_price = None
    sale_value = None
    
    while True:
      Terminal.clear()

      Terminal.header('Cadastro de Produto - SGEC')
      
      print('1 - Nome:', name.capitalize()) if name else print('1 - Nome: Não informado')
      print('2 - Categoria:', selected_category.name.capitalize()) if selected_category else print('2 - Categoria: Não selecionado')
      print(f'3 - Preço de custo:, {cost_price:,.2f}') if cost_price else print('3 - Preço de custo: Não informado')
      print(f'4 - Valor de venda:, {sale_value:,.2f}') if sale_value else print('4 - Valor de venda: Não informado')
      Terminal.separator()
      print('5 - Finalizar cadastro')

      Terminal.separator()

      option = Terminal.ask_int('Escolha um campo')

      if option == 1:
        name_validation = Terminal.ask('Nome')
        if name_validation.isalpha() == False or 2 < len(name_validation) < 64:
          Terminal.error('Valor inválido inserido. O nome só pode conter letras')
        else:
          name = name_validation

      elif option == 2:
        Terminal.clear()
        categories = (self._category_service.list_category())
        Terminal.header('Lista de Categorias | ERP-Biodigital')
        for x, category in enumerate(categories, start=1):
          print(f'{x} - {category.name}')
        Terminal.separator()
        try:
          category = Terminal.ask_int('Digite o número correspondente')
          selected_category = categories[category - 1]
        except ValueError or IndexError:
          print('Entrada inválida. Insira uma entrada válida e tente novamente!')
          continue
        
      elif option == 3:
        try:
          cost_price = Terminal.ask('Preço de custo')
        except InvalidOperation:
          Terminal.error('Entrada inválida. Digite apenas números nesse campo.')
          
      elif option == 4:
        try:
          sale_value = Terminal.ask('Valor de venda')
        except InvalidOperation:
          Terminal.error('Entrada inválida. Digite apenas números nesse campo.')
      
      elif option == 5:
        pass
            
  def create_category_screen(self) -> None:
    
    name = None
    
    while True:

      Terminal.header('Criação de Categoria | ERP-Biodigital')
      print(f'1 - Nome: {name.capitalize()}') if name is not None else print('1 - Nome: Não digitado')
      print(f'2 - Criar')
      print(f'3 - Cancelar')
      Terminal.separator()
      
      option = Terminal.ask_int('Escolha a ação desejada')
      
      try:
        if option == 1:
          name_entry = Terminal.ask('Nome')
          if name_entry.isalpha() == False or len(name_entry) < 2 or len(name_entry) > 32:
            Terminal.error('O nome da categoria só pode conter letras.)')
            print('(2 - 32 caracteres.)')
            Terminal.pause()
            Terminal.clear()
            continue
          else:
            name = name_entry
            Terminal.success('Nome atribuído com sucesso!')
            Terminal.pause()
            Terminal.clear()
            continue
      
        elif option == 2:
          if name is None:
            Terminal.error('Necessário atribuir um nome a categoria para criar.')
            Terminal.pause()
            Terminal.clear()
            continue
          else:
            self._category_service.create_category(name.upper())
            Terminal.success('Categoria cadastrada com sucesso!')
            Terminal.pause()
            Terminal.clear()
            break
          
        elif option == 3:
          break
        
        else: 
          Terminal.error('Insira um valor válido.')
          Terminal.pause()
          Terminal.clear()
          continue
        
      except ValueError:
        Terminal.error('Insira um valor válido.')
        Terminal.pause()
        Terminal.clear()
        