"""
Módulo principal para construção da interface gráfica da aplicação.

Define a janela principal (BatchControlApp) com sidebar, homepage
e integração com o AppController para navegação entre telas.
"""

from customtkinter import CTk
from src.gui.components import Sidebar, Homepage
from src.gui.theme import COLORS
from src.gui.app_controller import AppController
from src.bootstrap import AppContext


class BatchControlApp(CTk):
    """
    Janela principal da aplicação Batch Control.

    Args:
        context: Contexto carregado pelo Loader com serviços e dados do dashboard.
    """

    def __init__(self, context: AppContext):
        super().__init__()
        self._app_context = context
        self._app_controller = AppController(app_context=self._app_context, app_frame=self, destroy_homepage=self.destroy_homepage)
        self.title("Batch Control")
        self.geometry("900x580")
        self.configure(fg_color=COLORS.fundo_primario)
        self.resizable(False, False)
        self._create_homepage()
        self._build_widgets()
        self._layout_widgets()

    def _build_widgets(self) -> None:
        """Cria os widgets principais da janela."""
        self._create_sidebar()

    def _create_sidebar(self) -> None:
        """Instancia a sidebar com callbacks de navegação."""
        self._sidebar = Sidebar(
        parent=self,
        on_click_product=self._app_controller.on_click_product_button,
        on_click_batch=self._app_controller.on_click_batch_button)

    def _layout_widgets(self) -> None:
        """Posiciona sidebar e homepage lado a lado."""
        self._sidebar.pack(side="left", fill="y")
        self._sidebar.pack_propagate(False)
        self._homepage.pack(side="left", fill="y")
        self._homepage.pack_propagate(False)

    def _create_homepage(self) -> None:
        """Cria o frame da homepage exibido ao abrir a aplicação."""
        self._homepage = Homepage(self)

    def destroy_homepage(self) -> None:
        """Remove a homepage da tela ao navegar para outra seção."""
        if self._homepage is not None:
            self._homepage.destroy()

    def run(self) -> None:
        """Inicia o loop principal da interface gráfica."""
        self.mainloop()
