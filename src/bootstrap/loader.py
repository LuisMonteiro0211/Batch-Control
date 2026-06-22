from typing import Callable
from src.bootstrap.app_context import AppContext
from src.bootstrap.app_service import AppServices
from src.service.product_service import ProductService
from src.repository.product_repository import ProductRepository

DATABASE_NAME = "test_batch_control.db"
class Loader:
    def __init__(self, on_progress: Callable[[str, float]]) -> None:
        self._on_progress: Callable[[str, float]] = on_progress
        self.context: AppContext = AppContext()

    def run(self) -> AppContext:
        """
        Executa o loader da aplicação.
        Passo a passo:
        1. Conecta ao banco de dados.
        2. Carrega os produtos.
        3. Carrega os lotes.
        4. Prepara a interface.

        Returns:
            AppContext: Contexto da aplicação.
        """
        steps = [
            ("Conectando ao banco...", self._step_connect),
            ("Carregando produtos...", self._step_load_products),
            ("Carregando lotes...", self._step_load_batches),
            ("Preparando interface...", self._step_prepare_interface)
        ]
        

        total_steps = len(steps)

        for index, (message, step_function) in enumerate(steps):
            progress = (index +1) / total_steps
            self._on_progress(message, progress)
            step_function()

        return self.context

    def _step_connect(self):
        product_repository = ProductRepository(database_name=DATABASE_NAME)
        product_service = ProductService(product_repository=product_repository)

        self.context.services = AppServices(product=product_service) #Preparando o contexto para a aplicação

    def _step_load_products(self):
        self.context.dashboard_data.low_stock_products = []

    def _step_load_batches(self):
        self.context.dashboard_data.expiring_batches = []

    def _step_prepare_interface(self):
        
        if self.context.services is None:
            raise RuntimeError("Serviços não foram carregados.")

        if self.context.services.product is None:
            raise RuntimeError("Serviço de produtos não foi carregado.")