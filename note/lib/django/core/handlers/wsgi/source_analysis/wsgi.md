## LimitedStream
* wrap another stream to disallow reading it past a number of bytes

## WSGIRequest(django.http.HttpRequest)
> [\__init__] setup some instance variable (most of them are not that important, except [self._stream] (LimitedStream), [self._read_started] (set to `False`), [self.resolver_match] (set to `None`))

> [\_get_scheme]

> [GET] return a dictionary like object by reading `QUERY_STRING` in [self.environ].

> [\_get_post] return [self._post] (call [self._load_post_and_files] if it don't exist).

> [\_set_post] 

> [COOKIES] return cookies (dictionary like) by reading `HTTP_COOKIE` in [self.environ].

> [FILES] return [self._files] (call [self._load_post_and_files] if it don't exist).

* POST = property(_get_post, _set_post)

## WSGIHandler(django.core.handlers.base.BaseHandler)
> [\__init__] extend [super().__init__] by loading middleware.

> [\__call__] (the same signature as WSGI app).
* set script prefix
* send request_started signed (basically do nothing)
* get request by initiating  request class
* get response (by calling [self.get_response(request)])
* send status, response header
* return response

## get_path_info
* return the HTTP request's PATH_INFO as a string.

## get_script_name

## get_bytes_from_wsgi
* get a value form the WSGI environ dictionary as bytes (encoded in iso-8859-1).

## get_str_from_wsgi
* get a value from the WSGI environ dictionary as str (by calling [get_bytes_from_wsgi] then decode it).
