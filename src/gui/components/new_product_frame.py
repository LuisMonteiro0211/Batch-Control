from customtkinter import CTkButton, CTkFont, CTkFrame, CTkLabel
from src.gui.theme import COLORS
from src.gui.theme.theme import FONTS
from src.gui.components.field_factory import FieldFactory

class NewProductFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.configure(
            width=357,
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
            font=CTkFont(family=FONTS.texto_tabela, size=12, weight="normal")
        )

        self._name_product_label = CTkLabel(
            self,
            text="Produto",
            text_color=COLORS.desabilitado,
            font=CTkFont(family=FONTS.texto_tabela, size=12, weight="normal")
        )

        self._minimun_balance_label = CTkLabel(
            self,
            text="Saldo mínimo",
            text_color=COLORS.desabilitado,
            font=CTkFont(family=FONTS.texto_tabela, size=12, weight="normal")
        )
        self._product_firm_label = CTkLabel(
            self,
            text="Fabricante",
            text_color=COLORS.desabilitado,
            font=CTkFont(family=FONTS.texto_tabela, size=12, weight="normal")
        )
        self._product_code_chb_label = CTkLabel(
            self,
            text="Código CHB",
            text_color=COLORS.desabilitado,
            font=CTkFont(family=FONTS.texto_tabela, size=12, weight="normal")
        )

        self._name_product = FieldFactory.create_entry(master=self, placeholder="Nome do produto")
        self._minimun_balance = FieldFactory.create_entry(master=self, placeholder="Saldo mínimo")
        self._product_firm = FieldFactory.create_entry(master=self, placeholder="Fabricante")
        self._product_code_chb = FieldFactory.create_entry(master=self, placeholder="Código CHB")

        self._save_product_button = CTkButton(
            self,
            text="Salvar Produto",
            fg_color=COLORS.botao_principal,
            text_color=COLORS.texto_botao_principal,
            font=CTkFont(family=FONTS.botao_primario, size=13, weight="normal"),
            command=None
        )
        self._save_product_button.configure(
            width=110,
            height=27,
            corner_radius=5,
        )


    def _layout_widgets(self):
        self._title_new_product.place(x=10, y=4, anchor="nw")
        self._title_new_product.pack_propagate(False)

        self._name_product_label.place(x=10, y=30, anchor="nw")
        self._name_product_label.pack_propagate(False)
        self._name_product.place(x=10, y=55, anchor="nw")
        self._name_product.pack_propagate(False)

        self._product_firm_label.place(x=10, y=92, anchor="nw")
        self._product_firm_label.pack_propagate(False)
        self._product_firm.place(x=10, y=117, anchor="nw")
        self._product_firm.pack_propagate(False)

        self._minimun_balance_label.place(x=183, y=30, anchor="nw")
        self._minimun_balance_label.pack_propagate(False)
        self._minimun_balance.place(x=183, y=55, anchor="nw")
        self._minimun_balance.pack_propagate(False)

        self._product_code_chb_label.place(x=183, y=92, anchor="nw")
        self._product_code_chb_label.pack_propagate(False)
        self._product_code_chb.place(x=186, y=117, anchor="nw")
        self._product_code_chb.pack_propagate(False)

        self._save_product_button.place(x=232, y=167, anchor="nw")
        self._save_product_button.pack_propagate(False)

        self._cancel_product_button.place(x=148, y=167, anchor="nw")
        self._cancel_product_button.pack_propagate(False)

    def get_values_from_frame(self):
        """Método para obter os valores do frame de novo produto.
        
        Args:
            None
        Returns:
            dict: DTO com os valores do frame de novo produto.
        """
        pass