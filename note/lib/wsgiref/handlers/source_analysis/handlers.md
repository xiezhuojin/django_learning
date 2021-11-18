## BaseHandler
> [run] this part handle to request, but instead of handling itself, it first setup the environment. then lets [application] to handle the request. [application] has the same function signature as django or flask does. After getting the result from [application] which is a file like object. It flushes the result, then calls [self.finish_response].

> [setup_environ] setup [self.environ].

> [finish_response] send any iterable data (result from application), closes it if needed. After that, call [self.close].

> [get_scheme]

> [cleanup_headers]

> [start_response] callable as specified by PEP 3333, which is a the second argument for application.

> [send_preamble] transmit version/status/date/server version, via self._write

> [write] callable as specified by PEP 3333. which the the called in application. it first sends headers, then sends the data application passes it.

> [finish_content]

> [close] close the iterable and reset all instance variables, for example: [self.result], [self.headers], [self.status], [self.environ]

> [send_headers] transmit headers to client by calling [self._write]

> [result_is_file]

> [client_is_modern]

> [log_exception]

> [handle_error]

> [error_output] WSGI mini-app to create error output

> [_write] (NOT IMPLEMENTED)

> [_flush] (NOT IMPLEMENTED)

> [_get_stdin] (NOT IMPLEMENTED)

> [_get_stderr] (NOT IMPLEMENTED)

> [_get_add_cgi_vars] (NOT IMPLEMENTED)


## SimpleHandler(BaseHandler)
> [get_stdin]

> [get_stderr]

> [add_cgi_vars]

> [_write] uses [self.stdout.write] to write the data

> [_flush]


## BaseCGIHandler(SimpleHandler)
    * just set origin_server to false, then do nothing


## IISCGIHandler(BaseCGIHandler)
    * basely do nothing
