## BaseServer
* when a request comes in, a RequestHandlerClass get initiated, then handler that request. It's get_request returns ("request", request address, self).
* every time it handles a request, it close that request.

## TCPServer(BaseServer)
* it's get_request method return (file descriptor, request address)

## UDPServer(TCPServer)
* protocol are different from TCPServer, it's get_request returns (data, request address)

## ForkingMixin
* it forks a process to handle that request (this could be expensive)

### _Threads(list)
### _NoThreads

## ThreadsMixin
* handle request in new thread, set new thread in daemon and wait for them according to it's settings.

## BaseRequestHandler
## StreamRequestHandler(BaseRequestHandler)
* create read file (buffered) and write (unbuffered) file from connection (request)

## _SocketWriter(io.BufferIOBase)

### DatagramRequestHandler(BaseRequestHandler)
* wrap request (datagram) into read/write file
