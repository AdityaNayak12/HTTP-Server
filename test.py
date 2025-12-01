from http_core.status_code import STATUS_CODE
from http_core.request import HTTPRequest

# print(STATUS_CODE[200])
# print(STATUS_CODE[404])

raw = (
    "GET /echo?message=hello HTTP/1.1\r\n"
    "Host: localhost\r\n"
    "\r\n"
)
req = HTTPRequest(raw)

print(req.method)   # GET
print(req.path)     # /echo
print(req.query)    # {'message': ['hello']}
print(req.version)  # HTTP/1.1


