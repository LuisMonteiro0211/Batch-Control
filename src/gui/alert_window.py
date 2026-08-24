from PIL import Image
from customtkinter import CTk, CTkButton, CTkFrame, CTkImage, CTkLabel

from src.gui.theme import COLORS, FONTS
from src.paths import icon_path

class AlertWindow(CTk):
    def __init__(self, message: str):
        super().__init__()
        self._alert_message = message
        self._setup_ui()


    def _setup_ui(self):
        self._configure_window()
        self._build_widgets()
        self._layout_widgets()

    def _configure_window(self):
        self.title("Alerta")
        self.geometry("360x240")
        self.resizable(False, False)
        self.configure(
            fg_color=COLORS.fundo_primario,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _build_widgets(self):
        icon_image = Image.open(icon_path("triangle-alert.png")).convert("RGBA")

        self._icon_ctk = CTkImage(light_image=icon_image, size=(36, 36))
        self._icon_label = CTkLabel(self, text="", image=self._icon_ctk)

        self._title_label = CTkLabel(
            self,
            text="Alerta",
            text_color=COLORS.texto_principal,
            font=FONTS.titulo_tela,
        )

        self._message_label = CTkLabel(
            self,
            text=self._alert_message,
            text_color=COLORS.texto_principal,
            font=FONTS.botao_primario,
            wraplength=280,
            justify="center",
        )

        self._confirm_button = CTkButton(
            self,
            text="Ok",
            command=self.destroy,
            width=90,
            height=28,
            corner_radius=5,
            border_width=1,
            border_color=COLORS.bordas,
            fg_color=COLORS.botao_principal,
            hover_color=COLORS.botao_selecionado,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
        )

    def _layout_widgets(self):
        self._icon_label.pack(pady=(24, 8))
        self._title_label.pack(padx=24, pady=(0, 12))
        self._message_label.pack(padx=24, pady=(0, 12))
        self._confirm_button.pack(pady=(16, 20))
        
    def run(self) -> None:
        self.mainloop()


if __name__ == "__main__":
    app = AlertWindow(message="Alerta de teste")
    app.run()
        