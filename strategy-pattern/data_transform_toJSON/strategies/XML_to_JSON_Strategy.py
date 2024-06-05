from .transform_strategy import TransformStrategy
import xmltodict
import json

class XMLToJSONStrategy(TransformStrategy):
    def transform(self, data: str) -> str:
        # Parse XML
        xml_dict = xmltodict.parse(data)
        return json.dumps(xml_dict, indent=4)