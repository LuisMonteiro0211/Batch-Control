from customtkinter import CTkButton, CTkFrame, CTkLabel
from src.exceptions.exceptions import ValidationError
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory
from src.dtos.product_dto import ProductDTO
from src.helpers import is_number, is_valid_string, sanitize_string
from typing import Callable, List, Tuple, Any

class NewProductFrame(CTkFrame):
    def __init__(self, parent, on_click_save_product: Callable):
        super().__init__(parent)
        self._setup_ui()
        self._on_click_save_product = on_click_save_product

    def _setup_ui(self):
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.configure(
            width=389,
            height=207,
            fg_color=COLORS.fundo_secundario,
            corner_radius=10,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _build_widgets(self):
        self._title_new_product = CTkLabel(
            self,
            text="NOVO PRODUTO",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )

        self._name_product_label = CTkLabel(
            self,
            text="Produto",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )

        self._minimun_balance_label = CTkLabel(
            self,
            text="Saldo mínimo",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._product_firm_label = CTkLabel(
            self,
            text="Fabricante",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )
        self._product_code_chb_label = CTkLabel(
            self,
            text="Código CHB",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )

        self._consumption_monthly_label = CTkLabel(
            self,
            text="Consumo mensal",
            text_color=COLORS.desabilitado,
            font=FONTS.texto_tabela
        )

        self._name_product = FieldFactory.create_entry(master=self, placeholder="Nome do produto", width=159, height=27, name_field = "nome_produto")
        self._minimun_balance = FieldFactory.create_number_entry(master=self, placeholder="Saldo mínimo", width=159, height=27, name_field= "saldo_min")
        self._product_firm = FieldFactory.create_entry(master=self, placeholder="Fabricante", width=159, height=27, name_field= "empresa")
        self._product_code_chb = FieldFactory.create_number_entry(master=self, placeholder="Código CHB", width=159, height=27, name_field= "cod_sku", max_digits=6)
        self._consumption_monthly = FieldFactory.create_number_entry(master=self, placeholder="Consumo mensal", width=159, height=27, name_field= "consumo_mensal", max_digits=6)

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

    def _layout_widgets(self):
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

    def get_values_from_frame(self) -> ProductDTO:
        """Método para obter os valores do frame de novo produto.
        
        Args:
            None
        Returns:
            ProductDTO: Objeto DTO com os valores do frame de novo produto.
        """
        list_number_fields = ["minimun_balance", "product_code_chb", "consumption_monthly"]

        list_values: List[Tuple[str, Any]] = [
            ("name", self._name_product.get()),
            ("minimun_balance", self._minimun_balance.get()),
            ("product_firm", self._product_firm.get()),
            ("product_code_chb", self._product_code_chb.get()),
            ("consumption_monthly", self._consumption_monthly.get()),
        ]

        for name_field, value in list_values:
            if not is_valid_string(value=value):
                raise ValidationError(f"O campo {name_field} deve ser uma string válida!")
            if name_field in list_number_fields:
                if not is_number(value=value):
                    raise ValidationError(f"O campo {name_field} deve ser um número!")

        return ProductDTO(
            name=sanitize_string(value=list_values[0][1]),
            minimun_balance=int(list_values[1][1]),
            product_firm=sanitize_string(value=list_values[2][1]),
            product_code_chb=int(list_values[3][1]),
            consumption_monthly=float(list_values[4][1]),

            id=None,
            created_at=None,
            updated_at=None,
        )

    def clear_fields(self):
        """Método para limpar os campos do frame de novo produto.
        
        Args:
            None
        Returns:
            None
        """
        for form_field in (
            self._name_product,
            self._minimun_balance,
            self._product_firm,
            self._product_code_chb,
            self._consumption_monthly,
        ):
            form_field.clear()