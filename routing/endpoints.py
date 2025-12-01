import json
from routing.router import route
from http_core.response import HTTPResponse
from storage.memory import database, add_record


@route("GET", "/")
def home(req):
    return HTTPResponse(200, "Welcome to the HTTP server!")


@route("GET", "/echo")
def echo(req):
    message = req.query.get("message", [""])[0]
    return HTTPResponse(200, message)


@route("POST", "/data")
def create(req):
    if "application/json" not in req.headers.get("content-type", ""):
        return HTTPResponse(400, "Expected application/json")

    try:
        payload = json.loads(req.body)
    except:
        return HTTPResponse(400, "Invalid JSON")

    record = add_record(payload)
    return HTTPResponse(201, json.dumps(record), "application/json")


@route("GET", "/data")
def get_all(req):
    return HTTPResponse(200, json.dumps(database), "application/json")
