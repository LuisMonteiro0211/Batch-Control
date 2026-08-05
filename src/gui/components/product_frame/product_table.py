"""
Módulo da tabela de produtos com alertas de estoque.

Exibe uma lista rolável de produtos abaixo do saldo mínimo,
com ícones de status e botão de edição por linha.

Métodos públicos:
    - initialization(): Popula a tabela com os produtos ou mensagem vazia.
"""

from customtkinter import CTkButton, CTkFrame, CTkLabel
from src.dtos import ProductCardDTO
from src.gui.components.scrollbar_frame import ScrollbarFrame
from src.gui.components.factory import LabelValueTable
from src.gui.theme import COLORS, FONTS
from src.helpers.image_helper import icon_button, resize_image
from src.paths import icon_path
from typing import Callable, List

from src.model.stock_level import StockLevel
from src.exceptions.exceptions import BatchControlError


class ProductTable(ScrollbarFrame):
    """
    Tabela rolável de produtos com alertas de estoque.

    Args:
        master: Widget pai.
        products_to_view: Lista de produtos a exibir na tabela.
        on_edit_product: Callback recebendo o product_id ao clicar em "Editar".
    """

    def __init__(self, master, products_to_view: List[ProductCardDTO], on_edit_product: Callable[[int], None]):
        super().__init__(master)
        self._on_edit_product = on_edit_product
        self._configure_layout()
        self._create_header_frame()
        self._layout_table_header()
        self._icon_check = icon_button("check.png", size=(16, 16))
        self._products_to_view = products_to_view

    def _create_header_frame(self) -> None:
        """Cria a linha de cabeçalho com os títulos das colunas."""
        self._header_frame = CTkFrame(
            self,
            width=681,
            height=32,
            fg_color=COLORS.fundo_primario,
            corner_radius=0,
            border_width=1,
            border_color=COLORS.bordas,

        )
        self._label_code = LabelValueTable.create_label_value_table(self._header_frame, "Código")
        self._label_name_product = LabelValueTable.create_label_value_table(self._header_frame, "Nome do Produto")
        self._label_product_firm = LabelValueTable.create_label_value_table(self._header_frame, "Marca")
        self._label_minimum_balance = LabelValueTable.create_label_value_table(self._header_frame, "Saldo Mínimo")
        self._label_current_balance = LabelValueTable.create_label_value_table(self._header_frame, "Saldo Atual")
        self._label_status = LabelValueTable.create_label_value_table(self._header_frame, "Status")
        self._label_actions = LabelValueTable.create_label_value_table(self._header_frame, "Ações")

    def _layout_table_header(self) -> None:
        """Posiciona os labels do cabeçalho."""
        self._header_frame.pack(side="top", fill="x")
        self._header_frame.pack_propagate(False)
        self._label_code.place(x=7, y=2, anchor="nw")
        self._label_code.pack_propagate(False)
        self._label_name_product.place(x=81, y=2, anchor="nw")
        self._label_name_product.pack_propagate(False)
        self._label_product_firm.place(x=226, y=2, anchor="nw")
        self._label_product_firm.pack_propagate(False)
        self._label_minimum_balance.place(x=296, y=2, anchor="nw")
        self._label_minimum_balance.pack_propagate(False)
        self._label_current_balance.place(x=412, y=2, anchor="nw")
        self._label_current_balance.pack_propagate(False)
        self._label_status.place(x=537, y=2, anchor="nw")
        self._label_status.pack_propagate(False)
        self._label_actions.place(x=609, y=2, anchor="nw")
        self._label_actions.pack_propagate(False)

    def _create_cards_items(self) -> List[CTkFrame]:
        """
        Cria uma linha (card) na tabela para cada produto da lista.

        Returns:
            Lista de CTkFrame, um por produto, prontos para inserção na tabela.
        """
        path_icon_yellow_alert = icon_path("circle-alert_yellow.png")
        path_icon_red_alert = icon_path("circle-alert_red.png")
        path_icon_green_alert = icon_path("circle-alert_green.png")
        path_icon_grey_alert = icon_path("circle-alert.png")

        TABLE_ICONS = {
            StockLevel.ALERTA: resize_image(path_icon_yellow_alert, (17, 17)),
            StockLevel.CRITICO: resize_image(path_icon_red_alert, (17, 17)),
            StockLevel.NORMAL: resize_image(path_icon_green_alert, (17, 17)),
        }

        products = self._products_to_view
        product_cards: List[CTkFrame] = []

        for product in products:
            card_item: CTkFrame = CTkFrame(
                self,
                width=681,
                height=32,
                corner_radius=0,
                border_width=1,
                border_color=COLORS.bordas,
                fg_color=COLORS.fundo_primario,
            )

            label_sku = LabelValueTable.create_label_value_table(card_item, product.product_code_chb)
            label_name_product = LabelValueTable.create_label_value_table(card_item, product.product_name)
            label_product_firm = LabelValueTable.create_label_value_table(card_item, product.product_firm)
            label_minimum_balance = LabelValueTable.create_label_value_table(card_item, product.minimun_balance)
            label_current_balance = LabelValueTable.create_label_value_table(card_item, product.current_balance)

            if not product.stock_level:
                raise BatchControlError("Stock level is required")

            status_icon = TABLE_ICONS.get(product.stock_level)
            label_status = CTkLabel(card_item, text="", image=status_icon, compound="left")
            button_action = CTkButton(
                card_item,
                text="Editar",
                width=51,
                height=15,
                corner_radius=5,
                fg_color=COLORS.fundo_secundario,
                hover_color="#3A3A3A",
                text_color=COLORS.texto_secundario,
                font=FONTS.texto_tabela,
                    command=lambda product_id=product.product_id: self._on_edit_product(product_id)
            )

            label_sku.place(x=9, y=2, anchor="nw")
            label_name_product.place(x=119, y=2, anchor="nw")
            label_product_firm.place(x=222, y=2, anchor="nw")
            label_minimum_balance.place(x=334, y=2, anchor="nw")
            label_current_balance.place(x=455, y=2, anchor="nw")
            label_status.place(x=551, y=2, anchor="nw")
            button_action.place(x=603, y=2, anchor="nw")

            product_cards.append(card_item)

        return product_cards

    def initialization(self) -> None:
        """Popula a tabela com os produtos ou exibe mensagem quando a lista está vazia."""
        if self._products_to_view is not None:
            product_cards = self._create_cards_items()

            for product_card in product_cards:
                self.insert_frame_item(product_card)
        else:
            self.initialization_message("Nenhum alerta disponível", self._icon_check)
