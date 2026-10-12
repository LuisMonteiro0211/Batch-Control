"""
Módulo para criação de campos de entrada de texto.

Métodos públicos:
    - create_entry(): Método para criar um campo de entrada de texto.
    - create_data_entry(): Método para criar um campo de entrada de data.

Uso recomendado:
    >>> from src.gui.components.field_factory import FieldFactory
    >>> field_factory = FieldFactory()
    >>> entry = field_factory.create_entry(master, placeholder="Digite seu nome")
    >>> data_entry = field_factory.create_data_entry(master, placeholder="Digite sua data de nascimento")

    >>> entry.pack(pady=20)
    >>> data_entry.pack(pady=20)
"""

from typing import Any, Callable, List, Optional
from customtkinter import CTkEntry, CTkSegmentedButton
from src.gui.theme import COLORS, FONTS
from .form_field import FormField
from src.dtos.product_dto import ProductCardDTO, SearchObjectTransfer
from src.interface.protocols import SearchProductByNameProtocol
from src.exceptions.exceptions import NoSearchValueError


class FieldFactory:
    """
    Classe para criar campos de entrada de texto.
    """
    @staticmethod
    def create_entry(master, placeholder, width=159, height=27) -> FormField:
        """
        Método para criar um campo de entrada de texto.

        Args:
            master: Widget pai do campo de entrada.
            placeholder: Texto de placeholder do campo de entrada.
            width: Largura do campo de entrada.
            height: Altura do campo de entrada.

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
        return FormField(field=entry)

    @staticmethod
    def set_value_entry(entry: CTkEntry, value: Any):
        """
        Método para definir o valor de um campo de entrada de texto.
        Args:
            entry: Campo de entrada de texto.
            value: Valor do campo de entrada.
        Returns:
            None
        """
        entry.delete(0, "end")
        entry.insert(0, value)
    
    @staticmethod
    def create_number_entry(
        master,
        placeholder,
        width=159,
        height=27,
        max_digits: Optional[int] = None,
    ) -> FormField:
        """
        Método para criar um campo de entrada de número.
        Args:
            master: Widget pai do campo de entrada.
            placeholder: Texto de placeholder do campo de entrada.
            width: Largura do campo de entrada.
            height: Altura do campo de entrada.
            max_digits: Limite máximo de dígitos (opcional).
        Returns:
            FormField: Campo de entrada de número encapsulado.
        """
        number_entry = CTkEntry(master=master, placeholder_text=placeholder)
        number_entry.configure(
            width=width,
            height=height,
            corner_radius=5,
            fg_color=COLORS.elevado,
            border_width=1,
            border_color=COLORS.bordas,
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_menor,
        )

        def _just_number(novo_valor):
            """
            Método para validar se o valor digitado é um número.

            Args:
                novo_valor: Valor digitado no campo de entrada. Enviado pelo evento do teclado.
            Returns:
                True se o valor digitado é um número, False caso contrário.
            """

            if novo_valor == placeholder:
                return True

            apenas_numeros = "".join(filter(str.isdigit, novo_valor))
            if novo_valor != apenas_numeros:
                return False
            if max_digits is not None:
                return len(apenas_numeros) <= max_digits
            return True

        validar = master.register(_just_number)
        number_entry.configure(
            validate="key",
            validatecommand=(validar, "%P"),
        )

        return FormField(field=number_entry)

    @staticmethod
    def create_data_entry(master, placeholder, width=159, height=27) -> FormField:
        """
        Método para criar um campo de entrada de data já com formatação.
        Args:
            master: Widget pai do campo de entrada.
            placeholder: Texto de placeholder do campo de entrada.
            width: Largura do campo de entrada.
            height: Altura do campo de entrada.
        Returns:
            FormField: Campo de entrada de data encapsulado.
        """
        form_field = FieldFactory.create_number_entry(
            master, placeholder, width, height, max_digits=8
        )
        date_entry = form_field.field

        def _format_data(event):
            if event.keysym in ("BackSpace", "Delete", "Left", "Right", "Tab"):
                return

            date_number = "".join(filter(str.isdigit, date_entry.get()))

            if isinstance(date_entry, CTkEntry):
                new_date = date_number
                if len(date_number) > 4:
                    new_date = date_number[:2] + "/" + date_number[2:4] + "/" + date_number[4:]
                elif len(date_number) > 2:
                    new_date = date_number[:2] + "/" + date_number[2:]

                if date_entry.get() != new_date:
                    date_entry.delete(0, "end")
                    date_entry.insert(0, new_date)

        date_entry.bind("<KeyRelease>", _format_data)

        return form_field

    @staticmethod
    def create_locked_entry(master, width=159, height=27, value: Optional[str] = None) -> CTkEntry:
        """
        Método para criar um campo de entrada de texto bloqueado.
        Args:
            master: Widget pai do campo de entrada.
            width: Largura do campo de entrada.
            height: Altura do campo de entrada.
            value: Valor do campo de entrada.
        Returns:
            CTkEntry: Campo de entrada de texto bloqueado.
        Exemplo de uso:
        >>> from src.gui.components.factory import FieldFactory
        >>> field_factory = FieldFactory()
        >>> entry = field_factory.create_locked_entry(master, width=159, height=27, value="John Doe")
        >>> entry.pack(pady=20)
        """
        #Esse retorna um CTkEntry e não um FormField pois não tera input de texto.

        entry = CTkEntry(
            master=master,
            width=width,
            height=height,
            corner_radius=5,
            fg_color=COLORS.elevado,
            border_width=1,
            border_color=COLORS.bordas,
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_menor,
        )

        if value is not None:
            entry.insert(0, value)
            entry.configure(state="disabled")
        return entry

    @staticmethod
    def set_value_locked_entry(entry: CTkEntry, value: Any):
        """
        Método para definir o valor de um campo de entrada de texto bloqueado.
        Args:
            entry: Campo de entrada de texto bloqueado.
            value: Valor do campo de entrada.
        Returns:
            None
        """
        entry.configure(state="normal")
        entry.delete(0, "end")
        entry.insert(0, value)
        entry.configure(state="disabled")

    @staticmethod
    def create_search_entry(
        master,
        placeholder,
        search_fn: Optional[SearchProductByNameProtocol] = None,
        trigger_controller: Optional[Callable] = None,
        width=159,
        height=27,
    ) -> FormField:
        """
        Cria um campo de busca com debounce de 300 ms ao digitar.

        A busca só é disparada quando o texto tem 2 ou mais caracteres.

        Args:
            master: Widget pai do campo.
            placeholder: Texto de placeholder.
            search_fn: Função de busca por nome de produto.
            width: Largura do campo.
            height: Altura do campo.

        Returns:
            FormField: Campo de busca encapsulado.
        """
        search_entry = CTkEntry(master=master, placeholder_text=placeholder)
        search_entry.configure(
            width=width,
            height=height,
            corner_radius=5,
            fg_color=COLORS.elevado,
            border_width=1,
            border_color=COLORS.bordas,
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_menor,
        )

        after_id = None # Tem que ficar do lado de fora para persistir o estado/valor da variável
        empty_search_notified = False

        def _search(text: str)-> None:
            """
            Método responsável por fazer a chamada da função de busca por nome de produto do banco de dados

            Args:
                text: Texto digitado no campo de busca.
            Returns:
                Optional[List[ProductCardDTO]]: Lista com as informações para montar o card do produto ou None se não houver produtos com o nome informado.
            """

            nonlocal empty_search_notified

            if search_fn is not None and trigger_controller is not None:
                empty_search_notified = False
                search_values = search_fn(name_product=text)
                search_object = SearchObjectTransfer(
                    product_cards=search_values,
                    text_search=text
                )
                trigger_controller(search_object)
                


        def debounce_search(event):
            """
            Método para buscar o produto.
            Args:
                event: Evento de teclado.
            Returns:
                None
            """
            nonlocal after_id #Impede que a variável seja local no escopo da função
            #O nonlocal é usado para acessar a variável fora da função get_search_value
            nonlocal empty_search_notified


            if event.keysym in ("Left", "Right", "Tab", "Up", "Down"):
                return
            
            search_entry_value = search_entry.get().strip()

            if after_id is not None:
                search_entry.after_cancel(after_id) #Cancela o evento de busca anterior

            if event.keysym == "BackSpace" and search_entry_value == "" and not empty_search_notified:
                """
                Caso o usuário apague o texto do campo de busca
                e acionado o trigger para poder atualizar a lista com os produtos com estoque baixo.
                """
                empty_search_notified = True
                if trigger_controller is not None:
                    search_value = SearchObjectTransfer(
                        product_cards=None,
                        text_search=None
                    )
                    trigger_controller(search_value)
                    return

            if len(search_entry_value) < 2:
                return #Valor muito curto para pesquisa

            after_id = search_entry.after(300, lambda: _search(search_entry_value))
            

        search_entry.bind("<KeyRelease>", debounce_search)


        return FormField(field=search_entry)


    @staticmethod
    def create_segmented_button(master, list_buttons: List[str], width: int, height: int) -> FormField:
        """
        Cria um botão segmentado para seleção entre opções (ex: Ativo/Inativo).

        Args:
            master: Widget pai.
            list_buttons: Lista de opções exibidas no segmento.
            width: Largura do widget.
            height: Altura do widget.

        Returns:
            FormField: Botão segmentado encapsulado.
        """
        segmented_button = CTkSegmentedButton(
            master=master,
            values=list_buttons,
            width=width,
            height=height,
            corner_radius=5,
            fg_color=COLORS.elevado,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.subtitulo_menor,

        )
        return FormField(field=segmented_button)