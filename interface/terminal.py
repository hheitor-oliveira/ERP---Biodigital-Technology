# lib's import
import os
from decimal import Decimal

class Terminal:
    """Utilitário responsável pela interface do terminal."""

    @staticmethod
    def ask_decimal(message: str) -> Decimal:
      return Decimal(input(f"{message}: ").replace(",", "."))

    @staticmethod
    def clear() -> None:
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def separator(length: int = 60) -> None:
        print("─" * length)

    @staticmethod
    def header(title: str) -> None:
        Terminal.clear()
        Terminal.separator()
        print(title.center(60))
        Terminal.separator()

    @staticmethod
    def success(message: str) -> None:
        print(f"\n✅ {message}\n")

    @staticmethod
    def warning(message: str) -> None:
        print(f"\n⚠️  {message}\n")

    @staticmethod
    def error(message: str) -> None:
        print(f"\n❌ {message}\n")

    @staticmethod
    def pause() -> None:
        input("Pressione ENTER para continuar...")

    @staticmethod
    def ask(message: str) -> str:
        return input(f"{message}: ")

    @staticmethod
    def ask_int(message: str) -> int:
        return int(input(f"{message}: "))