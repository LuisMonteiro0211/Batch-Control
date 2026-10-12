from typing import Callable
from customtkinter import CTkButton

from src.gui.theme.theme import COLORS, FONTS

class PrimaryActionButton(CTkButton):
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