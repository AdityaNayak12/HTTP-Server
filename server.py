import socket
import os

from http_core.request import HTTPRequest
from http_core.response import HTTPResponse
from routing.router import router
import routing.endpoints


HOST = "127.0.0.1"
PORT = 8080


def log(message):
    print(f"[LOG] {message}")


def serve_static(path):
    file_path = os.path.join("static", path.replace("/static/", "", 1))

    if not os.path.exists(file_path):
        return HTTPResponse(404, "File Not Found")

    with open(file_path, "rb") as f:
        return HTTPResponse(200, f.read(), "text/html")


def handle_connection(conn):
    data = conn.recv(4096)

    if not data:
        return

    text = data.decode("utf-8", errors="replace")

    try:
        req = HTTPRequest(text)
        log(f"{req.method} {req.path}")

        if req.path.startswith("/static/"):
            response = serve_static(req.path)
        else:
            handler = router.resolve(req.method, req.path)
            response = handler(req) if handler else HTTPResponse(404, "Route Not Found")
    except Exception as e:
        print("Error:", e)
        response = HTTPResponse(500, "Internal Server Error")

    conn.sendall(response.to_bytes())


def run():
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            log(f"Connection from {addr}")
            handle_connection(conn)
            conn.close()


if __name__ == "__main__":
    run()
