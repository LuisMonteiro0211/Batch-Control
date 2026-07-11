from customtkinter import CTkButton, CTkFrame, CTkLabel
from src.dtos import ProductDTO
from src.gui.theme.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory, LabelNameField, FormField
from typing import Any, Callable, Dict


class EditProductFrame(CTkFrame):
    def __init__(
        self,
        parent,
        product_dto: ProductDTO,
        save_callback: Callable,
        cancel_callback: Callable,
    ):
        super().__init__(parent)
        self._product_dto: ProductDTO = product_dto
        self._save_callback = save_callback
        self._cancel_callback = cancel_callback
        self._setup_ui()

    def _setup_ui(self):
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()
        self._populate_fields()

    def _configure_layout(self):
        self.configure(
            width=619,
            height=224,
            fg_color=COLORS.fundo_secundario,
            corner_radius=10,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _build_widgets(self):
        self._title_edit_product = CTkLabel(
            self,
            text="EDITAR PRODUTO",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela,
        )

        self._name_product_label = LabelNameField.create_label_name_field(self, "Produto")
        self._minimun_balance_label = LabelNameField.create_label_name_field(self, "Saldo mínimo")
        self._product_code_chb_label = LabelNameField.create_label_name_field(self, "Código CHB")
        self._product_firm_label = LabelNameField.create_label_name_field(self, "Fabricante")
        self._consumption_monthly_label = LabelNameField.create_label_name_field(self, "Consumo mensal")

        self._name_product = FieldFactory.create_entry(
            master=self,
            placeholder="Nome do produto",
            width=159,
            height=27,
            name_field="nome_produto",
        )
        self._minimun_balance = FieldFactory.create_number_entry(
            master=self,
            placeholder="Saldo mínimo",
            width=159,
            height=27,
            name_field="saldo_min",
        )
        self._product_code_chb = FieldFactory.create_locked_entry(
            master=self,
            width=159,
            height=27,
            value=str(self._product_dto.product_code_chb),
        )
        self._product_firm = FieldFactory.create_entry(
            master=self,
            placeholder="Fabricante",
            width=159,
            height=27,
            name_field="empresa",
        )
        self._consumption_monthly = FieldFactory.create_number_entry(
            master=self,
            placeholder="Consumo mensal",
            width=159,
            height=27,
            name_field="consumo_mensal",
            max_digits=6,
        )

        self._save_product_button = CTkButton(
            self,
            text="Salvar Alterações",
            fg_color=COLORS.botao_principal,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            command=self._save_callback,
        )
        self._save_product_button.configure(
            width=120,
            height=27,
            corner_radius=5,
        )

        self._cancel_product_button = CTkButton(
            self,
            text="Cancelar",
            fg_color=COLORS.elevado,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            command=self._on_cancel,
        )
        self._cancel_product_button.configure(
            width=69,
            height=27,
            corner_radius=5,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _layout_widgets(self):
        self._title_edit_product.place(x=10, y=4, anchor="nw")
        self._title_edit_product.pack_propagate(False)

        self._name_product_label.place(x=10, y=30, anchor="nw")
        self._name_product_label.pack_propagate(False)
        self._name_product.field.place(x=10, y=55, anchor="nw")

        self._minimun_balance_label.place(x=218, y=30, anchor="nw")
        self._minimun_balance_label.pack_propagate(False)
        self._minimun_balance.field.place(x=218, y=55, anchor="nw")

        self._product_code_chb_label.place(x=426, y=30, anchor="nw")
        self._product_code_chb_label.pack_propagate(False)
        self._product_code_chb.place(x=426, y=55, anchor="nw")

        self._product_firm_label.place(x=10, y=92, anchor="nw")
        self._product_firm_label.pack_propagate(False)
        self._product_firm.field.place(x=10, y=117, anchor="nw")

        self._consumption_monthly_label.place(x=218, y=92, anchor="nw")
        self._consumption_monthly_label.pack_propagate(False)
        self._consumption_monthly.field.place(x=218, y=117, anchor="nw")

        self._save_product_button.place(x=497, y=184, anchor="nw")
        self._save_product_button.pack_propagate(False)
        self._cancel_product_button.place(x=413, y=184, anchor="nw")
        self._cancel_product_button.pack_propagate(False)

    def _populate_fields(self):
        self._set_field_value(self._name_product, self._product_dto.name)
        self._set_field_value(self._minimun_balance, self._product_dto.minimun_balance)
        self._set_field_value(self._product_firm, self._product_dto.product_firm)
        self._set_field_value(self._consumption_monthly, self._product_dto.consumption_monthly)

    @staticmethod
    def _set_field_value(form_field: FormField, value: Any) -> None:
        form_field.field.delete(0, "end")
        form_field.field.insert(0, str(value))

    def _on_cancel(self):
        self._populate_fields()
        self._cancel_callback()

    def get_raw_values(self) -> Dict[str, Any]:
        return {
            "id": self._product_dto.id,
            "name": self._name_product.get(),
            "minimun_balance": self._minimun_balance.get(),
            "product_firm": self._product_firm.get(),
            "product_code_chb": self._product_dto.product_code_chb,
            "consumption_monthly": self._consumption_monthly.get(),
        }
