from customtkinter import CTkFrame
from src.gui.components.scrollbar_frame import ScrollbarFrame
from src.gui.components.factory import LabelValueTable
from src.gui.theme.theme import COLORS
from src.helpers.image_helper import icon_button

class ProductTable(ScrollbarFrame):
    def __init__(self, master):
        super().__init__(master)
        self._configure_layout()
        self._create_header_frame()
        self._layout_table_header()
        self._icon_check = icon_button("check.png")

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

    def initialization(self):

        self.initialization_message("Nenhum alerta disponível", self._icon_check)



    