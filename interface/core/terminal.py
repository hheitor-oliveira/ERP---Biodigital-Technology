import os
from decimal import Decimal, InvalidOperation
from typing import Iterable, Sequence


class Terminal:
    """Utilitário responsável pela interface do terminal."""

    WIDTH = 72

    @staticmethod
    def clear() -> None:
        if os.environ.get("TERM") or os.name == "nt":
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("\n" * 2)

    @staticmethod
    def separator(length: int | None = None) -> None:
        print("-" * (length or Terminal.WIDTH))

    @staticmethod
    def header(title: str, subtitle: str | None = None) -> None:
        Terminal.clear()
        Terminal.separator()
        print(title.upper().center(Terminal.WIDTH))
        if subtitle:
            print(subtitle.center(Terminal.WIDTH))
        Terminal.separator()

    @staticmethod
    def section(title: str) -> None:
        print()
        print(title)
        Terminal.separator()

    @staticmethod
    def success(message: str) -> None:
        print(f"\n[OK] {message}\n")

    @staticmethod
    def warning(message: str) -> None:
        print(f"\n[AVISO] {message}\n")

    @staticmethod
    def error(message: str) -> None:
        print(f"\n[ERRO] {message}\n")

    @staticmethod
    def pause() -> None:
        input("Pressione ENTER para continuar...")

    @staticmethod
    def ask(message: str) -> str:
        return input(f"{message}: ").strip()

    @staticmethod
    def ask_int(message: str) -> int:
        while True:
            try:
                return int(Terminal.ask(message))
            except ValueError:
                Terminal.error("Digite apenas números inteiros.")

    @staticmethod
    def ask_decimal(message: str) -> Decimal:
        while True:
            try:
                return Decimal(Terminal.ask(message).replace(",", "."))
            except InvalidOperation:
                Terminal.error("Digite um valor numérico válido.")

    @staticmethod
    def option(number: int, label: str, detail: str | None = None) -> None:
        suffix = f" - {detail}" if detail else ""
        print(f"{number:>2} - {label}{suffix}")

    @staticmethod
    def options(items: Sequence[str]) -> None:
        for number, label in enumerate(items, start=1):
            Terminal.option(number, label)

    @staticmethod
    def ask_option(message: str, valid_options: Iterable[int]) -> int:
        valid = set(valid_options)
        while True:
            option = Terminal.ask_int(message)
            if option in valid:
                return option

            Terminal.error("Opção inválida. Escolha uma opção do menu.")

    @staticmethod
    def field(number: int, label: str, value: object | None) -> None:
        formatted_value = value if value not in (None, "") else "Não informado"
        print(f"{number:>2} - {label:<18} {formatted_value}")

    @staticmethod
    def money(value: Decimal | None) -> str | None:
        if value is None:
            return None

        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    @staticmethod
    def empty(message: str) -> None:
        print(message.center(Terminal.WIDTH))

    @staticmethod
    def table(headers: Sequence[str], rows: Sequence[Sequence[object]]) -> None:
        if not rows:
            Terminal.empty("Nenhum registro encontrado.")
            return

        widths = [len(header) for header in headers]
        for row in rows:
            for index, value in enumerate(row):
                widths[index] = max(widths[index], len(str(value)))

        header_line = " | ".join(
            header.ljust(widths[index]) for index, header in enumerate(headers)
        )
        print(header_line)
        print("-" * len(header_line))

        for row in rows:
            print(
                " | ".join(
                    str(value).ljust(widths[index])
                    for index, value in enumerate(row)
                )
            )
