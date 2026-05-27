"""
Módulo para criação do frame com scrollbar.

Métodos públicos:
    - insert_frame_item(frame_item: CTkFrame): Método para inserir um frame item no frame canvas.

Uso recomendado:
    >>> from src.gui.components.scrollbar_frame import ScrollbarFrame
    >>> scrollbar_frame = ScrollbarFrame(master)
    >>> scrollbar_frame.insert_frame_item(frame_item)

Observações:
    - O frame a ser inserido sempre vem no topo do frame canvas.
"""

from customtkinter import CTkFrame, CTkCanvas, CTkLabel
from src.gui.theme import COLORS
from src.gui.theme.theme import FONTS

class ScrollbarFrame(CTkFrame):
    """
    Classe para criação do frame com scrollbar.

    Args:
        master: Widget pai do frame com scrollbar.
    """
    def __init__(self, master):
        super().__init__(master)
        self._configure_layout()

    def _configure_layout(self):
        """
        Método para configurar o layout do frame com scrollbar
        """
        # Configura o frame principal externo
        self.configure(
            width=681,
            height=200,
            fg_color=COLORS.transparente,
            corner_radius=5,
            border_width=1,
            border_color=COLORS.bordas,
        )

    def _create_canvas(self):
        self._canvas = CTkCanvas(
            self,
            width=681,
            height=168,
            highlightthickness=0,
            background=COLORS.transparente,
        )

    def _create_frame_to_canvas(self):
        self._frame_to_canvas = CTkFrame(
            self._canvas,
            fg_color=COLORS.transparente)

    def _create_window_to_canvas(self):
        self._window_to_canvas = self._canvas.create_window(
            (0, 0),
            window=self._frame_to_canvas,
            anchor="nw",
            tags="frame_to_canvas",
            width=681,
        )
        self._frame_to_canvas.bind("<Configure>", self._on_frame_to_canvas_configure)

    def _on_frame_to_canvas_configure(self, event):
        """
        Método para configurar o frame canvas quando é identificado que ele foi configurado.
        """
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))
        self._canvas.itemconfig("frame_to_canvas", width=event.width)

    def _bind_mouse_wheel(self):
        """
        Método para vincular o evento de scroll do mouse ao frame canvas sem precisar do scrollbar.
        """
        self._canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

    def _on_mouse_wheel(self, event):
        """
        Método para scrollar o frame canvas quando é identificado que o mouse foi rolado.
        """
        self._canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _configure_scrollbar(self):
        """
        Método para configurar o scrollbar do frame canvas.
        """
        self._frame_to_canvas.bind("<Configure>", self._on_frame_to_canvas_configure)
    
    # Métodos públicos
    def insert_frame_item(self, frame_item: CTkFrame):
        """
        Método para inserir um frame item no frame canvas.
        """
        frame_item.pack(side="top", fill="x")
        frame_item.pack_propagate(False)

    def initialization_message(self, message: str, icon_path: str):
        """
        Método para criar um label com uma mensagem de informação no meio do frame.
        """
        self._message_label = CTkLabel(
            self,
            image=icon_path,
            compound="left",
            text=message,
            text_color=COLORS.texto_principal,
            font=FONTS.subtitulo_tela,
            anchor="center",
        )
        self._message_label.place(x=266, y=92)    
        
    def _create_canvas(self):
        """
        Método para criar o canvas do frame com scrollbar.
        """
        self._create_canvas()
        self._create_frame_to_canvas()
        self._create_window_to_canvas()
        self._bind_mouse_wheel()
        self._configure_scrollbar()