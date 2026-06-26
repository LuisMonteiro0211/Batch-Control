from pathlib import Path
from typing import Optional
from customtkinter import CTk, CTkImage, CTkLabel, CTkProgressBar
from PIL import Image
from src.exceptions import BatchControlError
from src.gui.theme import COLORS, FONTS
from src.bootstrap.loader import Loader
from src.bootstrap import AppContext

class SplashScreen(CTk):
    def __init__(self):
        super().__init__()
        self._icon_image = CTkImage(
            light_image=Image.open(Path(__file__).parent.parent / "icons" /
            "brach_ctrl_logo_transparent.png").convert("RGBA"),
            size=(120, 53)
        )
        self._setup_ui()
        self._loader: Loader = Loader(on_progress=self._on_progress)
        self.context: Optional[AppContext] = None
        self.after(100, self.start)
        self._error: Optional[BatchControlError] = None

    def _setup_ui(self):
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.geometry("320x150")
        self.title("Batch Control")
        self.resizable(False, False)
        self.configure(fg_color=COLORS.fundo_primario)

    def _build_widgets(self):
        self._icon_label = CTkLabel(
            self,
            image=self._icon_image,
            text="",
        )
        self._status_label = CTkLabel(
            self,
            text="Iniciando aplicação...",
            text_color=COLORS.texto_principal,
            font=FONTS.valor
        )

        self._progress_bar = CTkProgressBar(
            self,
            width=260,
            progress_color=COLORS.botao_principal,
        )

        self._progress_bar.set(0)

    def _layout_widgets(self):
        padx = 30
        self._progress_bar.pack(side="bottom", fill="x", padx=padx, pady=(0, 12))
        self._status_label.pack(side="bottom", pady=(0, 4))
        self._icon_label.pack(side="top", pady=(25, 8))

    def _on_progress(self, message: str, progress: float):
        self._status_label.configure(text=message)
        self._progress_bar.set(progress)
        self.update()
        
    #================================================================
    def start(self) -> None:
        """
        Inicia o loader da aplicação.
        Se ocorrer um erro, ele é armazenado em self._error.
        A janela é destruída e a aplicação é encerrada.

        Returns:
            None
        """
        try:
            self._loader.run()
            self.context = self._loader.context

        except BatchControlError as e:
            self._error = e

        finally:
            self.destroy()

    def get_context(self) -> AppContext:
        """
        Retorna o contexto da aplicação.

        Returns:
            AppContext: Contexto da aplicação.
        """
        
        if self.context is None:
            raise RuntimeError("Contexto da aplicação não foi inicializado.")
        return self.context

    def get_error(self):
        """
        Retorna o erro da aplicação.

        Returns:
            BatchControlError: Erro da aplicação.
        """
        return self._error

if __name__ == "__main__":
    app = SplashScreen()
    app.mainloop()
    print("Contexto: ", app.context)