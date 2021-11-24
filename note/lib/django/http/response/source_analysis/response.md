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


## StreamHttpResponse(HttpResponseBase)


## FileResponse(StreamingHttpResponse)


## HttpResponseRedirectBase(HttpResponse)


## HttpResponseRedirect(HttpResponseRedirectBase)


## HttpResponsePermanentRedirect(HttpResponseRedirectBase)


## HttpResponseNotModified(HttpResponse)


## HttpResponseBadRequest(HttpResponse)


## HttpResponseNotFound(HttpResponse)


## HttpResponseForbidden(HttpResponse)


## HttpResponseNotAllowed(HttpResponse)


## HttpResponseGone(HttpResponse)


## HttpResponseServerError(HttpResponse)


## Http404(Exception)


## JsonResponse(HttpRequest)
