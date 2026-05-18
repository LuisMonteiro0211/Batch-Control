"""
Módulo para criação dos botões do menu lateral.
Esse módulo inclui ações de mouse sobre o botão, como hover, enter e leave.
Já inclui a imagem do botão e o texto.

Métodos públicos:
    - select(): Muda o estado do botão para selecionado.
    - deselect(): Muda o estado do botão para deselecionado.

Métodos privados:
    - _on_mouse_enter(): Método para configurar aparênca do botão quando é identificado que o mouse está sobre ele.
    - _on_mouse_leave(): Método para configurar aparênca do botão quando é identificado que o mouse saiu de cima dele.

Uso recomendado:
    >>> from src.gui.components.menu_button import MenuButton

    >>> btn = MenuButton(master, text="Botão", command=lambda: print("Botão clicado"))
    >>> btn.pack(pady=20)

    >>> btn.select()
    >>> btn.deselect()
    >>> btn.deselect()
"""

from customtkinter import CTkButton, CTkFont
from src.gui.theme import COLORS, FONTS
from src.helpers.image_helper import icon_button
from typing import Callable

class MenuButton(CTkButton):
    """
    Classe para criação dos botões do menu lateral.

    Args:
        master: Widget pai do botão.
        text: Texto do botão.
        command: Função a ser executada quando o botão for clicado.
    """

    def __init__(self, master, text: str, name_icon: str, command: Callable|None):
        self._is_selected = False
        self._icon_enabled = icon_button(name_icon+"_habilitado.png")
        self._icon_disabled = icon_button(name_icon+"_desabilitado.png")

        super().__init__(
            master=master,
            text=text,
            command=command,
            fg_color=COLORS.transparente,
            text_color=COLORS.desabilitado,
            font=CTkFont(family=FONTS.valor, size=13, weight="normal"),
            image=self._icon_disabled,
            compound="left",
            anchor="w",
            hover=False,
            height=30,
            width=165,
            corner_radius=10
        )

        self.bind("<Enter>", self._on_mouse_enter)
        self.bind("<Leave>", self._on_mouse_leave)

    def _on_mouse_enter(self, event):
        "Método para configurar aparênca do botão quando é identificado que o mouse está sobre ele."
        if not self._is_selected:
            self.configure(
                fg_color=COLORS.elevado,
                text_color=COLORS.desabilitado
            )

    def _on_mouse_leave(self, event):
        "Método para configurar aparênca do botão quando é identificado que o mouse saiu de cima dele."
        if not self._is_selected:
            self.configure(
                fg_color=COLORS.transparente,
                text_color=COLORS.desabilitado
            )

    def select(self):
        "API pública para mudar o estado do botão para selecionado."

        self._is_selected = True

        self.configure(
            image=self._icon_enabled,
            fg_color=COLORS.botao_selecionado,
            text_color=COLORS.texto_selecionado
        )

    def deselect(self):
        "API pública para mudar o estado do botão para deselecionado."

        self._is_selected = False
        self.configure(
            image=self._icon_disabled,
            fg_color=COLORS.transparente,
            text_color=COLORS.desabilitado
        )