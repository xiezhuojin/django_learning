## get_internal_wsgi_application
* load and return the WSGI application as configured by the user in [settings.WSGI_APPLICATION]. With the default ``startproject`` layout, this will be the ``application`` object in ``projectname/wsgi.py``

## is_broken_pipe_error

## WSGIServer(simple_server.WSGIServer)
> [__init__] override to setup [self.allow_reuse_address]

## ThreadedWSGIServer(socketserver.ThreadingMixIn, WSGIServer)
* a threaded version of the WSGIServer with [daemon_threads] set to true

## ServerHandler(simple_server.ServerHandler)
> [__init__] wrap stdin into [LimitedStream(stdin, content_length)] so that unread request data will be ignored at the end of request.

> [closeup_headers] HTTP/1.1 requires support for persistent connections. Send `close` if the content length is unknown to prevent clients from reusing the connection.

> [close]

> [handle_error]

## WSGIRequestHandler(simple_server.WSGIRequestHandler)
> [address_string]

> [log_message]

> [get_environ] strip all headers with underscores in the name before constructing the WSGI environ. 

> [handle] override [simple_server.WSGIRequestHandler.handle] to keep handle request by calling [self.handle_one_request] util [self.close_connection] is set to true

> [handle_one_request] just like [simple_server.WSGIRequestHandler.handle]

## run
* setup wsgi server and it's app, then [serve_forever]
