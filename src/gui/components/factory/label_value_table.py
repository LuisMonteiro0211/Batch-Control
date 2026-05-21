from customtkinter import CTkLabel
from src.gui.theme.theme import COLORS, FONTS

class LabelValueTable():

    @staticmethod
    def create_label_value_table(master, label):
        label_value_table = CTkLabel(
            master,
            text=label,
            text_color=COLORS.texto_secundario,
            font=FONTS.texto_tabela,
            fg_color=COLORS.transparente
        )
        return label_value_table