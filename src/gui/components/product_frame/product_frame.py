"""
Módulo do frame principal de produtos.

Compõe o formulário de cadastro, busca e tabela de produtos,
alternando entre os modos de novo produto e edição.

Métodos públicos:
    - show_edit_product(): Exibe o formulário de edição preenchido.
    - show_new_product(): Exibe o formulário de novo produto.
    - hide_new_product_frame(): Oculta o formulário de novo produto.
    - hide_edit_product_frame(): Destroi o formulário de edição.
    - get_state_product_frame(): Retorna o estado atual (new_product ou edit_product).
    - get_raw_values(): Coleta os valores do formulário de edição ativo.
"""

from customtkinter import CTkFrame, CTkLabel
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory
from .new_product_frame import NewProductFrame
from .edit_product_frame import EditProductFrame
from .product_table import ProductTable
from typing import Callable, List, Optional
from src.dtos.product_dto import ProductCardDTO, ProductDTO
from src.forms.product_form_types import EditProductRawData
from .product_frame_state import ProductFrameState


class ProductFrame(CTkFrame):
    """
    Frame principal da tela de produtos.

    Args:
        master: Widget pai.
        on_click_save_product: Callback ao salvar um novo produto.
        on_click_save_edit_product: Callback ao salvar edição de produto.
        on_click_edit_product: Callback ao clicar em editar na tabela.
        products_to_view: Produtos exibidos na tabela de alertas.
    """

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
        self._on_click_save_product = on_click_save_product
        self._on_click_save_edit_product = on_click_save_edit_product
        self._on_click_edit_product = on_click_edit_product
        self._edit_product_frame: Optional[EditProductFrame] = None
        self._state_product_frame: Optional[ProductFrameState] = None
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self) -> None:
        """Define dimensões e cores do frame."""
        self.configure(
            width=720,
            height=580,
            fg_color=COLORS.fundo_secundario,
            corner_radius=0,
        )

    def _build_widgets(self) -> None:
        """Cria título, formulários, busca e tabela de produtos."""
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
        self._state_product_frame = ProductFrameState.NEW_PRODUCT #Define o estado inicial do frame como novo produto

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
        )
        self._product_table = ProductTable(
            self,
            products_to_view=self._products_to_view,
            on_edit_product=self._on_click_edit_product,
        )
        self._product_table.initialization()

    def _layout_widgets(self) -> None:
        """Posiciona os widgets na tela."""
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
        """
        Substitui o formulário de novo produto pelo de edição, preenchido com os dados do DTO.

        Args:
            product_dto: Dados do produto a ser editado.
        """
        self._edit_product_frame = EditProductFrame(
            self,
            product_dto=product_dto,
            save_callback=self._on_click_save_edit_product,
            cancel_callback=self._cancel_edit_product_frame,
        )
        self._edit_product_frame.set_data_product_dto()
        self._edit_product_frame.place(x=12, y=54, anchor="nw")
        self._edit_product_frame.pack_propagate(False)
        self._state_product_frame = ProductFrameState.EDIT_PRODUCT
        #Mudo o estado do frame para frame de edição
        self.hide_new_product_frame()

    def _cancel_edit_product_frame(self) -> None:
        """Cancela a edição e retorna ao formulário de novo produto."""
        if self._edit_product_frame is not None:
            self.hide_edit_product_frame()
            self._state_product_frame = ProductFrameState.NEW_PRODUCT
            #Mudo o estado do frame para frame de novo produto
            self.show_new_product()

    def show_new_product(self) -> None:
        """Exibe o formulário de cadastro de novo produto."""
        if self._edit_product_frame is not None:
            self.hide_edit_product_frame()
        self._new_product_frame.place(x=12, y=70, anchor="nw")

    def hide_new_product_frame(self) -> None:
        """Oculta o formulário de novo produto sem destruí-lo."""
        if self._new_product_frame is not None:
            self._new_product_frame.place_forget()

    def hide_edit_product_frame(self) -> None:
        """Destroi o formulário de edição ativo."""
        if self._edit_product_frame is not None:
            self._edit_product_frame.destroy()
            self._edit_product_frame = None

    def get_state_product_frame(self) -> Optional[ProductFrameState]:
        """
        Retorna o estado atual do frame de formulário.

        Returns:
            ``ProductFrameState.NEW_PRODUCT``, ``ProductFrameState.EDIT_PRODUCT`` ou None se ainda não inicializado.
        """
        return self._state_product_frame

    def get_raw_values(self) -> EditProductRawData:
        """
        Coleta os valores do formulário de edição ativo.

        Returns:
            Dicionário com chaves dos campos e valores digitados, ou vazio se não houver edição.
        """
        if self._edit_product_frame is not None:
            return self._edit_product_frame.get_raw_values()
        return EditProductRawData(
            nome_produto="",
            empresa="",
            saldo_min="",
            ativo="",
        )
