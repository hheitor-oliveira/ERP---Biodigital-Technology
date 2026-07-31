# internal import's
from interface.terminal import Terminal
from services.inventory.category_service import CategoryService
from services.inventory.product_service import ProductService
from decimal import InvalidOperation

class CreateMenu:
  
  def __init__(self) -> None:
    self._category_service = CategoryService()
    self._product_service = ProductService()
    
     
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
      
      print(f'1 - Nome: {name.title()}') if name is not None else print('1 - Nome: Não informado')
      print(f'2 - Categoria: {selected_category.name.capitalize()}') if selected_category is not None else print('2 - Categoria: Não selecionado')
      print(f'3 - Preço de custo: R${cost_price:,.2f}') if cost_price is not None else print('3 - Preço de custo: Não informado')
      print(f'4 - Valor de venda: R${sale_value:,.2f}') if sale_value is not None else print('4 - Valor de venda: Não informado')
      Terminal.separator()
      print('5 - Cadastrar Produto')
      print('6 - Cancelar Cadastro')

      Terminal.separator()

      option = Terminal.ask_int('Escolha um campo')

      if option == 1:
        name_entry = Terminal.ask('Nome')
        name_validation = name_entry
        name_validation = name_validation.replace(' ','')
        if name_validation.isalnum() == False or len(name_validation) <= 2 or len(name_validation) >= 64:
          Terminal.error('O nome só pode conter entre 2 e 64 caracteres.')
          Terminal.pause()
        else:
          name = name_entry

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
          cost_price = Terminal.ask_decimal('Preço de custo')
        except InvalidOperation:
          Terminal.error('Entrada inválida. Digite apenas números nesse campo.')
          
      elif option == 4:
        try:
          sale_value = Terminal.ask_decimal('Valor de venda')
        except InvalidOperation:
          Terminal.error('Entrada inválida. Digite apenas números nesse campo.')
      
      elif option == 5:
        if name is not None and selected_category is not None and cost_price is not None and sale_value is not None:
          self._product_service.create_product(name, selected_category, cost_price, sale_value)
          Terminal.success('Produto cadastrado com sucesso!')
          Terminal.pause()
          Terminal.clear()
          break
        else:
          Terminal.error('Ainda existem campos vazios, preencha todos para criar.')
          Terminal.pause()
          Terminal.clear()
          continue

      elif option == 6:
        break
            
  def create_category_screen(self) -> None:
    
    name = None
    
    while True:

      Terminal.header('Criação de Categoria | ERP-Biodigital')
      print(f'1 - Nome: {name.title()}') if name is not None else print('1 - Nome: Não digitado')
      print(f'2 - Cadastrar Categoria')
      print(f'3 - Cancelar')
      Terminal.separator()
      
      option = Terminal.ask_int('Escolha a ação desejada')
      
      try:
        if option == 1:
          name_entry = Terminal.ask('Nome')
          name_validation = name_entry.replace(' ','').strip('')
          if name_validation.isalpha() == False or len(name_validation) < 2 or len(name_validation) > 32:
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
        