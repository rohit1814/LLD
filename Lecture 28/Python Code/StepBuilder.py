class HttpRequest:
    def __init__(self):
        self.url = None
        self.method = None
        self.headers = {}
        self.query_params = {}
        self.body = None
        self.timeout = None

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


# Step interfaces (Python doesn't enforce interfaces, so we just document the flow)
class UrlStep:
    def with_url(self, url: str):
        raise NotImplementedError


class MethodStep:
    def with_method(self, method: str):
        raise NotImplementedError


class HeaderStep:
    def with_header(self, key: str, value: str):
        raise NotImplementedError


class OptionalStep:
    def with_body(self, body: str):
        raise NotImplementedError

    def with_timeout(self, timeout: int):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError


# Concrete step builder
class HttpRequestStepBuilder(UrlStep, MethodStep, HeaderStep, OptionalStep):
    def __init__(self):
        self.req = HttpRequest()

    # UrlStep
    def with_url(self, url: str) -> MethodStep:
        self.req.url = url
        return self

    # MethodStep
    def with_method(self, method: str) -> HeaderStep:
        self.req.method = method
        return self

    # HeaderStep
    def with_header(self, key: str, value: str) -> OptionalStep:
        self.req.headers[key] = value
        return self

    # OptionalStep
    def with_body(self, body: str) -> OptionalStep:
        self.req.body = body
        return self

    def with_timeout(self, timeout: int) -> OptionalStep:
        self.req.timeout = timeout
        return self

    def build(self) -> HttpRequest:
        if not self.req.url:
            raise RuntimeError("URL cannot be empty")
        return self.req

    # static method to start the builder
    @staticmethod
    def get_builder() -> UrlStep:
        return HttpRequestStepBuilder()


if __name__ == "__main__":
    step_request = (
        HttpRequestStepBuilder.get_builder()
        .with_url("https://api.example.com/products")
        .with_method("POST")
        .with_header("Content-Type", "application/json")
        .with_body('{"product": "Laptop", "price": 49999}')
        .with_timeout(45)
        .build()
    )

    step_request.execute()
