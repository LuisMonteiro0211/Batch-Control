from customtkinter import CTkFrame, CTkLabel, CTkFont
from src.gui.theme import COLORS, FONTS


class ProductFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)


    def _configure_layout(self):
        self.configure(
            width=720,
            height=500,
            fg_color=COLORS.fundo_primario,
            corner_radius=0,
        )

    def _build_widgets(self):
        self._title_product = CTkLabel(
            self,
            text="Produtos",
            text_color=COLORS.texto_principal,
            font=CTkFont(family=FONTS.titulo_tela, size=18, weight="normal")
        )

        self._subtitle_product = CTkLabel(
            self,
            text="Gerencie o catálogo de produtos",
            text_color=COLORS.desabilitado,
            font=CTkFont(family=FONTS.subtitulo_tela, size=11, weight="normal")
        )

    def _layout_widgets(self):
        self._title_product.place(x=12, y=18, anchor="nw")
        self._title_product.pack_propagate(False)

        self._subtitle_product.place(x=12, y=34, anchor="nw")
        self._subtitle_product.pack_propagate(False)