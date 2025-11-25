from routing.router import route
from http.response import HTTPResponse
from storage.memory import database, add_record
import json

@route("GET","/")

def home(request):
    return HTTPResponse(200,"Welcome to HTTP Server")


@route("GET","/echo")

def echo(request):
    message = request.qurey.get("message",[""])[0]
    return HTTPResponse(200,message)

@route("POST","/data")

def create_data(request):
    content_type = request.header.get("content-type","")
    if "application/json" not in content_type:
        return HTTPResponse(400,"Expected JSON")
    
    try:
        body_json = json.loads(request.body)
    except:
        return HTTPResponse(400,"Invalid JSON")
    
    record = add_record(body_json)

    response_body = json.dumps({"success":True,"id":record["id"]})
    return HTTPResponse(201,response_body,content_type = "application/json")

@route("GET","/data")

def list_data(request):
    return HTTPResponse(200, json.dumps(database),"application/json")


