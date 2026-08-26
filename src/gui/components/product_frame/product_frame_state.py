from enum import Enum

class ProductFrameState(Enum):
    """
    Enum para o estado do frame de produtos.
    """
    NEW_PRODUCT = "new_product"
    EDIT_PRODUCT = "edit_product"