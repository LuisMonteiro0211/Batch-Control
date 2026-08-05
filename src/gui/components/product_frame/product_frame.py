from customtkinter import CTkFrame, CTkLabel
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory
from .new_product_frame import NewProductFrame
from .edit_product_frame import EditProductFrame
from .product_table import ProductTable
from typing import Callable, Dict, List, Optional
from src.dtos.product_dto import ProductCardDTO, ProductDTO

class ProductFrame(CTkFrame):
    def __init__(
        self,
        master,
        on_click_save_product: Callable,
        on_click_save_edit_product: Callable,
        on_click_edit_product: Callable,
        products_to_view: List[ProductCardDTO],
    ):
        super().__init__(master)
        self._products_to_view = products_to_view
        self._current_frame = None
        #Callbacks
        self._on_click_save_product = on_click_save_product
        self._on_click_save_edit_product = on_click_save_edit_product
        self._on_click_edit_product = on_click_edit_product
        #Frames
        self._edit_product_frame: Optional[EditProductFrame] = None
        self._state_product_frame = None
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.configure(
            width=720,
            height=580,
            fg_color=COLORS.fundo_secundario,
            corner_radius=0,
        )

    def _build_widgets(self):
        self._title_product = CTkLabel(
            self,
            text="Produtos",
            text_color=COLORS.texto_principal,
            font=FONTS.titulo_tela
        )

        self._subtitle_product = CTkLabel(
            self,
            text="Gerencie o catálogo de produtos",
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_tela
        )

        self._new_product_frame = NewProductFrame(self, on_click_save_product=self._on_click_save_product)
        self._state_product_frame = "new_product"

        self._product_search_frame = CTkFrame(self,
        width=685,
        height=284,
        fg_color=COLORS.transparente,
        corner_radius=0,
        )
        self._product_search_label = CTkLabel(self._product_search_frame,
        text="Buscar",
        text_color=COLORS.texto_principal,
        font=FONTS.titulo_tela)
        self._subtitle_search = CTkLabel(self._product_search_frame,
        text="Pesquisa de produtos",
        text_color=COLORS.desabilitado,
        font=FONTS.subtitulo_tela)

        self._search_entry = FieldFactory.create_search_entry(
            master=self._product_search_frame,
            placeholder="Buscar produto...",
            name_field="search_product_name"
        )
        self._product_table = ProductTable(
            self,
            products_to_view=self._products_to_view,
            on_edit_product=self._on_click_edit_product,
        )
        self._product_table.initialization()

    def _layout_widgets(self):
        self._title_product.place(x=12, y=8, anchor="nw")
        self._title_product.pack_propagate(False)
        self._subtitle_product.place(x=12, y=30, anchor="nw")
        self._subtitle_product.pack_propagate(False)

        self._new_product_frame.place(x=12, y=70, anchor="nw")
        self._new_product_frame.pack_propagate(False)

        self._product_search_frame.place(x=12, y=281, anchor="nw")
        self._product_search_frame.pack_propagate(False)

        self._product_search_label.place(x=0, y=0, anchor="nw")
        self._subtitle_search.place(x=0, y=22, anchor="nw")

        self._search_entry.field.place(x=0, y=48, anchor="nw")

        self._product_table.place(x=16, y=365, anchor="nw")
        self._product_table.pack_propagate(False)

    def show_edit_product(self, product_dto: ProductDTO) -> None:
        self._edit_product_frame = EditProductFrame(
            self,
            product_dto=product_dto,
            save_callback=self._on_click_save_edit_product,
            cancel_callback=self._cancel_edit_product_frame,
        )
        self._edit_product_frame.set_date_product_dto()
        self._edit_product_frame.place(x=12, y=54, anchor="nw")
        self._edit_product_frame.pack_propagate(False)
        self._state_product_frame = "edit_product"
        self.hide_new_product_frame()

    def _cancel_edit_product_frame(self) -> None:
        if self._edit_product_frame is not None:
            self.hide_edit_product_frame()
            self._state_product_frame = "new_product"
            self.show_new_product()

    def show_new_product(self) -> None:
        """
        Mostra o frame de novo produto.
        """
        if self._edit_product_frame is not None:
            self.hide_edit_product_frame()
        self._new_product_frame.place(x=12, y=70, anchor="nw")

    def hide_new_product_frame(self) -> None:
        """
        Oculta o frame de novo produto.
        """
        if self._new_product_frame is not None:
            self._new_product_frame.place_forget()

    def hide_edit_product_frame(self) -> None:
        """
        Oculta o frame de edição de produto.
        """
        if self._edit_product_frame is not None:
            self._edit_product_frame.destroy()

    def get_state_product_frame(self) -> Optional[str]:
        if self._state_product_frame is not None:
            return self._state_product_frame

    def get_raw_values(self) -> Dict[str, str]:
        if self._edit_product_frame is not None:
            return self._edit_product_frame.get_raw_values()
        return {}