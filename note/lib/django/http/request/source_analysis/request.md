## UnreadablePostError(OSError)

## RawPostDataException(Exception)

## HttpRequest
> [\__init__] setup  [self.GET], [self.POST], [self.COOKIE], [self.META], [self.FILES], [self.path], [self.path_info], [self.method], [self.resolver_match], [self.content_type], [self.content_params] to initial state (mostly `None`)

> [\__repr__]

> [header] a cached property, which return the result of [HttpHeaders(self.META)]

> [accepted_types] return a list of MediaType instances. 

> [accepts] return true if `media_type` matches any of [self.accepted_types]

> [_set_content_type_params] set [self.content_type], [self.content_params], [self.encoding] which are parsed from header.

> [_get_raw_host] (unsafe) return the HTTP host using the environment or request headers. Try `HTTP_X_FORWARDED_HOST` first, `HTTP_HOST` second, `SERVER_NAME` last.

> [get_host] (safe) return the HTTP host using the environment or request headers.

> [get_port] return the port number for the request as a string

> [get_full_path] call [self._get_full_path]

> [get_full_path_info] call [self._get_full_path] but provide [self.path_info]

> [_get_full_path] return the full path, format like `user?id=1`

> [get_signed_cookie] attempt to return a signed cookie. If the signature fails or the cookie has expired, raise an exception, unless the `default` arguemnt is provided, in which case return that value.

> [get_raw_url] return an absolute URI from variables available in this request. Skip allowed hosts protection.

> [build_absolute_uri] build an absolute URI from the location and the variables available in this request.

> [_current_scheme_host] a cached property, which return the scheme of current request

> [_get_scheme] just return `'http'`

> [scheme] get scheme (read it from [settings.SECURE_PROXY_SSL_HEADER] first, [self.META] second, [self._get_scheme] last).

> [is_secure] return turn if [self.scheme] equals https.

> [is_ajax] 

> [encoding] (property)

> [encoding] (setter) set the encoding used for GET/POST accesses. If the GET or POST dictionary has already been created, remove and recreate it on the next access. 

> [\_initialized_handlers] load uploadhandler from [settings.FILE_UPLOAD_HANDLERS] to [self._upload_handlers]. 

> [upload_handlers] (property) calls [self._initialized_handlers] if it is not set.

> [upload_handlers] (seter)

> [parse_file_upload] parse `post_data` using [MultiPartParser] to return return a tuple of (POST QueryDict, FILES MultiValueDict).

> [body] read body by calling [self.read] if [self._body] is not set.

> [_mark_post_parse_error] reset [self._post] and [self._files] to initial state.

> [_load_post_and_files] populate [self._post] and [self._files] if the content-type is a form type.

> [close] close all file object in [self._files.lists()].

> [read] return content read in [self._stream.read].

> [readline] return content read in [self._stream.readline]

> [__iter__] iterate [self.readline]

> [readlines] return `list[self]`


## HttpHeaders(django.utils.datastructures.CaseInsensitiveMapping)
* return a map which key are extracted `HTTP_` and replace `_` by `-` from `environ`. 


## QueryDict(django.utils.datastructures.MultiValueDict)
* a specialized MultiValueDict which represents a query string. A QueryDict can be used to represent GET or POST data. 

## MediaType


## bytes_to_text


## split_domain_port


## validate_host
* validate the given `host` against `allowed_hosts`


## parse_accept_header
* return a list of [MediaType] which parsed from header's `Accept` field.
