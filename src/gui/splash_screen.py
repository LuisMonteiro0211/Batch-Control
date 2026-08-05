"""
Módulo da tela de splash (carregamento inicial).

Exibe logo, barra de progresso e mensagens enquanto o Loader
inicializa serviços, banco de dados e contexto da aplicação.

Métodos públicos:
    - start(): Executa o carregamento e fecha a splash.
    - get_context(): Retorna o AppContext carregado.
    - get_error(): Retorna erro capturado durante o carregamento.
"""

from typing import Optional
from customtkinter import CTk, CTkImage, CTkLabel, CTkProgressBar
from PIL import Image
from src.exceptions import BatchControlError
from src.gui.theme import COLORS, FONTS
from src.bootstrap.loader import Loader
from src.bootstrap import AppContext
from src.paths import icon_path

class SplashScreen(CTk):
    """
    Janela de carregamento exibida antes da aplicação principal.

    Executa o Loader em background e disponibiliza o contexto
    ou erro capturado após o fechamento da janela.
    """

    def __init__(self):
        super().__init__()
        self._icon_image = CTkImage(
            light_image=Image.open(
                icon_path("brach_ctrl_logo_transparent.png")
            ).convert("RGBA"),
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
        Executa o Loader e fecha a splash ao concluir.

        Erros de BatchControlError são capturados em ``self._error``
        sem interromper o fechamento da janela.
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
        Retorna o contexto da aplicação carregado pelo Loader.

        Returns:
            AppContext com serviços e dados do dashboard.

        Raises:
            RuntimeError: Se o contexto não foi inicializado.
        """
        
        if self.context is None:
            raise RuntimeError("Contexto da aplicação não foi inicializado.")
        return self.context

    def get_error(self) -> Optional[BatchControlError]:
        """
        Retorna o erro capturado durante o carregamento, se houver.

        Returns:
            BatchControlError ou None se o carregamento foi bem-sucedido.
        """
        return self._error

if __name__ == "__main__":
    app = SplashScreen()
    app.mainloop()
    print("Contexto: ", app.context)