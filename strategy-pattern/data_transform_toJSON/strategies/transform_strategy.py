from abc import ABC, abstractmethod

class TransformStrategy(ABC):
    @abstractmethod
    def transform(self, data: str) -> str:
        pass