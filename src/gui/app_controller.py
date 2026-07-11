from dataclasses import replace
from src.bootstrap.app_context import AppContext
from src.dtos.product_dto import ProductDTO
from src.exceptions import DatabaseOperationError, DuplicateSkuError
from src.exceptions.exceptions import ValidationError
from src.forms.product_form import build_product_dto
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
    def __init__(self, master, homepage, context: AppContext):
        self._master = master
        self._context = context
        self._frames: AppFrames = {
            "product": ProductFrame(
                self._master,
                on_click_save_product=self.on_click_save_product,
                on_click_save_edit_product=self.on_click_save_edit_product,
                on_click_edit_product=self.on_click_edit_product,
                products_to_view=self._context.dashboard_data.low_stock_products,
            ),
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
        """

        "Função que salva um novo produto na aplicação."

        Args:
            None

        Returns:
            None
        """

        product_frame = self._frames["product"]
        new_product_frame = product_frame._new_product_frame

        if self._context.services is None or self._context.services.product is None:
            raise RuntimeError("Serviços não foram carregados.")

        try:
            raw_data = new_product_frame.get_raw_values()
            product_dto = build_product_dto(raw_date=raw_data)
            
            product_id = self._context.services.product.create_product(product_dto=product_dto)

        except ValidationError as e:
            #Exibir mensagem de erro na tela
            pass
        except DuplicateSkuError as e:
            #Exibir mensagem de erro na tela
            pass
        except DatabaseOperationError as e:
            #Exibir mensagem de erro na tela
            pass

    def on_click_edit_product(self, product_id: int):
        if self._context.services is None or self._context.services.product is None:
            raise RuntimeError("Serviços não foram carregados.")

        product_dto = self._context.services.product.get_product_by_id(id_produto=product_id)
        self._frames["product"].show_edit_product(product_dto=product_dto)

    def on_click_save_edit_product(self):
        product_frame = self._frames["product"]
        edit_product_frame = product_frame.edit_product_frame

        if edit_product_frame is None:
            return

        if self._context.services is None or self._context.services.product is None:
            raise RuntimeError("Serviços não foram carregados.")

        try:
            raw_data = edit_product_frame.get_raw_values()
            product_dto = replace(
                build_product_dto(raw_date=raw_data),
                id=raw_data["id"],
            )

            self._context.services.product.update_product(
                id_produto=product_dto.id,
                list_to_update=[
                    ("nome_produto", product_dto.name),
                    ("empresa", product_dto.product_firm),
                    ("saldo_min", product_dto.minimun_balance),
                    ("consumo_mensal", product_dto.consumption_monthly),
                ],
            )
            product_frame.show_new_product()

        except ValidationError:
            pass
        except DatabaseOperationError:
            pass

