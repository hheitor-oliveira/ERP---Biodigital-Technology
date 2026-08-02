from interface.core.terminal import Terminal
from services.inventory.product_service import ProductService


class ConsultMenu:
    def __init__(self) -> None:
        self._product_service = ProductService()

    def run(self) -> None:
        while True:
            Terminal.header("Inventário", "Consultas")
            Terminal.options(
                [
                    "Listar produtos",
                    "Consultar categorias",
                    "Voltar",
                ]
            )
            Terminal.separator()

            option = Terminal.ask_option("Digite a opção desejada", range(1, 4))

            if option == 1:
                self._list_products()
            elif option == 2:
                Terminal.warning("Consulta de categorias em desenvolvimento.")
                Terminal.pause()
            elif option == 3:
                break

    def _list_products(self) -> None:
        products = self._product_service.list_products()
        rows = []

        for product in products:
            status = product.status.value if hasattr(product.status, "value") else product.status
            rows.append(
                [
                    product.name.title(),
                    product.category.name.capitalize(),
                    product.stock_quantity,
                    Terminal.money(product.sale_value),
                    status,
                ]
            )

        Terminal.header("Produtos cadastrados", "Inventário")
        Terminal.table(
            ["Produto", "Categoria", "Estoque", "Venda", "Status"],
            rows,
        )
        print()
        Terminal.pause()
