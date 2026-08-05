"""
Módulo do controlador principal da aplicação.

Responsável por inicializar os controladores de cada tela e rotear
as ações do menu lateral para o controller correspondente.

Métodos públicos:
    - on_click_product_button(): Exibe a tela de produtos.
    - on_click_batch_button(): Exibe a tela de lotes (em desenvolvimento).
"""

from customtkinter import CTk
from src.bootstrap.app_context import AppContext
from src.gui.components.product_frame import ProductController
from typing import Callable


class AppController:
    """
    Orquestra a navegação entre telas e delega ações aos controllers específicos.

    Args:
        app_context: Contexto da aplicação com serviços e dados do dashboard.
        app_frame: Janela principal (CTk) onde os frames são posicionados.
        destroy_homepage: Callback para remover a homepage ao navegar.
    """

    def __init__(self, app_context: AppContext, app_frame: CTk, destroy_homepage: Callable) -> None:
        self._app_frame = app_frame
        self._app_context = app_context
        self._product_controller = None
        self._batch_controller = None
        self._destroy_homepage = destroy_homepage
        self._init_controllers()

    def _init_controllers(self) -> None:
        """Inicializa os controllers disponíveis com base no contexto carregado."""
        if self._app_context.services is not None and self._app_context.services.product is not None:
            self._product_controller = ProductController(
                product_service=self._app_context.services.product,
                init_products_to_view=self._app_context.dashboard_data.low_stock_products,
                product_frame_parent=self._app_frame
            )

    def on_click_product_button(self) -> None:
        """Remove a homepage e exibe a tela de produtos."""
        self._destroy_homepage()
        if self._product_controller is not None:
            self._product_controller.show_product_frame()

    def on_click_batch_button(self) -> None:
        """Exibe a tela de lotes. Implementação pendente."""
        pass
