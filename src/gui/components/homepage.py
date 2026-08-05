"""
Módulo da homepage da aplicação.

Exibe o logo centralizado na tela inicial, antes do usuário
navegar para produtos ou lotes.
"""

from customtkinter import CTkImage, CTkFrame, CTkLabel
from PIL import Image
from src.gui.theme import COLORS
from src.paths import icon_path


class Homepage(CTkFrame):
    """
    Tela inicial com o logo da aplicação centralizado.

    Args:
        master: Widget pai (janela principal).
    """

    def __init__(self, master):
        super().__init__(master)
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self) -> None:
        """Define dimensões e cor de fundo."""
        self.configure(
            width=717,
            height=580,
            fg_color=COLORS.fundo_primario
        )

    def _get_image(self) -> Image.Image:
        """Carrega a imagem do logo a partir dos assets."""
        image = Image.open(icon_path("brach_ctrl_logo_transparent.png"))
        return image

    def _build_widgets(self) -> None:
        """Cria o label com a imagem do logo."""
        self._image = CTkImage(
            light_image=self._get_image(),
            size=(270, 120)
        )
        self._label_image = CTkLabel(master=self, image=self._image, text="")

    def _layout_widgets(self) -> None:
        """Centraliza o logo na tela."""
        self._label_image.place(relx=0.5, rely=0.5, anchor="center")
