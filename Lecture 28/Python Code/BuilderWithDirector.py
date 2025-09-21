

from typing import Dict, Optional


class HttpRequest:
    def __init__(self, url: str, method: str, headers: Dict[str, str],
                 query_params: Dict[str, str], body: str, timeout: int):
        self.url = url
        self.method = method
        self.headers = headers
        self.query_params = query_params
        self.body = body
        self.timeout = timeout

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


class HttpRequestBuilder:
    def __init__(self):
        self._url: Optional[str] = None
        self._method: Optional[str] = None
        self._headers: Dict[str, str] = {}
        self._query_params: Dict[str, str] = {}
        self._body: str = ""
        self._timeout: Optional[int] = None

    def with_url(self, url: str):
        self._url = url
        return self

    def with_method(self, method: str):
        self._method = method
        return self

    def with_header(self, key: str, value: str):
        self._headers[key] = value
        return self

    def with_query_param(self, key: str, value: str):
        self._query_params[key] = value
        return self

    def with_body(self, body: str):
        self._body = body
        return self

    def with_timeout(self, timeout: int):
        self._timeout = timeout
        return self

    def build(self) -> HttpRequest:
        if not self._url:
            raise ValueError("URL cannot be empty")

        return HttpRequest(
            url=self._url,
            method=self._method or "GET",
            headers=dict(self._headers),
            query_params=dict(self._query_params),
            body=self._body,
            timeout=self._timeout or 30,
        )


class HttpRequestDirector:
    @staticmethod
    def create_get_request(url: str) -> HttpRequest:
        return (
            HttpRequestBuilder()
            .with_url(url)
            .with_method("GET")
            .build()
        )

    @staticmethod
    def create_json_post_request(url: str, json_body: str) -> HttpRequest:
        return (
            HttpRequestBuilder()
            .with_url(url)
            .with_method("POST")
            .with_header("Content-Type", "application/json")
            .with_header("Accept", "application/json")
            .with_body(json_body)
            .build()
        )


# --- Usage ---
if __name__ == "__main__":
    # Normal Request
    normal_request = (
        HttpRequestBuilder()
        .with_url("https://api.example.com")
        .with_method("POST")
        .with_header("Content-Type", "application/json")
        .with_header("Accept", "application/json")
        .with_query_param("key", "12345")
        .with_body('{"name": "Aditya"}')
        .with_timeout(60)
        .build()
    )
    normal_request.execute()

    print("\n----------------------------\n")

    # GET Request
    get_request = HttpRequestDirector.create_get_request("https://api.example.com/users")
    get_request.execute()

    print("\n----------------------------\n")

    # JSON POST Request
    post_request = HttpRequestDirector.create_json_post_request(
        "https://api.example.com/users",
        '{"name": "Aditya", "email": "aditya@example.com"}',
    )
    post_request.execute()
