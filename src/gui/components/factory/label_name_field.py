from customtkinter import CTkLabel
from src.gui.theme.theme import COLORS, FONTS

class LabelNameField():

    @staticmethod
    def create_label_name_field(master, label: str)-> CTkLabel:
        """
        Cria um label com o nome do campo e o texto passado como parâmetro.

        Args:
            master: O widget pai do label.
            label: O texto do label.

        Returns:
            CTkLabel: O label criado.
        """

        label_name_field = CTkLabel(
            master=master,
            text=label,
            font=FONTS.texto_tabela,
            text_color=COLORS.desabilitado
        )

        return label_name_field