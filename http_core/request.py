from urllib.parse import urlsplit, parse_qs


class HTTPRequest:
    def __init__(self, raw_request: str):
        self.raw = raw_request

        self.method = None
        self.path = None
        self.query = {}
        self.version = None
        self.headers = {}
        self.body = ""

        self._parse()

    def _parse(self):
        if "\r\n\r\n" not in self.raw:
            raise ValueError("Malformed HTTP Request")

        header_part, body_part = self.raw.split("\r\n\r\n", 1)
        lines = header_part.split("\r\n")

        self._parse_request_line(lines[0])
        self._parse_headers(lines[1:])

        if "content-length" in self.headers:
            length = int(self.headers["content-length"])
            self.body = body_part[:length]

    def _parse_request_line(self, line):
        method, target, version = line.split(" ", 2)
        url = urlsplit(target)

        self.method = method
        self.path = url.path
        self.query = parse_qs(url.query)
        self.version = version

    def _parse_headers(self, header_lines):
        for line in header_lines:
            if not line:
                continue
            key, value = line.split(":", 1)
            self.headers[key.strip().lower()] = value.strip()
