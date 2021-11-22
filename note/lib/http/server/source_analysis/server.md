## HTTPServer(socketserver.TCPServer)
* override server_bind to store server name and port

## ThreadingHTTPServer(socket.server.ThreadingMixIn, HTTPServer)
* set new thread in daemon mode

## BaseHTTPRequestHandler(socketserver.StreamRequestHandler)
> [parse_request] is used to parse the request, it returns true for successfully parse the request, false for failure. If it change self.close_connection, caller will end the request connection (this is for keep-alive connection).

> [handle_one_request] reads all bytes from rfile (can get blocked), parse the request, after that it will get the command then call do_command method. 

> [handle] is the method who handles the request. It first set self.close_connection to true, then call [handle_one_request]. If callee set self.close_connection to false, handle will never call [handle_one_request] any more.

> [send_error]

> [send_response] add the response header to the headers buffer and log the response code. IT DOES NOT SEND THE BACK THE RESPONSE!!!

> [send_response_only] sends a MIME header to the headers buffer, it changes self.close_connection if keyword is "connection".

> [end_headers] end the headers buffer by appending CRLF to it's end. then call [flush_headers].

> [flush_headers] it just send the header buffer the clean it.

> [log_message] it just send messages to STDERR.

## SimleHTTPRequestHandler(BaseHTTPRequestHandler)
* simple http request handler with GET and HEAD commands. This serves files from given directory (current working directory if not specified) and any of its subdirectories. 

## _url_collapse_path

## executable
* test given path is executable

## CGIHTTPRequestHandler(SimpleHTTPRequestHandler)
* complete http server with GET, HEAD, and POST commands.
> [run_cgi] execute a CGI script

## \__main__
* run cgi or directory server
