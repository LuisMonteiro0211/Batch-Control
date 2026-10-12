from typing import Callable
from customtkinter import CTkToplevel, CTkCheckBox, BooleanVar
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import LabelNameField
from src.gui.components.primary_action_button import PrimaryActionButton

class TopLevelFilter(CTkToplevel):
    def __init__(self, master, status, callback: Callable[[bool], None]):
        self._master = master
        self._status = status
        self._callback = callback
        super().__init__(master)
        self._setup_ui()

    def _setup_ui(self):
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _get_status_check_box(self):
        status = self._check_box.get()

        if status == 1:
            return True
        else:
            return False


    def _configure_layout(self) -> None:
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
        self._close_button.place(x=59, y=98)
        self._check_box.place(x=15, y=18)

    def _close_top_level(self):
        self._callback(self._get_status_check_box())
        self.destroy()