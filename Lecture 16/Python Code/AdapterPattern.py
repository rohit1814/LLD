from abc import ABC, abstractmethod
import json


# 1. Target interface expected by the client
class IReports(ABC):
    @abstractmethod
    def get_json_data(self, data: str) -> str:
        pass


# 2. Adaptee: provides XML data from raw input
class XmlDataProvider:
    def get_xml_data(self, data: str) -> str:
        # Expect data in "name:id" format (e.g. "Alice:42")
        name, id_ = data.split(":")
        # Build a simple XML representation
        return f"<user><name>{name}</name><id>{id_}</id></user>"


# 3. Adapter: implements IReports by converting XML → JSON
class XmlDataProviderAdapter(IReports):
    def __init__(self, xml_provider: XmlDataProvider):
        self.xml_provider = xml_provider

    def get_json_data(self, data: str) -> str:
        # 1. Get XML from the adaptee
        xml = self.xml_provider.get_xml_data(data)

        # 2. Parse out <name> and <id> values (simple parsing)
        start_name = xml.find("<name>") + len("<name>")
        end_name = xml.find("</name>")
        name = xml[start_name:end_name]

        start_id = xml.find("<id>") + len("<id>")
        end_id = xml.find("</id>")
        id_ = xml[start_id:end_id]

        # 3. Build JSON string
        return json.dumps({"name": name, "id": int(id_)})


# 4. Client code works only with IReports
class Client:
    def get_report(self, report: IReports, raw_data: str):
        print("Processed JSON:", report.get_json_data(raw_data))


# Example usage
if __name__ == "__main__":
    xml_provider = XmlDataProvider()
    adapter = XmlDataProviderAdapter(xml_provider)

    client = Client()
    raw_data = "Alice:42"
    client.get_report(adapter, raw_data)
    # Output: Processed JSON: {"name": "Alice", "id": 42}
