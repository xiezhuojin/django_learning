## ResponseHeaders(django.utils.datastructures.CaseInsensitiveMapping)
> [\__init__]

> [\_convert_to_charset] convert headers key/value to ascii/latin-1 native strings.

> [\__delitem__]

> [\__setitem__]
* convert `key` and `value` to specific charset (ascii for `key`, `latin-1` for value)

> [pop]

> [setdefault]


## BadHeaderError(ValueError)


## HttpResponseBase
* An http response base class with dictionary-accessed headers. This class doesn't handle content. It should not be used directly. Use the HttpResponse and StreamingHttpResponse subclasses instead.
* This is also a file like object. 
> [\__init__] setup [self.headers], [self._charset], [self.headers['Content-Type]], [self._handler_class], [self.cookies], [self.closed], [self.status_code], [self._reason_phrase].

> [reason_phrase] (property)

> [reason_phrase] (setter)

> [charset] return [self._charset] if it is set, otherwise return charset base on the content type's charset in [settings.DEFAULT_CHARSET].

> [charset] (setter)

> [serialize_headers] HTTP headers as a bytestring

> [\_content_type_for_repr]

> [\__setitem__] set [self.headers[`header`] to `value`]

> [\__delitem__] opposite of [\__setitem__].

> [\__getitem__] return [self.headers[`headers`]].

> [has_header]

> [item] return [self.headers.items()]

> [get] just like [\__getitem__] but with a default value.

> [set_cookie] set a cookie

> [setdefault] set a header unless it has already been set.

> [set_signed_cookie] set a cookie with sign.

>[delete_cookie] ask browser to delete cookie (by setting cookie's expires to UNIX Epoch).

> [make_bytes] turn a value into a bytestring encoded in the output charset. 

> [close] called by WSGI server. What it does is call every closer in [self._resource_closers], then clear [self._resource_closers]; set [self.closed] to `true` then signal [self._handler_class] to request has been finished.

> [write] just raise `OSEeeor`.

> [flush] do nothing.

> [tell] raise `OSError`

> [readable] return `False`.

> [seekable] return `False`

> [writable] return `False`

> [writelines] raise `OSError`


## HttpResponse(HttpResponseBase)
* An HTTP response class with a string as content. This content cna be read, appended to, or replaced.
> [\__init__] extend super's \__init__ constructor, and add `content` to [self.content] (which is a bytestring).

> [\__repr__]

> [serialize] return [self.serialize_headers() + b'\r\n\r\n' + self.content], which is full HTTP message, including headers, as a bytestring. 

> [content] (property)

> [\__iter__]

> [write] append `content` to [self._container].

> [tell] return the length of [self.content]

> [getvalue] return [self.content]

> [writable] return `True`

> [writelines] call [self.write] with lines.


## StreamHttpResponse(HttpResponseBase)
* a streaming HTTP response class with an iterator as content. 
> [\__init__] extend super's \__init__ constructor, and add `streaming_content` to [self.streaming_content].

> [content] (property) raise an `AttributeError` by saying has no content.

> [streaming_content] (property)

> [streaming_content] (setter) create an iterable for `value`, and set [self._iterator].

> [\__iter__] return [self.streaming_content]

> [getvalue] basically return [self.streaming_content].


## FileResponse(StreamingHttpResponse)
* a streaming HTTP response class optimized for files.
> [\__init__] extend super's \__init__ constructor, and setup [self.as_attachment], [self.filename]

> [\_set_streaming_content] setup [set_headers], and calls [super()._set_streaming_content] to setup file like iterable. 

> [set_headers] set some common response headers (Content-Length, Content-Type, and Content-Disposition) base on the `filelike` response content.


## HttpResponseRedirectBase(HttpResponse)
> [\__init__] extend super's \__init__ constructor, and setup [self['Location']] to `redirect_to` if target's scheme is in [self.allowed_schemes].

> [\__repr__]


## HttpResponseRedirect(HttpResponseRedirectBase)
* status_code = 302


## HttpResponsePermanentRedirect(HttpResponseRedirectBase)
* status_code = 301


## HttpResponseNotModified(HttpResponse)
* status_code = 304
> [\__init__] delete [self.['content-type']] beside extend super's \__init__constructor.


## HttpResponseBadRequest(HttpResponse)
* status_code = 400


## HttpResponseNotFound(HttpResponse)
* status_code = 404


## HttpResponseForbidden(HttpResponse)
* status_code = 403


## HttpResponseNotAllowed(HttpResponse)
* status_code = 405
> [\__init__] setup [self.['Allow']] to `permitted_methods` beside extend super's \__init__constructor.


## HttpResponseGone(HttpResponse)
* status_code = 410


## HttpResponseServerError(HttpResponse)
* status_code = 500


## Http404(Exception)


## JsonResponse(HttpRequest)
* an http response class that consumes data to be serialized to JSON.
> [\__init__] what difference from super's \__init__ is it put serialized JSON data to [super().\__init__] and setup corresponding headers.
