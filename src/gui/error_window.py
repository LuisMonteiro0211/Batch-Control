from pathlib import Path

from customtkinter import CTk, CTkButton, CTkFrame, CTkImage, CTkLabel
from PIL import Image

from src.gui.theme import COLORS, FONTS

DEFAULT_MESSAGE = "Erro na aplicação."


class ErrorWindow(CTk):
    """Janela de erro exibida quando a inicialização falha."""

    def __init__(
        self,
        message: str,
        standard_message: str = DEFAULT_MESSAGE,
    ) -> None:
        super().__init__()
        self._detail_message = message
        self._standard_message = standard_message
        self._setup_ui()

    def _setup_ui(self) -> None:
        self._configure_window()
        self._build_widgets()
        self._layout_widgets()

    def _configure_window(self) -> None:
        self.title("Batch Control")
        self.geometry("360x240")
        self.resizable(False, False)
        self.configure(
            fg_color=COLORS.fundo_primario,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _build_widgets(self) -> None:
        icon_path = Path(__file__).parent.parent / "icons" / "circle-x.png"
        icon_image = Image.open(icon_path).convert("RGBA")

        self._icon_ctk = CTkImage(light_image=icon_image, size=(36, 36))
        self._icon_label = CTkLabel(self, text="", image=self._icon_ctk)

        self._title_label = CTkLabel(
            self,
            text=self._standard_message,
            text_color=COLORS.texto_principal,
            font=FONTS.titulo_tela,
            wraplength=300,
            justify="center",
        )

        self._detail_frame = CTkFrame(
            self,
            fg_color=COLORS.fundo_secundario,
            border_width=1,
            border_color=COLORS.bordas,
            corner_radius=6,
        )

        self._detail_label = CTkLabel(
            self._detail_frame,
            text=self._detail_message,
            text_color=COLORS.texto_secundario,
            font=FONTS.subtitulo_menor,
            wraplength=280,
            justify="center",
        )

        self._close_button = CTkButton(
            self,
            text="Fechar",
            width=90,
            height=28,
            corner_radius=5,
            border_width=1,
            border_color=COLORS.bordas,
            fg_color=COLORS.botao_principal,
            hover_color=COLORS.botao_selecionado,
            text_color=COLORS.texto_botao_principal,
            font=FONTS.botao_primario,
            command=self.destroy,
        )

    def _layout_widgets(self) -> None:
        self._icon_label.pack(pady=(24, 8))
        self._title_label.pack(padx=24, pady=(0, 12))
        self._detail_frame.pack(padx=24, fill="x")
        self._detail_label.pack(padx=12, pady=10, fill="x")
        self._close_button.pack(pady=(16, 20))

    def run(self) -> None:
        self.mainloop()


if __name__ == "__main__":
    app = ErrorWindow(message="Erro ao conectar ao banco de dados.")
    app.run()
