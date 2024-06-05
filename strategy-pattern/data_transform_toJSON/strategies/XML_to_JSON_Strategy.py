from .transform_strategy import TransformStrategy
import xml.etree.ElementTree as ET

class XMLToJSONStrategy(TransformStrategy):
    def transform(self, data: str) -> str:
        # Parse XML
        root = ET.fromstring(data)
        return self._element_to_dict(root)
    
    def _element_to_dict(self, element):
        if len(element) == 0:
            return element.text
        return {element.tag: {child.tag: self._element_to_dict(child) for child in element}}