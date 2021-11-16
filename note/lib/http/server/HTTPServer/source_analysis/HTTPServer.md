### HTTPServer(socketserver.TCPServer)
* override server_bind to store server name and port

## ThreadingHTTPServer(socket.server.ThreadingMixIn, HTTPServer)
* set new thread in daemon mode

## BaseHTTPRequestHandler(socketserver.StreamRequestHandler)
