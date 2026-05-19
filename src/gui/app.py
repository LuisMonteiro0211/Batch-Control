"""
Módulo principal para construção da interface gráfica da aplicação.
"""

from customtkinter import CTk
from src.gui.components import Sidebar, ProductFrame
from src.gui.theme import COLORS, FONTS, SETTINGS
from src.gui.app_controller import AppController

class BatchControlApp(CTk):
    def __init__(self):
        self._controller = AppController()
        super().__init__()
        self.title("Batch Control")
        self.geometry("900x580")
        self.configure(fg_color=COLORS.fundo_primario)
        self.resizable(False, False)
        self._build_widgets()
        self._layout_widgets()

    def _build_widgets(self):
        self._create_sidebar()
        self._create_product_frame()

    def _create_sidebar(self):
        self._sidebar = Sidebar(self,
        on_click_product=self._controller.on_click_product_buttom, 
        on_click_batch=self._controller.on_click_batch_buttom)

    def _create_product_frame(self):
        self._product_frame = ProductFrame(self)

    def _layout_widgets(self):
        self._sidebar.pack(side="left", fill="y")
        self._sidebar.pack_propagate(False)

        self._product_frame.pack(side="left")
        self._product_frame.pack_propagate(False)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = BatchControlApp()
    app.run()