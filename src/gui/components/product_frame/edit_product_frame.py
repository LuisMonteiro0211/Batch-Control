from customtkinter import CTkButton, CTkEntry, CTkFrame, CTkLabel
from src.dtos import ProductDTO
from src.gui.theme.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory, LabelNameField, FormField
from typing import Any, Callable, Dict, List, Tuple


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

        #Criação de labels
        self._name_product_label = LabelNameField.create_label_name_field(self, "Produto")
        self._firm_label = LabelNameField.create_label_name_field(master=self, label="Empresa")
        self._consumption_monthly_label = LabelNameField.create_label_name_field(master=self, label="Consumo Médio")
        self._minimun_balance_label = LabelNameField.create_label_name_field(master=self, label="Saldo Mínimo")
        self._sku_code_label = LabelNameField.create_label_name_field(master=self, label="Código CHB")
        self._status_label = LabelNameField.create_label_name_field(master=self,label="Status do Produto")
        self._date_creation_label = LabelNameField.create_label_name_field(master=self, label="Data de Cadastro")
        self.date_update_label = LabelNameField.create_label_name_field(master=self, label="Atualizado em")

        #Criaçõ dos campos
        self._name_product_field = FieldFactory.create_entry(master=self, placeholder="", width=159, height=27, name_field="nome_produto")
        self._firm_field = FieldFactory.create_entry(master=self, placeholder="", width=159, height=27, name_field="empresa")
        self._minimun_balance_field = FieldFactory.create_number_entry(master=self, placeholder="", width=159, height=27, name_field="consumo_mensal")
        self._status_segmented_button = FieldFactory.create_segmented_button(master=self, list_buttons=["Ativo", "Inativo"], width=159, height=27, name_field="ativo")

        #Campos bloqueados
        self._consumption_monthly_field = FieldFactory.create_locked_entry(master=self, value=None, width=159, height=27)
        self._sku_code_field = FieldFactory.create_locked_entry(master=self, value=None, width=159,
        height=27)
        self._date_creation_field = FieldFactory.create_locked_entry(master=self, width=159, height=27, value=None)
        self.date_update_field = FieldFactory.create_locked_entry(master=self, width=159, height=27, value=None)

        #Criação dos botões
        self._save_button = CTkButton(master=self, text="Salvar Alterações", command=self._save_callback, width=126, height=27, fg_color=COLORS.botao_principal, hover_color=COLORS.botao_selecionado, text_color=COLORS.botao_principal, font=FONTS.botao_primario, corner_radius=5, border_width=5)

        self._cancel_button = CTkButton(master=self, text="Cancelar", command=self._cancel_callback, width=126, height=27, fg_color=COLORS.elevado, hover_color=COLORS.botao_selecionado, text_color=COLORS.botao_principal, font=FONTS.texto_tabela, corner_radius=5, border_width=5, border_color=COLORS.bordas)

    def _get_editable_fields(self)-> List[FormField]:
        return [
            self._name_product_field,
            self._firm_field,
            self._minimun_balance_field,
            self._status_segmented_button
        ]

    def get_raw_values(self)-> Dict[str, str]:
        """
        Método para obter os valores dos campos editáveis.
        Args:
            None
        Returns:
            Dict[str, str]: Dicionário com os valores dos campos editáveis.
        """
        return {
            field.name_field: field.get() for field in self._get_editable_fields()
        }


    def set_date_product_dto(self):
        """
        Função para setar os valores do frame de edição com os valores do produto.
        """

        #Setando os valores dos campos editáveis
        list_editable_fields = [
            self._name_product_field,
            self._firm_field,
            self._minimun_balance_field,
            #self._status_segmented_button,
        ]
        #Listando os valores dos campos editáveis
        list_values = [
            self._product_dto.name,
            self._product_dto.product_firm,
            self._product_dto.minimun_balance,
            #self._product_dto.status,
        ]

        for index, editable_field in enumerate(list_editable_fields):
            if type(editable_field.field) == CTkEntry:
                FieldFactory.set_value_entry(
                    entry=editable_field.field,
                    value=str(list_values[index]))

        #Setando os valores dos campos bloqueados
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
            entry=self.date_update_field,
            value=str(self._product_dto.updated_at)
        )