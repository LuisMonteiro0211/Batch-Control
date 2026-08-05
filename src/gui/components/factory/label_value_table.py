"""
Módulo para criação de labels de valor em tabelas.

Usado nas colunas de cabeçalho e nas células de dados das tabelas
de produtos e lotes.
"""

from customtkinter import CTkLabel
from src.gui.theme import COLORS, FONTS


class LabelValueTable:
    """Factory estática para labels de células e cabeçalhos de tabela."""

    @staticmethod
    def create_label_value_table(master, label) -> CTkLabel:
        """
        Cria um label para exibir um valor ou título de coluna na tabela.

        Args:
            master: Widget pai (linha ou cabeçalho da tabela).
            label: Texto ou valor a ser exibido.

        Returns:
            CTkLabel estilizado para uso em tabelas.
        """
        label_value_table = CTkLabel(
            master,
            text=label,
            text_color=COLORS.texto_secundario,
            font=FONTS.texto_tabela,
            fg_color=COLORS.transparente
        )
        return label_value_table
