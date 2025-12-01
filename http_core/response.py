from email.utils import formatdate
from .status_codes import STATUS_CODES


class HTTPResponse:
    def __init__(self, status_code=200, body="", content_type="text/plain", headers=None):
        self.status_code = status_code
        self.reason = STATUS_CODES.get(status_code, "Unknown")

        self.body = body.encode("utf-8") if isinstance(body, str) else body

        self.headers = {
            "Content-Type": content_type,
            "Content-Length": str(len(self.body)),
            "Date": formatdate(usegmt=True),
            "Connection": "close",
            "Access-Control-Allow-Origin": "*"
        }

        if headers:
            self.headers.update(headers)

    def to_bytes(self):
        head = f"HTTP/1.1 {self.status_code} {self.reason}\r\n"
        head += "".join(f"{k}: {v}\r\n" for k, v in self.headers.items())
        head += "\r\n"

        return head.encode("utf-8") + self.body
