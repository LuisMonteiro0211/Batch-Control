from customtkinter import CTk
from src.bootstrap.app_context import AppContext
from src.dtos.product_dto import ProductDTO
from src.gui.components.product_frame import ProductController
from typing import Callable
class AppController:
    def __init__(self, app_context: AppContext, app_frame: CTk, destroy_homepage: Callable) -> None:
        """
        Função 
        Inicialização dos controladores da aplicação.
        """
        self._app_frame = app_frame
        self._app_context = app_context
        self._product_controller = None
        self._batch_controller = None
        self._destroy_homepage = destroy_homepage
        self._init_controllers()

    def _init_controllers(self):
        """
        Função para inicialização e criação dos controladores da aplicação.
        """
        if self._app_context.services is not None and self._app_context.services.product is not None:
            self._product_controller = ProductController(
                product_service=self._app_context.services.product,
                init_products_to_view=self._app_context.dashboard_data.low_stock_products,
                product_frame_parent=self._app_frame
            )
            

    def on_click_product_button(self):
        self._destroy_homepage()
        if self._product_controller is not None:
            self._product_controller.show_product_frame()


    def on_click_batch_button(self):
        pass