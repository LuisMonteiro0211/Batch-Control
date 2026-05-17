from customtkinter import CTkFrame
from src.gui.theme import COLORS, FONTS, SETTINGS

class Sidebar(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self._configure_layout()
        self._build()

    def _configure_layout(self):
        self.configure(
            width=180,
            height=580,
            
        )
        pass

    def _build(self):
        pass