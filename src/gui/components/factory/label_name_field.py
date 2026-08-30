"""
Módulo para criação de labels de nome de campo em formulários.

Usado acima de cada input para identificar o campo ao usuário.
"""

from customtkinter import CTkLabel
from src.gui.theme import COLORS, FONTS


class LabelNameField:
    """Factory estática para labels de identificação de campos de formulário."""

    @staticmethod
    def create_label_name_field(master, label: str) -> CTkLabel:
        """
        Cria um label com o nome do campo.

        Args:
            master: Widget pai do label.
            label: Texto exibido (ex: "Produto", "Empresa").

        Returns:
            CTkLabel estilizado conforme o tema da aplicação.
        """
        label_name_field = CTkLabel(
            master=master,
            text=label,
            font=FONTS.texto_tabela,
            text_color=COLORS.desabilitado
        )

        return label_name_field
