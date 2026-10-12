"""
Módulo do botão de ação primária reutilizável.

Encapsula um CTkButton já estilizado com as cores e fontes do tema,
para padronizar os botões de ação principal da aplicação.
"""

from typing import Callable
from customtkinter import CTkButton

from src.gui.theme.theme import COLORS, FONTS

class PrimaryActionButton(CTkButton):
    """
    Botão de ação primária com o estilo padrão da aplicação.

    Args:
        master: Widget pai do botão.
        text: Texto exibido no botão.
        command: Função chamada ao clicar no botão.
        height: Altura do botão em pixels.
        width: Largura do botão em pixels.
    """
    def __init__(self, master, text: str, command: Callable, height: int, width: int):
        self._master = master
        self._height = height
        self._width = width
        self._command = command
        self._text = text

        super().__init__(
            master=self._master,
            text=self._text,
            width=self._width,
            height=self._height,
            fg_color=COLORS.botao_principal,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            corner_radius=5,
            command=self._command
        )