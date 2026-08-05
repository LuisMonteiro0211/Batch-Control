"""
Módulo do controlador da tela de produtos.

Conecta a interface (ProductFrame) ao ProductService, gerenciando
criação, edição e exibição de produtos.

Métodos públicos:
    - edit_product_mode(): Abre o formulário de edição para um produto.
    - show_product_frame(): Posiciona o frame de produtos na janela.
    - hide_product_frame(): Oculta o frame de produtos.
    - get_product_id_to_edit(): Busca um produto pelo ID para edição.
"""

from typing import List, Optional

from customtkinter import CTk
from src.dtos import ProductCardDTO, ProductDTO
from src.exceptions import DatabaseOperationError, ProductNotFoundError
from src.gui.components.product_frame import ProductFrame
from src.gui.error_window import ErrorWindow
from src.service.product_service import ProductService


class ProductController:
    """
    Orquestra o fluxo de produtos entre a GUI e o service.

    Args:
        product_service: Serviço de produtos para operações no banco.
        init_products_to_view: Produtos exibidos na tabela ao abrir a tela.
        product_frame_parent: Widget pai onde o ProductFrame será posicionado.
    """

    def __init__(
        self,
        product_service: ProductService,
        init_products_to_view: List[ProductCardDTO],
        product_frame_parent: CTk,
    ):
        self._product_service = product_service
        self._products_to_view = init_products_to_view
        self._product_frame_parent = product_frame_parent
        self._product_frame = None
        self._message_state = None
        self._state_product_frame = None
        self._init_product_frame()

    def _init_product_frame(self) -> None:
        """Cria o ProductFrame e configura os callbacks de ação."""
        self._product_frame = ProductFrame(
            master=self._product_frame_parent,
            on_click_save_product=self._on_click_save_product,
            on_click_save_edit_product=self._on_click_save_edit_product,
            on_click_edit_product=self.edit_product_mode,
            products_to_view=self._products_to_view
        )
        self._product_frame.show_new_product()

    def _on_click_save_product(self) -> None:
        """Callback do botão salvar no formulário de novo produto. Implementação pendente."""
        pass

    def _on_click_save_edit_product(self) -> None:
        """Callback do botão salvar no formulário de edição. Coleta os valores do frame."""
        if self._product_frame is not None:
            print("Resultado da coleta de dados:")
            print("--------------------------------")
            print(self._product_frame.get_raw_values())

    def get_product_id_to_edit(self, product_id: int) -> Optional[ProductDTO]:
        """
        Busca um produto pelo ID para preencher o formulário de edição.

        Args:
            product_id: ID do produto a ser editado.

        Returns:
            ProductDTO do produto encontrado, ou None em caso de erro.
        """
        try:
            product = self._product_service.get_product_by_id(id_produto=product_id)
            return product

        except ProductNotFoundError as e:
            ErrorWindow(message=str(e))
            return None
        except DatabaseOperationError as e:
            ErrorWindow(message=str(e))
            return None

    def edit_product_mode(self, product_id: int) -> None:
        """
        Entra no modo de edição, substituindo o formulário de novo produto.

        Só permite a transição quando o frame está no estado ``new_product``.

        Args:
            product_id: ID do produto selecionado na tabela.
        """
        product_dto = self.get_product_id_to_edit(product_id=product_id)

        if self._product_frame is not None:
            self._state_product_frame = self._product_frame.get_state_product_frame()

            if self._state_product_frame == "new_product":
                if product_dto is not None:
                    if self._product_frame is not None:
                        self._product_frame.hide_new_product_frame()
                        self._product_frame.show_edit_product(product_dto=product_dto)
                        self._state_product_frame = "edit_product"
                    else:
                        ErrorWindow(message="Frame de produtos não inicializado.")
                else:
                    ErrorWindow(message="Produto não encontrado.")

    def show_product_frame(self) -> None:
        """Posiciona o frame de produtos na janela principal."""
        if self._product_frame is not None:
            self._product_frame.place(x=190, y=0, anchor="nw")

    def hide_product_frame(self) -> None:
        """Remove o frame de produtos da janela principal."""
        if self._product_frame is not None:
            self._product_frame.place_forget()
