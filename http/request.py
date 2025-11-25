from urllib.parse import urlsplit, parse_qs

class HTTPRequest:
    def __init__(self, raw_req: str):
        self.raw = raw_req
        self.method = None
        self.path = None
        self.query = {}
        self.version = None

        self.header = {}
        self.body = ""

        self.parse()

    def parse(self):
        if "r\n\r\n" in self.raw:
            header_part, body_part = self.raw.split("r\n\r\n",1)
        else:
            raise ValueError("Malformed HTTP Request")

        lines = header_part.split("r\n")

        self.parse_request_line(lines[0]) #parsing request line

        self.parse_request_line(lines[1:]) #parsing header

        if "content-length" in self.header:
            expectedLen = int(self.header["content-length"])
            self.body = body_part[: expectedLen]
        

    def parse_request_line(self):
        first_line = self.raw.split("\r\n",1)[0]
        method,version,target = first_line.split(" ",2)

        url = urlsplit(target)

        self.method = method
        self.path = url.path
        self.query = parse_qs(query)
        self.version = version
    

    def parse_headers(self, header_lines):
        for line in header_lines:
            if not line:
                continue

            if ":" not in line:
                raise ValueError(f"Malformed line: {line}")
            
            name,value = line.split(":",1)
            self.header[name.strip().lower()] = value.strip()

    def repr(self):
        return f"<HTTPRequest {self.method} {self.path} header = {len(self.header)}>"

