# check pythonic version of immutablility
# dataclass and frozen=True
# property decorator for getters

# Target Class
class HttpRequest:
    def __init__(self):
        self.url = None
        self.method = None
        self.headers = {}
        self.query_params = {}
        self.body = ""
        self.timeout = None

    def execute(self):
        if not self.url:
            raise ValueError("URL cannot be empty")

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

# Builder Class
class HttpRequestBuilder:
    def __init__(self):
        self.req = HttpRequest()

    # Method chaining with reference return type so that we can chain multiple calls
    def with_url(self, url):
        self.req.url = url
        return self

    def with_method(self, method):
        self.req.method = method
        return self

    def with_header(self, key, value):
        self.req.headers[key] = value
        return self

    def with_query_param(self, key, value):
        self.req.query_params[key] = value
        return self

    def with_body(self, body):
        self.req.body = body
        return self

    def with_timeout(self, timeout):
        self.req.timeout = timeout
        return self

    # Build method to create the immutable HttpRequest object
    # Performs validation at one place --> Resolves the Scatter-Validation problem
    def build(self):
        # Validation logic can be added here
        if not self.req.url:
            raise ValueError("URL cannot be empty")
        if not self.req.method:
            self.req.method = "GET"  # Default method
        if not self.req.timeout:
            self.req.timeout = 30  # Default timeout
        return self.req


# --- Usage ---
if __name__ == "__main__":

    # Reason for using so many with_x methods with dot(.) --> because each method returns the builder object itself
    request = (
        HttpRequestBuilder()
        .with_url("https://api.example.com")
        .with_method("POST")
        .with_header("Content-Type", "application/json")
        .with_header("Accept", "application/json")
        .with_query_param("key", "12345")
        .with_body('{"name": "Aditya"}')
        .with_timeout(60)
        .build()    # Build method converts the builder object to the HttpRequest object at the end, 
                    # If we don't call build(), we will have a builder object instead of HttpRequest object
                    # Also called as Termination Method
    )

    request.execute()

    request2 = (
        HttpRequestBuilder()
        .with_url("https://api.example.com/users")
        .with_method("GET")
        .with_query_param("page", "1")
        .build()
    )
