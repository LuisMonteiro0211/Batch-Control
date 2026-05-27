from customtkinter import CTkFrame
from src.gui.components.scrollbar_frame import ScrollbarFrame
from src.gui.components.factory import LabelValueTable
from src.gui.theme import COLORS
from src.helpers.image_helper import icon_button

class BatchTable(ScrollbarFrame):
    def __init__(self, master):
        super().__init__(master)
        self._setup_ui()

    def _setup_ui(self):
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

        self._label_batch = LabelValueTable.create_label_value_table(master=self._header_frame, label="Lote")
        self._label_product = LabelValueTable.create_label_value_table(master=self._header_frame, label="Produto")
        self._label_product_firm = LabelValueTable.create_label_value_table(master=self._header_frame, label="Fabricante")
        self._label_quantity = LabelValueTable.create_label_value_table(master=self._header_frame, label="Saldo")
        self._label_manufacturer_date = LabelValueTable.create_label_value_table(master=self._header_frame, label="Fabricação")
        self._label_expiration_date = LabelValueTable.create_label_value_table(master=self._header_frame, label="Validade")
        self._label_status = LabelValueTable.create_label_value_table(master=self._header_frame, label="Status")


    def _layout_table_header(self):
        self._header_frame.pack(side="top", fill="x")
        self._header_frame.pack_propagate(False)

        self._label_batch.place(x=9, y=2, anchor="nw")
        self._label_batch.pack_propagate(False)

        self._label_product.place(x=120, y=2, anchor="nw")
        self._label_product.pack_propagate(False)

        self._label_product_firm.place(x=223, y=2, anchor="nw")
        self._label_product_firm.pack_propagate(False)
        
        self._label_quantity.place(x=320, y=2, anchor="nw")
        self._label_quantity.pack_propagate(False)

        self._label_manufacturer_date.place(x=396, y=2, anchor="nw")
        self._label_manufacturer_date.pack_propagate(False)

        self._label_expiration_date.place(x=530, y=2, anchor="nw")
        self._label_expiration_date.pack_propagate(False)

        self._label_status.place(x=630, y=2, anchor="nw")
        self._label_status.pack_propagate(False)

    def initialization(self):
        self.initialization_message("Nenhum alerta disponível", self._icon_check)