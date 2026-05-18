from customtkinter import CTkFrame, CTkLabel, CTkFont
from .menu_button import MenuButton
from src.gui.theme import COLORS, FONTS, SETTINGS
from typing import Callable

class Sidebar(CTkFrame):
    def __init__(self, parent, on_click_product: Callable, on_click_batch: Callable):
        self._on_click_product = on_click_product
        self._on_click_batch = on_click_batch

        super().__init__(parent)
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.configure(
            width=190,
            height=580,
        )
        pass

    def _build_widgets(self):
        # Título da sidebar
        self._title_sidebar = CTkLabel(self, 
        text="LoteCtrl",
        text_color=COLORS.texto_principal,
        font=CTkFont(family=FONTS.titulo_tela, size=16, weight="bold"))

        # Subtítulo da sidebar
        self._subtitle_sidebar = CTkLabel(self,
        text="Controle de Lote",
        text_color=COLORS.desabilitado,
        font=CTkFont(family="Inter", size=13, weight="normal"))

        # Linha separadora
        self._separator_sidebar = CTkFrame(self,
        width=165,
        height=2,
        fg_color=COLORS.bordas)

        self._label_cadastro = CTkLabel(self,
        text="CADASTRO",
        text_color=COLORS.desabilitado,
        font=CTkFont(family="Inter", size=13, weight="normal"))

        # Botões da sidebar
        self._product_button = MenuButton(self, "Produtos", "produtos", command=self.handler_click_product)
        self._batch_button = MenuButton(self, "Lotes", "lotes", command=self.handler_click_batch)

    def _layout_widgets(self):
        self._title_sidebar.place(x=14, y=10, anchor="nw")
        self._title_sidebar.pack_propagate(False)

        self._subtitle_sidebar.place(x=14, y=30, anchor="nw")
        self._subtitle_sidebar.pack_propagate(False)

        self._separator_sidebar.place(x=6, y=55, anchor="nw")
        self._separator_sidebar.pack_propagate(False)
        
        self._label_cadastro.place(x=14, y=74, anchor="w")
        self._label_cadastro.pack_propagate(False)

        self._product_button.place(x=6, y=105, anchor="w")
        self._product_button.pack_propagate(False)

        self._batch_button.place(x=6, y=135, anchor="w")
        self._batch_button.pack_propagate(False)

    def handler_click_product(self):
        "Método para lidar com o clique no botão de produtos e atualizar o estado dos botões."
        self._product_button.select()
        self._batch_button.deselect()
        self._on_click_product()

    def handler_click_batch(self):
        "Método para lidar com o clique no botão de lotes e atualizar o estado dos botões."
        self._product_button.deselect()
        self._batch_button.select()
        self._on_click_batch()