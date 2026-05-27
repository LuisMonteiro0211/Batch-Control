"""
Módulo para criação de campos de entrada de texto.

Métodos públicos:
    - create_entry(): Método para criar um campo de entrada de texto.
    - create_data_entry(): Método para criar um campo de entrada de data.
    - create_locked_entry(): Método para criar um campo de entrada de texto bloqueado.

Uso recomendado:
    >>> from src.gui.components.field_factory import FieldFactory
    >>> field_factory = FieldFactory()
    >>> entry = field_factory.create_entry(master, placeholder="Digite seu nome")
    >>> data_entry = field_factory.create_data_entry(master, placeholder="Digite sua data de nascimento")
    >>> locked_entry = field_factory.create_locked_entry(master, label="Nome", value="John Doe")

    >>> entry.pack(pady=20)
    >>> data_entry.pack(pady=20)
    >>> locked_entry.pack(pady=20)
"""


from customtkinter import CTkEntry, CTkTextbox
from src.gui.theme import COLORS, FONTS

class FieldFactory:
    """
    Classe para criar campos de entrada de texto.
    """
    @staticmethod
    def create_entry(master, placeholder, width=159, height=27) -> CTkEntry:
        """
        Método para criar um campo de entrada de texto.

        Args:
            master: Widget pai do campo de entrada.
            placeholder: Texto de placeholder do campo de entrada.
            width: Largura do campo de entrada.
            height: Altura do campo de entrada.

        Returns:
            CTkEntry: Campo de entrada de texto.
        """
        entry = CTkEntry(master=master, placeholder_text=placeholder)
        entry.configure(
            width=width,
            height=height,
            corner_radius=5,
            fg_color=COLORS.elevado,
            border_width=1,
            border_color=COLORS.bordas,
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_menor,
        )
        return entry
    @staticmethod
    def create_data_entry(master, placeholder, width=159, height=27) -> CTkEntry:
        """
        Método para criar um campo de entrada de data já com formatação.
        Args:
            master: Widget pai do campo de entrada.
            placeholder: Texto de placeholder do campo de entrada.
            width: Largura do campo de entrada.
            height: Altura do campo de entrada.
        Returns:
            CTkEntry: Campo de entrada de data.
        """
        data_entry = CTkEntry(master=master, placeholder_text=placeholder)
        data_entry.configure(
            width=width,
            height=height,
            corner_radius=5,
            fg_color=COLORS.elevado,
            border_width=1,
            border_color=COLORS.bordas,
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_menor,
        )
        def format_data(event):
            """
            Método para formatar a data de entrada de texto.
            Args:
                event: Evento de teclado.
            Returns:
                None
            """
            data = data_entry.get()

            number = "".join(filter(str.isdigit, data))
            number = number[:9]

            if len(number) == 2:
                number += "/"
            elif len(number) == 5:
                number += "/"

            data_entry.delete(0, "end")
            data_entry.insert(0, number)

        data_entry.bind("<KeyRelease>", format_data)

        return data_entry

    @staticmethod
    def create_locked_entry(self, master, label, value)-> CTkEntry:
        pass