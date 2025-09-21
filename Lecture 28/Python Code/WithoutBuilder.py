class HttpRequest:
    def __init__(self, url, method="GET", timeout=30, headers=None, query_params=None, body=""):
        self.url = url
        self.method = method
        self.timeout = timeout
        self.headers = headers if headers is not None else {}
        self.query_params = query_params if query_params is not None else {}
        self.body = body

    # Setters (leads to mutable object, like in C++)
    def set_url(self, url):
        self.url = url

    def set_method(self, method):
        self.method = method

    def add_header(self, key, value):
        self.headers[key] = value

    def add_query_param(self, key, value):
        self.query_params[key] = value

    def set_body(self, body):
        self.body = body

    def set_timeout(self, timeout):
        self.timeout = timeout

    # Simulate HTTP execution
    def execute(self):
        print(f"Executing {self.method} request to {self.url}")

        if self.query_params:
            print("Query Parameters:")
            for k, v in self.query_params.items():
                print(f"  {k}={v}")

        if self.headers:
            print("Headers:")
            for k, v in self.headers.items():
                print(f"  {k}: {v}")

        if self.body:
            print(f"Body: {self.body}")

        print(f"Timeout: {self.timeout} seconds")
        print("Request executed successfully!")


# --- Usage ---
if __name__ == "__main__":
    # Using default arguments (like constructors)
    request1 = HttpRequest("https://api.example.com")
    request2 = HttpRequest("https://api.example.com", method="POST")
    request3 = HttpRequest("https://api.example.com", method="PUT", timeout=60)

    # Using setters (mutable object problem)
    request4 = HttpRequest("https://api.example.com")
    request4.set_method("POST")
    request4.add_header("Content-Type", "application/json")
    request4.add_query_param("key", "12345")

    # request4->execute(); # If we call execute here, it works in compile time but fails in runtime

    request4.set_body('{"name": "Aditya"}')
    request4.set_timeout(60)

    # The problem: what if we forgot to set an important field?
    request4.execute()
