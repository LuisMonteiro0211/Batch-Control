from customtkinter import CTkButton, CTkFrame
from src.dtos import ProductCardDTO
from src.gui.components.scrollbar_frame import ScrollbarFrame
from src.gui.components.factory import LabelValueTable
from src.gui.theme import COLORS, FONTS
from src.helpers.image_helper import icon_button
from typing import List

class ProductTable(ScrollbarFrame):
    def __init__(self, master, products_to_view: List[ProductCardDTO]):
        super().__init__(master)
        self._configure_layout()
        self._create_header_frame()
        self._layout_table_header()
        self._icon_check = icon_button("check.png", size=(16, 16))
        self._products_to_view = products_to_view

    def _create_header_frame(self):
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

    def _layout_table_header(self):
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

    def _create_cards_items(self):
        """
         Para cada produto na lista da lista de produtos vai criar um card item para ser exibido na tabela.
         Args:
            None
         Returns:
            None
         """
        products = self._products_to_view

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

            # Build label value table for each product

            label_sku = LabelValueTable.create_label_value_table(card_item, product.product_code_chb)
            label_name_product = LabelValueTable.create_label_value_table(card_item, product.product_name)
            label_product_firm = LabelValueTable.create_label_value_table(card_item, product.product_firm)
            label_minimum_balance = LabelValueTable.create_label_value_table(card_item, product.minimun_balance)
            label_current_balance = LabelValueTable.create_label_value_table(card_item, product.current_balance)
            label_status = LabelValueTable.create_label_value_table(card_item, product.status)
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
                command=lambda: print("Editar produto")
            )

            # Layout card item

            label_sku.place(x=9, y=11, anchor="nw")
            label_name_product.place(x=119, y=11, anchor="nw")
            label_product_firm.place(x=222, y=11, anchor="nw")
            label_minimum_balance.place(x=334, y=11, anchor="nw")
            label_current_balance.place(x=455, y=11, anchor="nw")
            button_action.place(x=603, y=11, anchor="nw")



    def initialization(self):

        self.initialization_message("Nenhum alerta disponível", self._icon_check)



    