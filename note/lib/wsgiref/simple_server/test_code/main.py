from wsgiref.simple_server import WSGIServer, WSGIRequestHandler, demo_app


if __name__ == "__main__":
    server = WSGIServer(("0.0.0.0", 8000), WSGIRequestHandler, True)
    server.set_app(demo_app)
    server.serve_forever()
