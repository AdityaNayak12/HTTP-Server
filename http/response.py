from email.utils import formatdate
from .status_code import STATUS_CODE


class HTTPResponse:
    def __init__(self, status_code=200,body="",content_type = "text/plain",header = None):
        self.status_code = status_code
        self.reason = STATUS_CODE.get(status_code, "Unknown status")

        if isinstance(body,str):
            self.body = body.encode("utf-8")
        else:
            self.body = body


        self.header = {
            "Content-Type": content_type,
            "Content-length": str(len(self.body)),
            "Date": formdate(timeval = None, usegmt = "true"),
            "Connection": "close",
        }

        if header:
            for k,v in header.item():
                self.header[k] = v
        
        def t0_bytes(self):

            status_line = f"HTTP/1.1 {self.status_code} {self.reason}\r\n"
            header_line = ""

            for key, value in self.header.items():
                header_line+= f"{key}: {value}\r\n"
            
            return (status_line+header_line+"\r\n").encode("utf-8")+self.body
        