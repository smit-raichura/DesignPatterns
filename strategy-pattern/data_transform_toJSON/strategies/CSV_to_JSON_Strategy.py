from .transform_strategy import TransformStrategy
import csv
import io
import json

class CSVToJSONStrategy(TransformStrategy):
    def transform(self, data: str) -> str:
        csv_reader = csv.DictReader(io.StringIO(data))
        rows = list(csv_reader)
        return json.dumps(rows, indent=4)