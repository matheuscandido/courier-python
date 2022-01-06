class Request:
    def __init__(self, name: str, method: str, url: str, headers: dict[str, str], body: str) -> None:
        self.name = name
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body    