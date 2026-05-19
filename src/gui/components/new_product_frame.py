from customtkinter import CTkFont, CTkFrame, CTkLabel
from src.gui.theme import COLORS
from src.gui.theme.theme import FONTS

class NewProductFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.configure(
            width=357,
            height=207,
            fg_color=COLORS.fundo_secundario,
            corner_radius=10,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _build_widgets(self):
        self._title_new_product = CTkLabel(
            self,
            text="NOVO PRODUTO",
            text_color=COLORS.desabilitado,
            font=CTkFont(family=FONTS.texto_tabela, size=12, weight="normal")
        )

    def _layout_widgets(self):
        self._title_new_product.place(x=10, y=6, anchor="nw")
        self._title_new_product.pack_propagate(False)