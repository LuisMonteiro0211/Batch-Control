from customtkinter import CTkFrame, CTkLabel
from src.gui.theme import COLORS, FONTS
from .new_batch_frame import NewBatchFrame

class BatchFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self._setup_ui()

    def _setup_ui(self):
        self._configure_layout()
        self._build_widgets()
        self._layout_widgets()

    def _configure_layout(self):
        self.configure(
            width=720,
            height=580,
            fg_color=COLORS.fundo_secundario,
            corner_radius=0,
        )

    def _build_widgets(self):
        self._title_batch = CTkLabel(
            self,
            text="Lotes",
            text_color=COLORS.texto_principal,
            font=FONTS.titulo_tela
        )

        self._subtitle_batch = CTkLabel(
            self,
            text="Gerenciamento de lotes do estoque",
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_tela
        )

        self._new_batch_frame = NewBatchFrame(self)

    def _layout_widgets(self):
        self._title_batch.place(x=12, y=18, anchor="nw")
        self._title_batch.pack_propagate(False)
        self._subtitle_batch.place(x=12, y=40, anchor="nw")
        self._subtitle_batch.pack_propagate(False)
        self._new_batch_frame.place(x=12, y=70, anchor="nw")