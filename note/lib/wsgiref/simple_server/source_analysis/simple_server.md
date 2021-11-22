## ServerHandler(wsgiref.handlers.SimpleHandler)
> [close] 

## WSGIServer(http.server.HTTPServer)
> [server_bind] override server_bind to store environment by calling [setup_environ]

> [setup_environ] set up base environment, for example: SERVER_NAME, GATEWAY_INTERFACE.

> [get_app]

> [set_app]

## WSGIRequestHandler(http.server.BaseHTTPRequestHandler)
> [get_environ] returns env which is extract from it's parent's attribute, for example: self.command, self.headers

> [get_stderr]

> [handle] handle a single http request. It firsts read bytes from "request", parse it (just like it's parent). After that it initiates [ServerHandler], call it's [run] method by passing [self.server.getapp()] the handle the request.
