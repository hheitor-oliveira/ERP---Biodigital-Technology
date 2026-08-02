from interface.core.terminal import Terminal
from services.inventory.category_service import CategoryService
from services.inventory.product_service import ProductService


class CreateMenu:
    def __init__(self) -> None:
        self._category_service = CategoryService()
        self._product_service = ProductService()

    def main_create_menu(self):
        while True:
            Terminal.header("Inventário", "Cadastros")
            Terminal.options(
                [
                    "Cadastrar produto",
                    "Cadastrar categoria",
                    "Voltar",
                ]
            )
            Terminal.separator()

            option = Terminal.ask_option("Digite a opção desejada", range(1, 4))

            if option == 1:
                self.create_product_screen()
            elif option == 2:
                self.create_category_screen()
            elif option == 3:
                break

    def create_product_screen(self) -> None:
        """Interface de criação de um produto no terminal."""
        name = None
        selected_category = None
        cost_price = None
        sale_value = None

        while True:
            Terminal.header("Cadastro de produto", "Inventário")

            Terminal.field(1, "Nome", name.title() if name else None)
            Terminal.field(
                2,
                "Categoria",
                selected_category.name.capitalize() if selected_category else None,
            )
            Terminal.field(3, "Preço de custo", Terminal.money(cost_price))
            Terminal.field(4, "Valor de venda", Terminal.money(sale_value))
            Terminal.separator()
            Terminal.option(5, "Cadastrar produto")
            Terminal.option(6, "Cancelar cadastro")
            Terminal.separator()

            option = Terminal.ask_option("Escolha um campo", range(1, 7))

            if option == 1:
                name_entry = Terminal.ask("Nome")
                name_validation = name_entry.replace(" ", "")
                if (
                    name_validation.isalnum() is False
                    or len(name_validation) <= 2
                    or len(name_validation) >= 64
                ):
                    Terminal.error("O nome deve conter entre 3 e 63 caracteres.")
                    Terminal.pause()
                else:
                    name = name_entry

            elif option == 2:
                selected_category = self._select_category()

            elif option == 3:
                cost_price = Terminal.ask_decimal("Preço de custo")

            elif option == 4:
                sale_value = Terminal.ask_decimal("Valor de venda")

            elif option == 5:
                if (
                    name is not None
                    and selected_category is not None
                    and cost_price is not None
                    and sale_value is not None
                ):
                    self._product_service.create_product(
                        name, selected_category, cost_price, sale_value
                    )
                    Terminal.success("Produto cadastrado com sucesso!")
                    Terminal.pause()
                    break

                Terminal.error("Ainda existem campos vazios, preencha todos para criar.")
                Terminal.pause()

            elif option == 6:
                break

    def create_category_screen(self) -> None:
        name = None

        while True:
            Terminal.header("Criação de categoria", "Inventário")
            Terminal.field(1, "Nome", name.title() if name else None)
            Terminal.separator()
            Terminal.option(2, "Cadastrar categoria")
            Terminal.option(3, "Cancelar")
            Terminal.separator()

            option = Terminal.ask_option("Escolha a ação desejada", range(1, 4))

            if option == 1:
                name_entry = Terminal.ask("Nome")
                name_validation = name_entry.replace(" ", "").strip()
                if (
                    name_validation.isalpha() is False
                    or len(name_validation) < 2
                    or len(name_validation) > 32
                ):
                    Terminal.error("O nome da categoria só pode conter letras.")
                    print("(2 - 32 caracteres.)")
                    Terminal.pause()
                    continue

                name = name_entry
                Terminal.success("Nome atribuído com sucesso!")
                Terminal.pause()

            elif option == 2:
                if name is None:
                    Terminal.error("Necessário atribuir um nome à categoria para criar.")
                    Terminal.pause()
                    continue

                self._category_service.create_category(name.upper())
                Terminal.success("Categoria cadastrada com sucesso!")
                Terminal.pause()
                break

            elif option == 3:
                break

    def _select_category(self):
        categories = self._category_service.list_category()

        Terminal.header("Lista de categorias", "Selecione uma categoria")

        if not categories:
            Terminal.empty("Nenhuma categoria cadastrada.")
            Terminal.pause()
            return None

        for number, category in enumerate(categories, start=1):
            Terminal.option(number, category.name)

        Terminal.separator()
        option = Terminal.ask_option(
            "Digite o número correspondente",
            range(1, len(categories) + 1),
        )
        return categories[option - 1]
