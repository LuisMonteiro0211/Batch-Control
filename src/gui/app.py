"""
Módulo principal para construção da interface gráfica da aplicação.
"""

from customtkinter import CTk
from src.gui.components import Sidebar, Homepage
from src.gui.theme import COLORS
from src.gui.app_controller import AppController
from src.bootstrap import AppContext

class BatchControlApp(CTk):
    def __init__(self, context: AppContext):
        super().__init__()
        self.title("Batch Control")
        self.geometry("900x580")
        self.configure(fg_color=COLORS.fundo_primario)
        self.resizable(False, False)
        self._create_homepage()
        self._controller = AppController(self, self._homepage, context=context)
        self._build_widgets()
        self._layout_widgets()

    def _build_widgets(self):
        self._create_sidebar()

    def _create_sidebar(self):
        self._sidebar = Sidebar(self,
        on_click_product=self._controller.on_click_product_buttom,
        on_click_batch=self._controller.on_click_batch_buttom)

    def _layout_widgets(self):
        self._sidebar.pack(side="left", fill="y")
        self._sidebar.pack_propagate(False)
        self._homepage.pack(side="left", fill="y")
        self._homepage.pack_propagate(False)

    def _create_homepage(self):
        self._homepage = Homepage(self)

    def run(self):
        self.mainloop()