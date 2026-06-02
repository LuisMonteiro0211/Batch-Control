from typing import Callable
from .app_context import AppContext

class Loader:
    def __init__(self, on_progress: Callable[[str, float]]) -> None:
        self._on_progress: Callable[[str, float]] = on_progress
        self.context: AppContext = AppContext()

    def run(self) -> AppContext:
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
        pass

    def _step_load_products(self):
        pass

    def _step_load_batches(self):
        pass

    def _step_prepare_interface(self):
        pass