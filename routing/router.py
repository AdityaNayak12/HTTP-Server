from typing import Callable, Dict, Tuple

class Router:
    def __init__(self):
        self.routes: Dict[Tuple[str, str], Callable] = {}

    def add_route(self, method, path, handler):
        self.routes[(method.upper(), path)] = handler

    def resolve(self, method, path):
        return self.routes.get((method.upper(), path))


router = Router()


def route(method, path):
    def wrapper(func):
        router.add_route(method, path, func)
        return func
    return wrapper
