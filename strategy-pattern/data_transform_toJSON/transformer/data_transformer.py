from strategies.transform_strategy import TransformStrategy

class DataTransformer:
    def __init__(self, strategy: TransformStrategy):
        self._strategy = strategy

    def set_strategy(self,strategy: TransformStrategy):
        self._strategy = strategy

    def transform(self, data: str) -> str:
        return self._strategy.transform(data)
    