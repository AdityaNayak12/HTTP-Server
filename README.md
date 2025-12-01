# Custom Python HTTP Server

This project is a basic HTTP server built **without using any web framework**.  
Everything (parsing, routing, responses, etc.) is written manually using Python sockets.  
The goal was to understand how HTTP works under the hood instead of relying on tools like Flask or FastAPI.

---

## Features

- Runs on a configurable port (default: `8080`)
- Parses request lines, headers, and body manually
- Generates proper HTTP/1.1 responses
- Simple routing system
- Supports query params
- Can receive JSON data and store it in memory
- Returns stored data as JSON
- Can serve static files from a `/static` folder
- Basic request logging

---

## Endpoints

### `GET /`

Returns a simple welcome message.

Example:

```bash
curl http://localhost:8080/
```

---

### `GET /echo?message=XYZ`

Reads the `message` query parameter and sends it back.

Example:

```bash
curl "http://localhost:8080/echo?message=hello"
```

Response:

```
hello
```

---

### `POST /data`

Stores JSON into memory and assigns an ID.

Headers required:

```
Content-Type: application/json
```

Example:

```bash
curl -X POST http://localhost:8080/data \
     -H "Content-Type: application/json" \
     -d '{"name":"Aditya"}'
```

Example response:

```json
{"name":"Aditya","id":1}
```

---

### `GET /data`

Returns all stored JSON values.

Example:

```bash
curl http://localhost:8080/data
```

Example response:

```json
[
  {"name":"Aditya","id":1}
]
```

---

### `GET /static/<filename>`

Serves files from the `static/` folder.  
For example, if you have:

```
static/index.html
```

Then:

```bash
curl http://localhost:8080/static/index.html
```

will return that file.

---

## Folder Structure

```
HTTP-Server/
│
├── server.py
│
├── http_core/
│   ├── request.py
│   ├── response.py
│   ├── status_codes.py
│   └── __init__.py
│
├── routing/
│   ├── router.py
│   ├── endpoints.py
│   └── __init__.py
│
├── storage/
│   ├── memory.py
│   └── __init__.py
│
└── static/
    └── index.html
```

---

## How to Run

Open a terminal and run:

```bash
cd HTTP-Server
python3 server.py
```

You should see:

```
Server running at http://127.0.0.1:8080
```

Then test using curl (examples above).

---

## Why it’s Built This Way

- Each part of the server is in its own file so it's easier to understand.
- The routing uses a decorator (`@route(...)`) which feels similar to modern frameworks.
- The request parser uses `\r\n\r\n` to separate headers and body (the actual HTTP standard).
- Responses include headers like `Content-Length`, `Date`, and a proper status line so clients interpret messages correctly.

---
