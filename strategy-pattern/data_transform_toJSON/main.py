import json

from transformer.data_transformer import DataTransformer
from strategies.XML_to_JSON_Strategy import XMLToJSONStrategy
from strategies.CSV_to_JSON_Strategy import CSVToJSONStrategy

if __name__ == "__main__":
    xml_data = '''<root>
                    <item>
                        <name>John</name>
                        <age>30</age>
                    </item>
                    <item>
                        <name>Jane</name>
                        <age>25</age>
                    </item>
                  </root>'''
    
    csv_data = "name,age\nJohn,30\nJane,25"

    # Using XML to JSON strategy
    dataTransformer = DataTransformer(XMLToJSONStrategy())
    json_result = dataTransformer.transform(xml_data)
    print("XML to JSON:")
    print(json.dumps(json_result, indent=4))

    # Switching to CSV to JSON strategy
    dataTransformer.set_strategy(CSVToJSONStrategy())
    json_result = dataTransformer.transform(csv_data)
    print("\nCSV to JSON:")
    print(json_result)
