"""
Módulo da janela (Toplevel) de filtros da busca de produtos.

Exibe um checkbox para incluir ou não os produtos bloqueados na busca e
devolve o resultado ao chamador por meio de um callback ao fechar.
"""

from typing import Callable
from customtkinter import CTkToplevel, CTkCheckBox, BooleanVar
from src.gui.theme import COLORS, FONTS
from src.gui.components.primary_action_button import PrimaryActionButton

class TopLevelFilter(CTkToplevel):
    """
    Janela de filtros da busca de produtos.

    Args:
        master: Widget pai da janela.
        status: Estado inicial do filtro (True inclui produtos bloqueados).
        callback: Função chamada ao fechar, recebendo o novo status (bool) do filtro.
    """
    def __init__(self, master, status, callback: Callable[[bool], None]):
        self._master = master
        self._status = status
        self._callback = callback
        super().__init__(master)
        self._setup_ui()

    def _setup_ui(self):
        """Configura o layout e constrói/posiciona os widgets da janela."""
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _get_status_check_box(self):
        """
        Lê o estado atual do checkbox.

        Returns:
            bool: True se o checkbox estiver marcado, False caso contrário.
        """
        status = self._check_box.get()

        if status == 1:
            return True
        else:
            return False


    def _configure_layout(self) -> None:
        """Define título, tamanho, cores e comportamento modal da janela."""
        self.title("Filtros")
        self.geometry("220x140")
        self.resizable(False, False)
        self.configure(
            fg_color=COLORS.fundo_primario,
            border_width =1,
            border_color=COLORS.bordas
        )
        self.transient(self._master)


    def _build_widgets(self):
        """Cria o checkbox de produtos bloqueados e o botão de fechar."""
        var = BooleanVar(value=self._status)
        self._close_button = PrimaryActionButton(
            master=self,
            text="Fechar",
            command=self._close_top_level,
            height=27,
            width=110
        )

        self._check_box = CTkCheckBox(
            master=self,
            width=16,
            height=16,
            text='Produtos Bloqueados',
            variable=var
        )

    def _layout_widgets(self) -> None:
        """Posiciona o checkbox e o botão de fechar na janela."""
        self._close_button.place(x=59, y=98)
        self._check_box.place(x=15, y=18)

    def _close_top_level(self):
        """Envia o status do filtro pelo callback e fecha a janela."""
        self._callback(self._get_status_check_box())
        self.destroy()