# lib's import's

# internal import's
from interface.terminal import Terminal
from domain.enums.product_categorys import Category
from services.product_service import ProductService

class ProductMenu:
  
  def __init__(self):
    self._product_service = ProductService()
  
  def run(self):
    
    while True:
      Terminal.header('Menu Produtos - SGEC')
      
      print('1 - Cadastrar Produto')
      print('2 - Remover Produto')
      print('3 - Editar Produto')
      print('4 - Dar entrada em Produto')
      print('5 - Dar saída em Produto')
      print('6 - Sair')
      
      Terminal.separator()
      
      user_choice = Terminal.ask_int('Escolha a opção desejada')
      
      if user_choice == 1:
        self.show_create_product_screen()
      elif user_choice == 2:
        input()
        Terminal.clear()
        break
      elif user_choice == 3:
        input()
        Terminal.clear()
        break
      elif user_choice == 4:
        input()
        Terminal.clear()
        break
      elif user_choice == 5:
        input()
        Terminal.clear()
        break
      elif user_choice == 6:
        break
  
  def show_create_product_screen(self):
    
    name = None
    selected_category = None
    cost_price = None
    sale_value = None
    
    while True:
      Terminal.clear()

      Terminal.header('Cadastro de Produto - SGEC')
      
      print('1 - Nome:', name) if name else print('1 - Nome: Não informado')
      print('2 - Categoria:', selected_category.value) if selected_category else print('2 - Categoria: Não selecionado')
      print('3 - Preço de custo:', cost_price) if cost_price else print('3 - Preço de custo: Não informado')
      print('4 - Valor de venda:', sale_value) if sale_value else print('4 - Valor de venda: Não informado')
      Terminal.separator()
      print('5 - Finalizar cadastro')

      Terminal.separator()

      option = Terminal.ask_int('Escolha um campo: ')

      if option == 1:
        name = Terminal.ask('Nome')

      elif option == 2:
        for index, item in enumerate(Category, start=1):
          print(f'{index} - {item.value}')
          
        option = Terminal.ask_int('Seleciona uma das categorias acima')  
        categories_list = list(Category)
        selected_category = categories_list[option - 1]
        
      elif option == 3:
        cost_price = Terminal.ask_decimal('Preço de custo')

      elif option == 4:
        sale_value = Terminal.ask_decimal('Preço de Venda')
      
      elif option == 5:
        if name and selected_category and cost_price and sale_value != None:
          self._product_service.create_product(name, selected_category, cost_price, sale_value)
          Terminal.success('Produto cadastrado com sucesso!')
          Terminal.pause()
          break
        else:
          Terminal.error('Preencha todos os campos antes de continuar!')
          Terminal.pause()
          continue