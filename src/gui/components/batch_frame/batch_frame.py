from customtkinter import CTkFrame, CTkLabel
from src.gui.theme import COLORS, FONTS
from src.gui.components.factory import FieldFactory
from .new_batch_frame import NewBatchFrame
from .batch_table import BatchTable

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

        self._batch_search_frame = CTkFrame(
            self,
            width=685,
            height=284,
            fg_color=COLORS.transparente,
            corner_radius=0,
        )
        self._batch_search_label = CTkLabel(
            self._batch_search_frame,
            text="Buscar",
            text_color=COLORS.texto_principal,
            font=FONTS.titulo_tela
        )

        self._subtitle_search = CTkLabel(
            self._batch_search_frame,
            text="Pesquisa de lotes",
            text_color=COLORS.desabilitado,
            font=FONTS.subtitulo_tela
        )

        self._search_entry = FieldFactory.create_entry(
            self._batch_search_frame,
            placeholder="Buscar lote...",
            name_field="search_batch_name"
        )

        self._batch_table = BatchTable(self)
        self._batch_table.initialization()

    def _layout_widgets(self):
        self._title_batch.place(x=12, y=18, anchor="nw")
        self._title_batch.pack_propagate(False)
        self._subtitle_batch.place(x=12, y=40, anchor="nw")
        self._subtitle_batch.pack_propagate(False)
        self._new_batch_frame.place(x=12, y=70, anchor="nw")
        self._new_batch_frame.pack_propagate(False)

        self._batch_search_frame.place(x=12, y=281, anchor="nw")
        self._batch_search_frame.pack_propagate(False)

        self._batch_search_label.place(x=0, y=0, anchor="nw")
        self._subtitle_search.place(x=0, y=22, anchor="nw")

        self._search_entry.field.place(x=0, y=48, anchor="nw")

        self._batch_table.place(x=16, y=365, anchor="nw")
        self._batch_table.pack_propagate(False)