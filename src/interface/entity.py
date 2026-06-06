from abc import ABC, abstractmethod
from typing import Any, Optional
from typing import List, Tuple


class Entity(ABC):
    @abstractmethod
    def create(self, entity: Any) -> Optional[int]:
        pass

    @abstractmethod
    def update(self, id: int, list_to_update: List[Tuple[str, Any]]) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Any:
        pass
