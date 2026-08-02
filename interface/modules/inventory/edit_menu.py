from interface.core.terminal import Terminal


class EditMenu:
    def run(self) -> None:
        while True:
            Terminal.header("Inventário", "Edições de produto")
            Terminal.options(
                [
                    "Mudar nome",
                    "Mudar valor de venda",
                    "Mudar preço de custo",
                    "Mudar status",
                    "Mudar categoria",
                    "Voltar",
                ]
            )
            Terminal.separator()

            option = Terminal.ask_option("Digite a opção desejada", range(1, 7))

            if option == 1:
                Terminal.error('Função em desenvolvimento')
                Terminal.pause()
            elif option == 2:
                Terminal.error('Função em desenvolvimento')
                Terminal.pause()
            elif option == 3:
                Terminal.error('Função em desenvolvimento')
                Terminal.pause()
            elif option == 4:
                Terminal.error('Função em desenvolvimento')
                Terminal.pause()
            elif option == 5:
                Terminal.error('Função em desenvolvimento')
                Terminal.pause()
            elif option == 6:
                break
