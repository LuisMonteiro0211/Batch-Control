from enum import Enum
from dataclasses import dataclass
from pathlib import Path
from typing import Dict

from PIL import Image
from customtkinter import CTkButton, CTkFrame, CTkImage, CTkLabel, CTkToplevel

from src.gui.theme.theme import COLORS, FONTS
from src.paths import icon_path

class DialogType(Enum):
    ALERT = "alert"
    CONFIRM = "confirm"
    ERROR = "error"
    SUCCESS = "success"

@dataclass(frozen=True)
class DialogSpec:
    icon_path: Path
    header: str
    button_text: str

TYPES: Dict[DialogType, DialogSpec] = {
    DialogType.ALERT: DialogSpec(
        icon_path=icon_path("triangle-alert.png"),
        header="Alerta",
        button_text="Ok"
    ),

    DialogType.CONFIRM: DialogSpec(
        icon_path=icon_path("check.png"),
        header="Confirmação",
        button_text="Sim"
    ),

    DialogType.ERROR: DialogSpec(
        icon_path=icon_path("circle-x.png"),
        header="Erro",
        button_text="Ok"
    ),

    DialogType.SUCCESS: DialogSpec(
        icon_path=icon_path("check.png"),
        header="Sucesso",
        button_text="Ok"
    ),
}

class InteractionWindow(CTkToplevel):
    def __init__(self, master, spec: DialogSpec, message: str):
        super().__init__(master)
        self._spec = spec
        self._message = message
        self._action = False
        self._master = master
        self._setup_ui()
        self.update_idletasks()
        self.grab_set()
        self.wait_window()

    def _setup_ui(self):
        self._configure_window()
        self._build_widgets()
        self._layout_widgets()
    
    def _configure_window(self):
        self.title(self._spec.header)
        self.geometry("360x240")
        self.resizable(False, False)
        self.configure(
            fg_color=COLORS.fundo_primario,
            border_width=1,
            border_color=COLORS.bordas
        )
        self.transient(self._master)


    def _on_click_button(self):
        self._action = True
        self.destroy()

    def _build_widgets(self):
        self._icon = Image.open(self._spec.icon_path).convert("RGBA")
        self._icon_ctk = CTkImage(self._icon, size=(36,36))
        self._icon_label = CTkLabel(self, image=self._icon_ctk, text="")


        self._title_label = CTkLabel(
            self, 
            text=self._spec.header,
            text_color=COLORS.texto_principal,
            font=FONTS.titulo_tela,
            wraplength=300,
            justify="center"
            )

        self._detail_frame = CTkFrame(
            self,
            width=288,
            height=14,
            fg_color=COLORS.fundo_secundario,
            border_width=1,
            border_color=COLORS.bordas,
            corner_radius=6
        )

        self._detail_label = CTkLabel(
            self._detail_frame,
            width=288,
            height=14,
            text=self._message,
            text_color=COLORS.texto_secundario,
            font=FONTS.subtitulo_menor,
            wraplength=280,
            justify="center",
        )

        self._button_action = CTkButton(
            self,
            text=self._spec.button_text,
            width=90,
            height=28,
            corner_radius=5,
            border_width=1,
            border_color=COLORS.bordas,
            fg_color=COLORS.botao_principal,
            hover_color=COLORS.botao_selecionado,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            command=self._on_click_button
        )

    def _layout_widgets(self):
        self._icon_label.pack(pady=(24, 8))
        self._title_label.pack(padx=24, pady=(0, 12))
        self._detail_frame.pack(padx=24, fill="x")
        self._detail_label.pack(padx=12, pady=10, fill="x")
        self._button_action.pack(pady=(16, 20))

        
    def get_action(self):
        return self._action


class FactoryInteractionWindow:
    @staticmethod
    def alert_window(master, message: str) -> InteractionWindow:
        return InteractionWindow(
            master=master, 
            spec=TYPES[DialogType.ALERT], 
            message=message)

    @staticmethod
    def error_window(master, message: str) -> InteractionWindow:
        return InteractionWindow(
            master=master,
            spec=TYPES[DialogType.ERROR],
            message=message
        )

    @staticmethod
    def confirm_window(master, message: str) -> InteractionWindow:
        return InteractionWindow(
            master=master,
            spec=TYPES[DialogType.CONFIRM],
            message=message
        )

    @staticmethod
    def success_window(master, message: str) -> InteractionWindow:
        return InteractionWindow(
            master=master,
            spec=TYPES[DialogType.SUCCESS],
            message=message
        )