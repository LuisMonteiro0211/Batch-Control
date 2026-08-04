from typing import List, Optional

from customtkinter import CTk
from src.dtos import ProductCardDTO, ProductDTO
from src.exceptions import DatabaseOperationError, ProductNotFoundError
from src.gui.components.product_frame import EditProductFrame, ProductFrame
from src.gui.error_window import ErrorWindow
from src.service.product_service import ProductService

class ProductController:
    def __init__(self, product_service: ProductService, 
    init_products_to_view: List[ProductCardDTO], 
    product_frame_parent: CTk):


        self._product_service = product_service
        self._products_to_view = init_products_to_view
        self._product_frame_parent = product_frame_parent
        self._product_frame = None
        self._message_state = None
        self._state_product_frame = None
        self._init_product_frame()

    def _init_product_frame(self):
        """
        Função de inicialização do frame de produtos, para ser chamada no início da aplicação.
        Cria o frame de produtos e inicializa o controlador de produtos.
        """
        self._product_frame = ProductFrame(
            master=self._product_frame_parent,
            on_click_save_product=self._on_click_save_product,
            on_click_save_edit_product=self._on_click_save_edit_product,
            on_click_edit_product=self.edit_product_mode,
            products_to_view=self._products_to_view
        )
        self._product_frame.show_new_product()

    def _on_click_save_product(self):
        pass
    
    def _on_click_save_edit_product(self):
        pass

    def get_product_id_to_edit(self, product_id: int) -> Optional[ProductDTO]:
        try:
            product = self._product_service.get_product_by_id(id_produto=product_id)
            return product

        except ProductNotFoundError as e:
            ErrorWindow(message=str(e))
            return None
        except DatabaseOperationError as e:
            ErrorWindow(message=str(e))
            return None

    
    def edit_product_mode(self, product_id: int):
        """
        Função para entrar no modo de edição de um produto.
        Chama a função show_edit_product do frame de produtos para exibir o frame de edição de um produto.

        Args:
            product_id: int

        Returns:
            None
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


    def show_product_frame(self):
        """
        Função para mostrar o frame de produtos.

        Args:
            None

        Returns:
            None
        """
        if self._product_frame is not None:
            self._product_frame.place(x=190, y=0, anchor="nw")


    def hide_product_frame(self):
        """
        Função para ocultar o frame de produtos.

        Args:
            None

        Returns:
            None
        """
        if self._product_frame is not None:
            self._product_frame.place_forget()