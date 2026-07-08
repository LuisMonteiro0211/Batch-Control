from customtkinter import CTkImage, CTkFrame, CTkLabel
from PIL import Image
from src.gui.theme import COLORS
from src.paths import icon_path

class Homepage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.configure(
            width=717,
            height=580,
            fg_color=COLORS.fundo_primario
        )

    def _get_image(self):
        image = Image.open(icon_path("brach_ctrl_logo_transparent.png"))
        return image
    
    def _build_widgets(self):
        self._image = CTkImage(
            light_image=self._get_image(),
            size=(270, 120)
        )
        self._label_image = CTkLabel(master=self, image=self._image, text="")

    def _layout_widgets(self):
        self._label_image.place(relx=0.5, rely=0.5, anchor="center")