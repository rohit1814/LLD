# Learn this also Lazy loading and fast loading using Proxy Design Pattern
# Do you also want me to show how to make the proxy lazy-load the real service 
# (only create RealDataService when fetch_data() is actually called), like in a virtual proxy?


from abc import ABC, abstractmethod

# Interface
class IDataService(ABC):
    @abstractmethod
    def fetch_data(self) -> str:
        pass


# Real service (simulates heavy setup / remote connection)
class RealDataService(IDataService):
    def __init__(self):
        # Simulating a heavy operation like connecting to a remote server
        print("[RealDataService] Initialized (simulating remote setup)")

    def fetch_data(self) -> str:
        return "[RealDataService] Data from server"


# Proxy class
class DataServiceProxy(IDataService):
    def __init__(self):
        # Proxy manages RealDataService initialization
        self.real_service = RealDataService()

    def fetch_data(self) -> str:
        print("[DataServiceProxy] Connecting to remote service...")
        return self.real_service.fetch_data()


# Client code
if __name__ == "__main__":
    data_service: IDataService = DataServiceProxy()
    result = data_service.fetch_data()
    print(result)
