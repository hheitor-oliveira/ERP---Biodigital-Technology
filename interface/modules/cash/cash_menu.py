from interface.core.terminal import Terminal


class CashMenu:
    def run(self) -> None:
        Terminal.header("Caixa", "Vendas, pagamentos e fechamento")
        Terminal.warning("Módulo de caixa em desenvolvimento.")
        Terminal.pause()
