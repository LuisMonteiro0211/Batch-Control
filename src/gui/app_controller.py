from src.gui.components import ProductFrame
from src.gui.components.batch_frame import BatchFrame
from customtkinter import CTkFrame


class AppController():
    def __init__(self, master, homepage):
        self._master = master
        self._frames = {
            "product": ProductFrame(self._master),
            "batch": BatchFrame(self._master),
        }
        self._frame_to_show: CTkFrame = homepage
        self._current_frame: CTkFrame = homepage

    def _show_frame(self, frame):
        if self._current_frame == self._frame_to_show:
            return
        else:
            self._current_frame.pack_forget()
            frame.pack(side="left", fill="y")
            frame.pack_propagate(False)
            self._current_frame = frame

    def on_click_product_buttom(self):
        self._frame_to_show = self._frames["product"]
        self._show_frame(self._frame_to_show)

    def on_click_batch_buttom(self):
        self._frame_to_show = self._frames["batch"]
        self._show_frame(self._frame_to_show)
