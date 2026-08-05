"""
Módulo do wrapper de campos de formulário.

Encapsula um widget CTkEntry ou CTkSegmentedButton com um identificador
(name_field) para coleta padronizada de valores.
"""

from dataclasses import dataclass
from typing import Union
from customtkinter import CTkEntry
from customtkinter import CTkSegmentedButton


@dataclass
class FormField:
    """
    Par nome-valor que associa um identificador a um widget de entrada.

    Args:
        name_field: Chave usada ao coletar valores do formulário (ex: ``"nome_produto"``).
        field: Widget CTkEntry ou CTkSegmentedButton subjacente.
    """

    name_field: str
    field: Union[CTkEntry, CTkSegmentedButton]

    def get(self) -> str:
        """Retorna o valor atual do campo."""
        return self.field.get()

    def clear(self) -> None:
        """Limpa o conteúdo do campo. Só funciona para CTkEntry."""
        if isinstance(self.field, CTkEntry):
            self.field.delete(0, "end")
            self.field.configure(placeholder_text=self.field.cget("placeholder_text"))
