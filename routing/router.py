from typing import Dict, Tuple, Callable
from http.response import HTTPResponse

class Router:

    def __inti__(self):
        self.routes: Dict[Tuple[str,str],callable] = {}

    def add_route(self,method:str, path:str,handler:Callable):
        self.routes[method.upper(),path] = handler
    
    def resolve(self, method:str, path:str):
        return self.routes.get((method.upper(),path,None))
    

router = Router()

def route(method,path):

    def wrapper(func):
        router.add_route(method,path,func)
        return func
    
    return wrapper

