from src.gui.components import ProductFrame


class AppController():
    def __init__(self, master, homepage):
        self._master = master
        self._homepage = homepage
        self._current_frame = homepage
        self._product_frame = None

    def _show_frame(self, frame):
        if self._current_frame is frame:
            return
        self._current_frame.pack_forget()
        frame.pack(side="left", fill="y")
        frame.pack_propagate(False)
        self._current_frame = frame

    def on_click_product_buttom(self):
        if self._product_frame is None:
            self._product_frame = ProductFrame(self._master)
        self._show_frame(self._product_frame)

    def on_click_batch_buttom(self):
        print("Lote clicado")
