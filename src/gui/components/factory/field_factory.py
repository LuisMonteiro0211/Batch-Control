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


from customtkinter import CTkEntry, CTkTextbox, StringVar
from src.gui.theme import COLORS, FONTS
from .form_field import FormField

class FieldFactory:
    """
    Classe para criar campos de entrada de texto.
    """
    @staticmethod
    def create_entry(master, placeholder, width=159, height=27, name_field: str = None) -> FormField:
        """
        Método para criar um campo de entrada de texto.

        Args:
            master: Widget pai do campo de entrada.
            placeholder: Texto de placeholder do campo de entrada.
            width: Largura do campo de entrada.
            height: Altura do campo de entrada.
            name_field: Nome do campo de entrada.

        Returns:
            FormField: Campo de entrada de texto encapsulado.
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
        return FormField(name_field=name_field, field=entry)
        
    @staticmethod
    def create_data_entry(master, placeholder, width=159, height=27, name_field: str = None) -> FormField:
        """
        Método para criar um campo de entrada de data já com formatação.
        Args:
            master: Widget pai do campo de entrada.
            placeholder: Texto de placeholder do campo de entrada.
            width: Largura do campo de entrada.
            height: Altura do campo de entrada.
            name_field: Nome do campo de entrada.
        Returns:
            FormField: Campo de entrada de data encapsulado.
        """
        date_entry = CTkEntry(master=master, placeholder_text=placeholder)
        date_entry.configure(
            width=width,
            height=height,
            corner_radius=5,
            fg_color=COLORS.elevado,
            border_width=1,
            border_color=COLORS.bordas,
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_menor,
        )

        def _limitar(novo_valor):
            apenas_numeros = "".join(filter(str.isdigit, novo_valor))
            return len(apenas_numeros) <= 8

        validar = master.register(_limitar)
        date_entry.configure(
        validate="key",
        validatecommand=(validar, "%P"))

        def _format_data(event):
            """
            Método para formatar a data de entrada de texto.
            Args:
                event: Evento de teclado.
            Returns:
                None
            """
            # Ignora teclas de navegação/controle para não quebrar o cursor
            if event.keysym in ("BackSpace", "Delete", "Left", "Right", "Tab"):
                return

            date = date_entry.get()

            # Extrai só os dígitos e limita a 8 (DDMMAAAA)
            date_number = "".join(filter(str.isdigit, date))

            # Reconstrói a string com as barras
            new_date = date_number
            if len(date_number) > 4:
                new_date = date_number[:2] + "/" + date_number[2:4] + "/" + date_number[4:]
            elif len(date_number) > 2:
                new_date = date_number[:2] + "/" + date_number[2:]

            # Atualiza o campo só se mudou
            if date_entry.get() != new_date:
                date_entry.delete(0, "end")
                date_entry.insert(0, new_date)

        # Vincula a função ao evento de tecla solta
        date_entry.bind("<KeyRelease>", _format_data)

        return FormField(name_field=name_field, field=date_entry)

    @staticmethod
    def create_locked_entry(master, label, value)-> CTkEntry:
        pass