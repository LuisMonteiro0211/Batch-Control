"""
Módulo do formulário de cadastro de novo lote.

Métodos públicos:
    - get_values_from_frame(): Coleta os valores e retorna um BatchDTO.
    - clear_fields(): Limpa todos os campos de entrada.
"""

from customtkinter import CTkFrame, CTkLabel, CTkButton
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory, LabelNameField
from src.dtos.batch_dto import BatchDTO


class NewBatchFrame(CTkFrame):
    """
    Formulário para cadastro de um novo lote.

    Args:
        master: Widget pai (BatchFrame).
    """

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

        self._batch_label = LabelNameField.create_label_name_field(self, "Lote")
        self._field_batch = FieldFactory.create_entry(
            self,
            placeholder="Lote...",
            width=131,
            height=27,
            name_field="batch_name"
        )

        self._code_chb_label = LabelNameField.create_label_name_field(self, "Código CHB")
        self._field_code_chb = FieldFactory.create_number_entry(
            self,
            placeholder="Código CHB...",
            width=131,
            height=27,
            name_field="code_chb"
        )
        self._manufacturer_date_label = LabelNameField.create_label_name_field(self, "Data de fabricação")
        self._field_manufacturer_date = FieldFactory.create_data_entry(
            self,
            placeholder="Data de fabricação...",
            width=131,
            height=27,
            name_field="manufacturer_date"
        )
        self._expiration_date_label = LabelNameField.create_label_name_field(self, "Data de validade")
        self._field_expiration_date = FieldFactory.create_data_entry(
            self,
            placeholder="Data de validade...",
            width=131,
            height=27,
            name_field="expiration_date"
        )
        self._product_firm_label = LabelNameField.create_label_name_field(self, "Fabricante")
        self._field_product_firm = FieldFactory.create_locked_entry(
            self,
            width=131,
            height=27,
            value="Fabricante..."
        )
        self._product_label = LabelNameField.create_label_name_field(self, "Produto")
        self._field_product = FieldFactory.create_locked_entry(
            self,
            width=131,
            height=27,
            value="Produto..."
        )
        self._quantity_label = LabelNameField.create_label_name_field(self, "Quantidade")

        self._field_quantity = FieldFactory.create_number_entry(
            self,
            placeholder="Quantidade...",
            width=131,
            height=27,
            name_field="quantity"
        )
        self._nf_label = LabelNameField.create_label_name_field(self, "Nota Fiscal")
        self._field_nf = FieldFactory.create_number_entry(
            self,
            placeholder="Nota Fiscal...",
            width=131,
            height=27,
            name_field="nf"
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
        self._field_batch.field.place(x=10, y=55, anchor="nw")

        self._code_chb_label.place(x=159, y=30, anchor="nw")
        self._code_chb_label.pack_propagate(False)
        self._field_code_chb.field.place(x=159, y=55, anchor="nw")

        self._manufacturer_date_label.place(x=307, y=30, anchor="nw")
        self._manufacturer_date_label.pack_propagate(False)
        self._field_manufacturer_date.field.place(x=307, y=55, anchor="nw")

        self._expiration_date_label.place(x=455, y=30, anchor="nw")
        self._expiration_date_label.pack_propagate(False)
        self._field_expiration_date.field.place(x=455, y=55, anchor="nw")

        self._product_firm_label.place(x=10, y=92, anchor="nw")
        self._product_firm_label.pack_propagate(False)
        self._field_product_firm.place(x=10, y=117, anchor="nw")

        self._product_label.place(x=159, y=92, anchor="nw")
        self._product_label.pack_propagate(False)
        self._field_product.place(x=159, y=117, anchor="nw")

        self._quantity_label.place(x=307, y=92, anchor="nw")
        self._quantity_label.pack_propagate(False)
        self._field_quantity.field.place(x=307, y=117, anchor="nw")

        self._nf_label.place(x=455, y=92, anchor="nw")
        self._nf_label.pack_propagate(False)
        self._field_nf.field.place(x=455, y=117, anchor="nw")

        self._save_batch_button.place(x=483, y=167, anchor="nw")
        self._save_batch_button.pack_propagate(False)

        self._cancel_batch_button.place(x=391, y=167, anchor="nw")
        self._cancel_batch_button.pack_propagate(False)

    def get_values_from_frame(self) -> BatchDTO:
        """
        Coleta os valores atuais de todos os campos e retorna um BatchDTO.

        Returns:
            BatchDTO com os dados digitados no formulário.
        """
        return BatchDTO(
            batch=self._field_batch.get(),
            code_chb=self._field_code_chb.get(),
            manufacturer_date=self._field_manufacturer_date.get(),
            expiration_date=self._field_expiration_date.get(),
            product_firm=self._field_product_firm.get(),
            product=self._field_product.get(),
            quantity=self._field_quantity.get(),
            nf=self._field_nf.get(),
        )

    def clear_fields(self) -> None:
        """Limpa o conteúdo de todos os campos de entrada."""
        for form_field in (
            self._field_batch,
            self._field_code_chb,
            self._field_manufacturer_date,
            self._field_expiration_date,
            self._field_quantity,
            self._field_nf,
        ):
            form_field.clear()

        FieldFactory.set_value_locked_entry(self._field_product_firm, "Fabricante...")
        FieldFactory.set_value_locked_entry(self._field_product, "Produto...")