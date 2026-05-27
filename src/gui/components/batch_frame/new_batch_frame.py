from customtkinter import CTkFrame, CTkLabel, CTkButton
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory

class NewBatchFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self._setup_ui()

    def _setup_ui(self):
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.configure(
            width=600,
            height=210,
            fg_color=COLORS.fundo_secundario,
            corner_radius=10,
            border_width=1,
            border_color=COLORS.bordas,
        )
    
    def _build_widgets(self):
        self._title_new_batch = CTkLabel(
            self,
            text="NOVO LOTE",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )

        self._batch_label = CTkLabel(
            self,
            text="Lote",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._field_batch = FieldFactory.create_entry(
            self,
            placeholder="Lote...",
            width=131,
            height=27,
        )

        self._code_chb_label = CTkLabel(
            self,
            text="Código CHB",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._field_code_chb = FieldFactory.create_entry(
            self,
            placeholder="Código CHB...",
            width=131,
            height=27,
        )
        self._manufacturer_date_label = CTkLabel(
            self,
            text="Data de fabricação",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._field_manufacturer_date = FieldFactory.create_data_entry(
            self,
            placeholder="Data de fabricação...",
            width=131,
            height=27,
        )
        self._expiration_date_label = CTkLabel(
            self,
            text="Data de validade",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._field_expiration_date = FieldFactory.create_data_entry(
            self,
            placeholder="Data de validade...",
            width=131,
            height=27,
        )
        self._product_firm_label = CTkLabel(
            self,
            text="Fabricante",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._field_product_firm = FieldFactory.create_entry(
            self,
            placeholder="Fabricante...",
            width=131,
            height=27,
        )
        self._product_label = CTkLabel(
            self,
            text="Produto",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._field_product = FieldFactory.create_entry(
            self,
            placeholder="Produto...",
            width=131,
            height=27,
        )
        self._quantity_label = CTkLabel(
            self,
            text="Quantidade",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )

        self._field_quantity = FieldFactory.create_entry(
            self,
            placeholder="Quantidade...",
            width=131,
            height=27,
        )
        self._nf_label = CTkLabel(
            self,
            text="Nota Fiscal",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._field_nf = FieldFactory.create_entry(
            self,
            placeholder="Nota Fiscal...",
            width=131,
            height=27,
        )

        self._save_batch_button = CTkButton(
            self,
            text="Salvar Lote",
            fg_color=COLORS.botao_principal,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            command=None
        )
        self._save_batch_button.configure(
            width=103,
            height=27,
            corner_radius=5,
        )

        self._cancel_batch_button = CTkButton(
            self,
            text="Cancelar",
            fg_color=COLORS.elevado,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            command=None
        )
        self._cancel_batch_button.configure(
            width=76,
            height=27,
            corner_radius=5,
            border_width=1,
            border_color=COLORS.bordas,
        )
    def _layout_widgets(self):
        self._title_new_batch.place(x=10, y=4, anchor="nw")
        self._title_new_batch.pack_propagate(False)

        self._batch_label.place(x=10, y=30, anchor="nw")
        self._batch_label.pack_propagate(False)
        self._field_batch.place(x=10, y=55, anchor="nw")
        self._field_batch.pack_propagate(False)

        self._code_chb_label.place(x=159, y=30, anchor="nw")
        self._code_chb_label.pack_propagate(False)
        self._field_code_chb.place(x=159, y=55, anchor="nw")
        self._field_code_chb.pack_propagate(False)

        self._manufacturer_date_label.place(x=307, y=30, anchor="nw")
        self._manufacturer_date_label.pack_propagate(False)
        self._field_manufacturer_date.place(x=307, y=55, anchor="nw")
        self._field_manufacturer_date.pack_propagate(False)

        self._expiration_date_label.place(x=455, y=30, anchor="nw")
        self._expiration_date_label.pack_propagate(False)
        self._field_expiration_date.place(x=455, y=55, anchor="nw")
        self._field_expiration_date.pack_propagate(False)

        self._product_firm_label.place(x=10, y=92, anchor="nw")
        self._product_firm_label.pack_propagate(False)
        self._field_product_firm.place(x=10, y=117, anchor="nw")
        self._field_product_firm.pack_propagate(False)

        self._product_label.place(x=159, y=92, anchor="nw")
        self._product_label.pack_propagate(False)
        self._field_product.place(x=159, y=117, anchor="nw")
        self._field_product.pack_propagate(False)

        self._quantity_label.place(x=307, y=92, anchor="nw")
        self._quantity_label.pack_propagate(False)
        self._field_quantity.place(x=307, y=117, anchor="nw")
        self._field_quantity.pack_propagate(False)

        self._nf_label.place(x=455, y=92, anchor="nw")
        self._nf_label.pack_propagate(False)
        self._field_nf.place(x=455, y=117, anchor="nw")
        self._field_nf.pack_propagate(False)

        self._save_batch_button.place(x=483, y=167, anchor="nw")
        self._save_batch_button.pack_propagate(False)

        self._cancel_batch_button.place(x=391, y=167, anchor="nw")
        self._cancel_batch_button.pack_propagate(False)