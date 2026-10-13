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
from src.dtos import ProductCardDTO, ProductDTO, SearchObjectTransfer
from src.exceptions import DatabaseOperationError, ProductNotFoundError, DuplicateSkuError, ValidationError
from src.exceptions.exceptions import NoSearchValueError, ProductHasBalanceError
from src.gui.components.product_frame import ProductFrame
from src.service.product_service import ProductService
from src.gui.interaction_window import FactoryInteractionWindow
from src.forms.product_form import build_edit_product_dto, build_product_create_dto
from src.gui.components.product_frame.product_frame_state import ProductFrameState
from src.interface.protocols import SearchProductByNameProtocol

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
        self._original_product_dto = None
        self._init_product_frame()
        self._status_filter = False

    def _init_product_frame(self) -> None:
        """Cria o ProductFrame e configura os callbacks de ação."""
        self._product_frame = ProductFrame(
            master=self._product_frame_parent,
            on_click_save_product=self._on_click_save_product,
            on_click_save_edit_product=self._on_click_save_edit_product,
            trigger_search_product_by_name=self.trigger_search_product_by_name,
            search_product_by_name=self.search_product_by_name,
            on_click_edit_product=self.edit_product_mode,
            products_to_view=self._products_to_view,
            on_click_delete_product=self._on_click_delete_product
        )
        self._product_frame.show_new_product()

    def _on_click_save_product(self) -> None:
        """
        Callback do botão salvar no formulário de novo produto.

        Coleta os valores do frame, monta o DTO de criação, persiste via serviço
        e exibe janela de sucesso ou erro (validação, SKU duplicado ou banco).
        """
        if self._product_frame is not None:
            raw_data = self._product_frame.get_raw_new_product_values()
            if raw_data is not None:
                try:
                    create_product_dto = build_product_create_dto(raw_data=raw_data)
                    new_product = self._product_service.create_product(product_dto=create_product_dto)
                    FactoryInteractionWindow.success_window(
                        master=self._product_frame,
                        message=(f"Produto com o ID {new_product} criado com sucesso!")
                    )

                except ValidationError as e:
                    FactoryInteractionWindow.error_window(
                    master=self._product_frame,
                    message=str(e))

                except DuplicateSkuError as e:
                    FactoryInteractionWindow.error_window(
                        master=self._product_frame,
                        message=str(e))

                except DatabaseOperationError as e:
                    FactoryInteractionWindow.error_window(
                        master=self._product_frame,
                        message=str(e))

    def _on_click_delete_product(self, product_id: int) -> None:
        """Callback do botão deletar no formulário de produto. Deleta um produto."""
        if self._product_frame is not None:

            #Chama a Janela de confirmação
            action_user = FactoryInteractionWindow.confirm_window(
                master=self._product_frame,
                message="Tem certeza que deseja deletar o produto?"
            )

            if action_user.get_action() == True:
                try:
                    #Tenta deletar o produto
                    self._product_service.delete_product(id_produto=product_id)
                    FactoryInteractionWindow.success_window(
                        master=self._product_frame,
                        message="Produto deletado com sucesso."
                    )
                    self._product_frame.hide_edit_product_frame()
                    self._product_frame.show_new_product()

                except DatabaseOperationError as e:
                    FactoryInteractionWindow.error_window(
                        master=self._product_frame,
                        message=str(e)
                    )
                
                except ProductNotFoundError as e:
                    FactoryInteractionWindow.error_window(
                        master=self._product_frame,
                        message=str(e)
                    )

                except ProductHasBalanceError as e:
                    FactoryInteractionWindow.error_window(
                        master=self._product_frame,
                        message=str(e)
                    )
                    
                
            else:
                FactoryInteractionWindow.alert_window(
                    master=self._product_frame,
                    message="Operação cancelada."
                )

    def _on_click_save_edit_product(self) -> None:
        """Callback do botão salvar no formulário de edição. Coleta os valores do frame."""
        if self._product_frame is not None:
            raw_data_edit = self._product_frame.get_raw_edit_values()#Coleta os valores do formulário de edição
            
            if raw_data_edit is None:
                FactoryInteractionWindow.error_window(
                    master=self._product_frame,
                    message="Nenhum dado encontrado!"
                )
                return

            if self._original_product_dto is not None:
                editing_product_dto = build_edit_product_dto(#Converte os valores do formulário de edição para um DTO
                    raw_data_edit=raw_data_edit,
                    original_product_dto=self._original_product_dto
                )

                if editing_product_dto.product_status != self._original_product_dto.product_status:
                    #Se houver tentativa de bloquear um item
                    if self._product_service.has_balance(id_produto=self._original_product_dto.id):
                        FactoryInteractionWindow.error_window(
                            master=self._product_frame,
                            message="Não é possível bloquear um produto com saldo ativo."
                        )
                        return

                if editing_product_dto == self._original_product_dto:
                    #Se os valores do formulário de edição são iguais aos valores do produto original, não há alterações para salvar.
                    FactoryInteractionWindow.alert_window(
                        master=self._product_frame,
                        message="Não há alterações para salvar."
                    )
                else:
                    #Se os valores do formulário de edição são diferentes dos valores do produto original, atualiza o produto.

                    action_user = FactoryInteractionWindow.confirm_window(
                        master=self._product_frame,
                        message="Confirmar alterações no produto?"
                    )

                    if action_user.get_action() == True:

                        try:
                            self._product_service.update_product(
                                original_product_dto=self._original_product_dto,
                                edited_product_dto=editing_product_dto
                            )
                        
                            FactoryInteractionWindow.success_window(
                                master=self._product_frame,
                                message="Produto atualizado com sucesso."
                            )
                            self._product_frame.hide_edit_product_frame()
                            self._product_frame.show_new_product()
                            self._low_products_cards = self._product_service.get_cards_low_stock()
                            self._product_frame.update_products_cards(self._low_products_cards)


                        except DuplicateSkuError as e:
                            FactoryInteractionWindow.error_window(
                                master=self._product_frame,
                                message=str(e)
                            )
                            return None
                        except DatabaseOperationError as e:
                            FactoryInteractionWindow.error_window(
                                master=self._product_frame,
                                message=str(e)
                            )
                            return None

                    else:
                        FactoryInteractionWindow.alert_window(
                            master=self._product_frame,
                            message="Operação cancelada."
                        )

            else:
                #Se o produto original não foi encontrado, exibe uma mensagem de erro.
                FactoryInteractionWindow.alert_window(
                    master=self._product_frame,
                    message="Produto não encontrado."
                )

                ##Sair do modo de edição

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
            FactoryInteractionWindow.error_window(
                master=self._product_frame,
                message=str(e)
            )
            return None
        except DatabaseOperationError as e:
            FactoryInteractionWindow.error_window(
                master=self._product_frame,
                message=str(e)
            )
            return None

    def edit_product_mode(self, product_id: int) -> None:
        """
        Entra no modo de edição, substituindo o formulário de novo produto.

        Só permite a transição quando o frame está no estado ``new_product``.

        Args:
            product_id: ID do produto selecionado na tabela.
        """
        product_dto = self.get_product_id_to_edit(product_id=product_id)
        self._original_product_dto = product_dto #Salva o produto no estado antes da edição

        if self._product_frame is None:
            FactoryInteractionWindow.error_window(
                master=self._product_frame,
                message="Frame de produtos não inicializado."
            )
            return

        current_state = self._product_frame.get_state_product_frame()
        if current_state != ProductFrameState.NEW_PRODUCT:
            return

        if product_dto is None:
            FactoryInteractionWindow.error_window(
                master=self._product_frame,
                message="Produto não encontrado."
            )
            return

        self._product_frame.hide_new_product_frame()
        self._product_frame.show_edit_product(product_dto=product_dto)

    def show_product_frame(self) -> None:
        """Posiciona o frame de produtos na janela principal."""
        if self._product_frame is not None:
            self._product_frame.place(x=190, y=0, anchor="nw")

    def hide_product_frame(self) -> None:
        """Remove o frame de produtos da janela principal."""
        if self._product_frame is not None:
            self._product_frame.place_forget()

    def trigger_search_product_by_name(self, search_object: SearchObjectTransfer) -> None:
        """
        Callback para a factory chamar quando finalizar a busca por nome

        Args:
            list_products_cards: Lista com as informações para montar o card do produto ou None se não houver produtos com o nome informado.
        Returns:
            None
        """

        self._search_object = search_object
        self._list_products_cards = self._search_object.product_cards

        if self._product_frame is not None:
            if self._list_products_cards is not None and search_object.text_search is not None:
                self._product_frame.update_products_cards(products_to_view=self._list_products_cards)

            if search_object.text_search is None and self._list_products_cards is None:
                self._low_products_cards = self._product_service.get_cards_low_stock()
                self._product_frame.update_products_cards(self._low_products_cards)

    
    def search_product_by_name(self, name_product: str) -> Optional[List[ProductCardDTO]]:
        """
        Busca produtos pelo nome respeitando o filtro de produtos bloqueados.

        Lê o status do filtro no ProductFrame: se estiver ativo, retorna todos os
        produtos (inclusive os bloqueados); caso contrário, retorna apenas os ativos.
        Erros de banco são exibidos em janela de erro e "produto não encontrado"
        vira uma mensagem na própria tabela.

        Args:
            name_product: Nome (ou parte dele) do produto a ser buscado.

        Returns:
            Optional[List[ProductCardDTO]]: Cards correspondentes ao nome, ou None
            quando nenhum produto é encontrado.
        """
        if self._product_frame is not None:
            self._status_filter = self._product_frame.get_status_filter()

            if self._status_filter:
                #Caso o filtro seja True para todos os produtos inclusive os bloqueados
                try:
                    product_cards =  self._product_service.get_all_product_cards_by_name(name_product=name_product)
                    if product_cards is not None:
                        return product_cards
                except DatabaseOperationError as e:
                    FactoryInteractionWindow.error_window(
                        master=self._product_frame,
                        message=str(e)
                    )
                except ProductNotFoundError as e:
                    self._product_frame.message_table(str(e))
            else:
                #Caso seja false e queira somente os produtos ativos
                try:
                    product_cards = self._product_service.get_product_cards_by_name(name_product=name_product)
                    if product_cards is not None:
                        return product_cards
                except DatabaseOperationError as e:
                    FactoryInteractionWindow.error_window(
                        master = self._product_frame,
                        message=str(e)
                    )
                except ProductNotFoundError as e:
                    self._product_frame.message_table(str(e))