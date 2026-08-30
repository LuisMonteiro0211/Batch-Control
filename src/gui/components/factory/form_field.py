"""
Módulo do wrapper de campos de formulário.

Encapsula um widget CTkEntry ou CTkSegmentedButton com uma interface
uniforme (``get`` / ``clear``), simplificando a coleta e limpeza de
valores no formulário.
"""

from dataclasses import dataclass
from typing import Union
from customtkinter import CTkEntry
from customtkinter import CTkSegmentedButton


@dataclass
class FormField:
    """
    Wrapper de widget de entrada com interface uniforme.

    Args:
        field: Widget CTkEntry ou CTkSegmentedButton subjacente.
    """

    field: Union[CTkEntry, CTkSegmentedButton]

    def get(self) -> str:
        """Retorna o valor atual do campo."""
        return self.field.get()

    def clear(self) -> None:
        """Limpa o conteúdo do campo. Só funciona para CTkEntry."""
        if isinstance(self.field, CTkEntry):
            self.field.delete(0, "end")
            self.field.configure(placeholder_text=self.field.cget("placeholder_text"))
