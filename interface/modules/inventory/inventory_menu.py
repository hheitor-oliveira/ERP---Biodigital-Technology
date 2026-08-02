from interface.core.terminal import Terminal
from interface.modules.inventory.consult_menu import ConsultMenu
from interface.modules.inventory.create_menu import CreateMenu
from interface.modules.inventory.edit_menu import EditMenu


class InventoryMenu:
    def __init__(self):
        self.create_menus = CreateMenu()
        self.consult_menus = ConsultMenu()
        self.edit_menus = EditMenu()

    def run(self):
        while True:
            Terminal.header("Inventário", "Produtos, categorias e movimentações")
            Terminal.options(
                [
                    "Cadastros",
                    "Consultas",
                    "Edições",
                    "Entrada/Saída",
                    "Voltar ao menu principal",
                ]
            )
            Terminal.separator()

            user_choice = Terminal.ask_option("Escolha a opção desejada", range(1, 6))

            if user_choice == 1:
                self.create_menus.main_create_menu()
            elif user_choice == 2:
                self.consult_menus.run()
            elif user_choice == 3:
                self.edit_menus.run()
            elif user_choice == 4:
                Terminal.warning("Entrada/Saída em desenvolvimento.")
                Terminal.pause()
            elif user_choice == 5:
                break
