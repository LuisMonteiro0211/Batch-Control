from src.dtos.product_dto import ProductDTO
from src.gui.components import ProductFrame
from src.gui.components.batch_frame import BatchFrame
from customtkinter import CTkFrame
from  typing import Literal, TypedDict
from src.gui.components.homepage import Homepage


class AppFrames(TypedDict):
    product: ProductFrame
    batch: BatchFrame

VisibleFrames = Homepage | ProductFrame | BatchFrame

class AppController():
    def __init__(self, master, homepage):
        self._master = master
        self._frames: AppFrames = {
            "product": ProductFrame(self._master, on_click_save_product=self.on_click_save_product),
            "batch": BatchFrame(self._master),
        }
        self._frame_to_show: VisibleFrames = homepage
        self._current_frame: VisibleFrames = homepage

    def _show_frame(self, frame: VisibleFrames):
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

    def on_click_save_product(self):
        product_frame = self._frames["product"]
        new_product_frame = product_frame._new_product_frame

        product_dto = new_product_frame.get_values_from_frame()
        

