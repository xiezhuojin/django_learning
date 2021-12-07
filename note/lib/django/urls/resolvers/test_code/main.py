from django.urls.resolvers import _route_to_regex, URLResolver
from django.urls.conf import path, include


urlconf = [
    path("/hi", [path("/index"), say_hi]),
]

def say_hi():
    print("hello, world")

def test_route_to_regex():
    regex = _route_to_regex("/book/<int:id>")
    print(regex)

def test_URLResolver_resolve():
    pass

def test_URLResolver_reverse():
    pass

if __name__ == "__main__":
    test_route_to_regex()
    test_URLResolver_resolve()
    test_URLResolver_reverse()
