"""
Módulo do formulário de edição de produto.

Exibe campos editáveis (nome, empresa, saldo mínimo, status) e campos
somente leitura (consumo, SKU, datas) preenchidos a partir do ProductDTO.

Métodos públicos:
    - get_raw_values(): Coleta os valores dos campos editáveis.
    - set_data_product_dto(): Preenche todos os campos com os dados do DTO.
"""

from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel, CTkSegmentedButton
from src.dtos import ProductDTO
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory, LabelNameField
from typing import Callable
from src.forms.product_form_types import EditProductRawData
PRIMEIRA_MARGEM_LABEL, SEGUNDA_MARGEM_LABEL, TERCEIRA_MARGEM_LABEL = 24, 230, 436
PRIMEIRA_LINHA_LABEL, SEGUNDA_LINHA_LABEL, TERCEIRA_LINHA_LABEL = 24, 87, 150

PRIMEIRA_MARGEM_CAMPO, SEGUNDA_MARGEM_CAMPO, TERCEIRA_MARGEM_CAMPO = 24, 230, 436
PRIMEIRA_LINHA_CAMPO, SEGUNDA_LINHA_CAMPO, TERCEIRA_LINHA_CAMPO = 48, 111, 174


class EditProductFrame(CTkFrame):
    """
    Formulário de edição de um produto existente.

    Args:
        parent: Widget pai (ProductFrame).
        product_dto: Dados do produto a ser editado.
        save_callback: Função chamada ao clicar em "Salvar Alterações".
        cancel_callback: Função chamada ao clicar em "Cancelar".
    """

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

    def _setup_ui(self) -> None:
        """Configura layout, cria widgets e posiciona na tela."""
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self) -> None:
        """Define dimensões, cores e borda do frame."""
        self.configure(
            width=619,
            height=224,
            fg_color=COLORS.fundo_secundario,
            corner_radius=10,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _build_widgets(self) -> None:
        """Cria labels, campos editáveis, campos bloqueados e botões."""
        self._title_edit_product = CTkLabel(
            self,
            text="EDITAR PRODUTO",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela,
        )

        self._name_product_label = LabelNameField.create_label_name_field(self, "Produto")
        self._firm_label = LabelNameField.create_label_name_field(master=self, label="Empresa")
        self._consumption_monthly_label = LabelNameField.create_label_name_field(master=self, label="Consumo Médio")
        self._minimun_balance_label = LabelNameField.create_label_name_field(master=self, label="Saldo Mínimo")
        self._sku_code_label = LabelNameField.create_label_name_field(master=self, label="Código CHB")
        self._status_label = LabelNameField.create_label_name_field(master=self,label="Status do Produto")
        self._date_creation_label = LabelNameField.create_label_name_field(master=self, label="Data de Cadastro")
        self._date_update_label = LabelNameField.create_label_name_field(master=self, label="Atualizado em")

        self._name_product_field = FieldFactory.create_entry(master=self, placeholder="", width=159, height=27)
        self._firm_field = FieldFactory.create_entry(master=self, placeholder="", width=159, height=27)
        self._minimun_balance_field = FieldFactory.create_number_entry(master=self, placeholder="", width=159, height=27)
        self._status_segmented_button = FieldFactory.create_segmented_button(master=self, list_buttons=["Ativo", "Inativo"], width=159, height=27)

        self._consumption_monthly_field = FieldFactory.create_locked_entry(master=self, value=None, width=159, height=27)
        self._sku_code_field = FieldFactory.create_locked_entry(master=self, value=None, width=159,
        height=27)
        self._date_creation_field = FieldFactory.create_locked_entry(master=self, width=159, height=27, value=None)
        self._date_update_field = FieldFactory.create_locked_entry(master=self, width=159, height=27, value=None)

        self._save_button = CTkButton(master=self, text="Salvar Alterações", command=self._save_callback, width=126, height=27, fg_color=COLORS.botao_principal, text_color=COLORS.texto_botao_principal, font=FONTS.botao_primario, corner_radius=5, border_width=1)

        self._cancel_button = CTkButton(master=self, text="Cancelar", command=self._cancel_callback, width=69, height=27, fg_color=COLORS.elevado, hover_color=COLORS.botao_selecionado, text_color=COLORS.texto_botao_principal, font=FONTS.texto_tabela, corner_radius=5, border_width=1, border_color=COLORS.bordas)

    def _layout_widgets(self) -> None:
        """Posiciona labels, campos e botões usando coordenadas fixas."""
        self._name_product_label.place(x=PRIMEIRA_MARGEM_LABEL, y=PRIMEIRA_LINHA_LABEL)
        self._firm_label.place(x=PRIMEIRA_MARGEM_LABEL, y=SEGUNDA_LINHA_LABEL)
        self._consumption_monthly_label.place(x=PRIMEIRA_MARGEM_LABEL, y=TERCEIRA_LINHA_LABEL)
        self._minimun_balance_label.place(x=SEGUNDA_MARGEM_LABEL, y=PRIMEIRA_LINHA_LABEL)
        self._sku_code_label.place(x=SEGUNDA_MARGEM_LABEL, y=SEGUNDA_LINHA_LABEL)
        self._status_label.place(x=SEGUNDA_MARGEM_LABEL, y=TERCEIRA_LINHA_LABEL)
        self._date_creation_label.place(x=TERCEIRA_MARGEM_LABEL, y=PRIMEIRA_LINHA_LABEL)
        self._date_update_label.place(x=TERCEIRA_MARGEM_LABEL, y=SEGUNDA_LINHA_LABEL)

        self._name_product_field.field.place(x=PRIMEIRA_MARGEM_CAMPO, y=PRIMEIRA_LINHA_CAMPO)
        self._firm_field.field.place(x=PRIMEIRA_MARGEM_CAMPO, y=SEGUNDA_LINHA_CAMPO)
        self._consumption_monthly_field.place(x=PRIMEIRA_MARGEM_CAMPO, y=TERCEIRA_LINHA_CAMPO)
        self._minimun_balance_field.field.place(x=SEGUNDA_MARGEM_CAMPO, y=PRIMEIRA_LINHA_CAMPO)
        self._sku_code_field.place(x=SEGUNDA_MARGEM_CAMPO, y=SEGUNDA_LINHA_CAMPO)
        self._status_segmented_button.field.place(x=SEGUNDA_MARGEM_CAMPO, y=TERCEIRA_LINHA_CAMPO)
        self._date_creation_field.place(x=TERCEIRA_MARGEM_CAMPO, y=PRIMEIRA_LINHA_CAMPO)
        self._date_update_field.place(x=TERCEIRA_MARGEM_CAMPO, y=SEGUNDA_LINHA_CAMPO)

        self._save_button.place(x=481, y=180, anchor="nw")
        self._cancel_button.place(x=405, y=180, anchor="nw")

    def get_raw_values(self) -> EditProductRawData:
        """
        Coleta os valores atuais dos campos editáveis.

        Returns:
            EditProductRawData com os valores digitados.
        """
        return EditProductRawData(
            nome_produto=self._name_product_field.get(),
            empresa=self._firm_field.get(),
            saldo_min=self._minimun_balance_field.get(),
            ativo=self._status_segmented_button.get(),
        )

    def set_data_product_dto(self) -> None:
        """
        Preenche todos os campos do formulário com os dados do ProductDTO.

        Campos editáveis recebem valor via set_value_entry; campos bloqueados
        e o segmented button de status são preenchidos separadamente.
        """
        list_editable_fields = [
            self._name_product_field,
            self._firm_field,
            self._minimun_balance_field,
        ]
        list_values = [
            self._product_dto.name,
            self._product_dto.product_firm,
            self._product_dto.minimun_balance,
        ]

        for index, editable_field in enumerate(list_editable_fields):
            if type(editable_field.field) == CTkEntry:
                FieldFactory.set_value_entry(
                    entry=editable_field.field,
                    value=str(list_values[index]))

        FieldFactory.set_value_locked_entry(
            entry=self._consumption_monthly_field,
            value=str(self._product_dto.consumption_monthly)
        )

        FieldFactory.set_value_locked_entry(
            entry=self._sku_code_field,
            value=str(self._product_dto.product_code_chb)
        )

        FieldFactory.set_value_locked_entry(
            entry=self._date_creation_field,
            value=str(self._product_dto.created_at)
        )

        FieldFactory.set_value_locked_entry(
            entry=self._date_update_field,
            value=str(self._product_dto.updated_at)
        )

        if type(self._status_segmented_button.field) == CTkSegmentedButton:
            status = "Ativo" if self._product_dto.product_status == 1 else "Inativo"
            self._status_segmented_button.field.set(status)
