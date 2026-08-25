"""
Módulo do formulário de cadastro de novo produto.

Métodos públicos:
    - get_raw_values(): Coleta os valores dos campos do formulário.
    - clear_fields(): Limpa todos os campos de entrada.
"""

from customtkinter import CTkButton, CTkFrame, CTkLabel
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory, LabelNameField
from typing import Callable, Dict
from src.forms.product_form_types import NewProductRawData


class NewProductFrame(CTkFrame):
    """
    Formulário para cadastro de um novo produto.

    Args:
        parent: Widget pai (ProductFrame).
        on_click_save_product: Callback executado ao clicar em "Salvar Produto".
    """

    def __init__(self, parent, on_click_save_product: Callable):
        super().__init__(parent)
        self._on_click_save_product = on_click_save_product
        self._setup_ui()

    def _setup_ui(self) -> None:
        """Configura layout, cria widgets e posiciona na tela."""
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self) -> None:
        """Define dimensões, cores e borda do frame."""
        self.configure(
            width=389,
            height=207,
            fg_color=COLORS.fundo_secundario,
            corner_radius=10,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _build_widgets(self) -> None:
        """Cria labels, campos de entrada e botões de ação."""
        self._title_new_product = CTkLabel(
            self,
            text="NOVO PRODUTO",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )

        self._name_product_label = LabelNameField.create_label_name_field(self, "Produto")
        self._minimun_balance_label = LabelNameField.create_label_name_field(self, "Saldo mínimo")
        self._product_firm_label = LabelNameField.create_label_name_field(self, "Fabricante")
        self._product_code_chb_label = LabelNameField.create_label_name_field(self, "Código CHB")
        self._consumption_monthly_label = LabelNameField.create_label_name_field(self, "Consumo mensal")

        self._name_product = FieldFactory.create_entry(master=self, placeholder="Nome do produto", width=159, height=27)
        self._minimun_balance = FieldFactory.create_number_entry(master=self, placeholder="Saldo mínimo", width=159, height=27)
        self._product_firm = FieldFactory.create_entry(master=self, placeholder="Fabricante", width=159, height=27)
        self._product_code_chb = FieldFactory.create_number_entry(master=self, placeholder="Código CHB", width=159, height=27, max_digits=6)
        self._consumption_monthly = FieldFactory.create_number_entry(master=self, placeholder="Consumo mensal", width=159, height=27, max_digits=6)

        self._save_product_button = CTkButton(
            self,
            text="Salvar Produto",
            fg_color=COLORS.botao_principal,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            command=self._on_click_save_product
        )
        self._save_product_button.configure(
            width=110,
            height=27,
            corner_radius=5,
        )

        self._cancel_product_button = CTkButton(
            self,
            text="Cancelar",
            fg_color=COLORS.elevado,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            command=self.clear_fields
        )
        self._cancel_product_button.configure(
            width=69,
            height=27,
            corner_radius=5,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _layout_widgets(self) -> None:
        """Posiciona os widgets na tela."""
        self._title_new_product.place(x=10, y=4, anchor="nw")
        self._title_new_product.pack_propagate(False)
        self._name_product_label.place(x=10, y=30, anchor="nw")
        self._name_product_label.pack_propagate(False)
        self._name_product.field.place(x=10, y=55, anchor="nw")

        self._product_firm_label.place(x=10, y=92, anchor="nw")
        self._product_firm_label.pack_propagate(False)
        self._product_firm.field.place(x=10, y=117, anchor="nw")

        self._minimun_balance_label.place(x=218, y=30, anchor="nw")
        self._minimun_balance_label.pack_propagate(False)
        self._minimun_balance.field.place(x=218, y=55, anchor="nw")

        self._product_code_chb_label.place(x=218, y=92, anchor="nw")
        self._product_code_chb_label.pack_propagate(False)
        self._product_code_chb.field.place(x=218, y=117, anchor="nw")

        self._consumption_monthly_label.place(x=10, y=145, anchor="nw")
        self._consumption_monthly_label.pack_propagate(False)
        self._consumption_monthly.field.place(x=10, y=170, anchor="nw")

        self._save_product_button.place(x=267, y=167, anchor="nw")
        self._save_product_button.pack_propagate(False)
        self._cancel_product_button.place(x=183, y=167, anchor="nw")
        self._cancel_product_button.pack_propagate(False)

    def get_raw_values(self) -> NewProductRawData:
        """
        Coleta os valores atuais de todos os campos.

        Returns:
            NewProductRawData com os valores coletados dos campos do formulário.
        """
        return NewProductRawData(
            nome_produto=self._name_product.get(),
            empresa=self._product_firm.get(),
            saldo_min=self._minimun_balance.get(),
            cod_sku=self._product_code_chb.get(),
            consumo_mensal=self._consumption_monthly.get()
        )

    def clear_fields(self) -> None:
        """Limpa o conteúdo de todos os campos de entrada."""
        for form_field in (
            self._name_product,
            self._minimun_balance,
            self._product_firm,
            self._product_code_chb,
            self._consumption_monthly,
        ):
            form_field.clear()
