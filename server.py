import socket

from http.request import HTTPRequest
from http.response import HTTPResponse
from routing.router import Router

HOST = "127.0.0.1"
PORT = 8080

def handle_connection(connec):
    raw_data = connec.recv(4096)

    if not raw_data:
        return
    
    try:
        raw_text = raw_data.decode("utf-8",errors = "replace")

        request = HTTPRequest(raw_text)

        handler = router.resolve(request.method,request.path)

        if handler is None:
            response = HTTPResponse(404, "Request not Found")
        else:
            response = handler(request)
    
    except Exception as e:
        print('Error handling request:',e)
        response = HTTPResponse(500,"Internal Server Error")

def run_server():
    print(f"Server running on http://{HOST}{PORT}")

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.bind((HOST,PORT))
        server.listen(1)

        while True:
            conn, addr = server.accept()
            handle_connection(conn)
            conn.close()

if __name__ == "__main__":
    run_server()


