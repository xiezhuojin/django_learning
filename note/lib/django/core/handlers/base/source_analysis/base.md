## BaseHandler
> [_view_middleware] (class variable)

> [_template_response_middleware] (class variable)

> [_exception_middleware] (class variable)

> [_middleware_chain] (class variable)

> [load_middleware] import middleware from `settings.MIDDLEWARE` in reversed order; figure out middleware is sync or async; append them to [self._view_middleware], [self._template_response_middleware], [self._exception_middleware] base ont their's attribute e.g. `process_view`, `process_template_response`, `process_exception`. 
* populate middleware lists from settings.MIDDLEWARE.
* must be called after the environment is fixed (see \__call__ in subclasses)

> [adapt_method_mode]
* adapt a method to be in the correct "mode" (sync or async).

> [get_response] first setup default url resolver for current thread, then call [self._middleware_chain] with `HttpRequest`, which return `HttpResponse`.
* return an HttpResponse object for the given HttpRequest.

> [get_response_async]
* asynchronous version of [get_response].

> [\_get_response] (INNER CORE OF get_response) try to resolve the request, apply view middleware (if middleware return a response, end of the function); wrap `callback` with [self.make_view_atomic]; and wrap `wrapped_callback` if it's a async function; call that wrapped wrapped callback (if there is an exception, calls [self.process_exception_by_middleware] to handle request); if the response supports deferred rendering, apply [self._template_response_middleware] to render the response. At last, return response.
* resolve and call the view, the apply view, exception, and template_response middleware. This method is everything that happens inside the request/response middleware.

> [\_get_response_async] basically the same as [\_get_response], but with async `middleware method`.
* resolve and call the view, then apply view, exception, and template_response middleware. This method is everything that happens inside the request/response middleware.

> [resolve_request] (THIS IS WHERE THE URL GET RESOLVED!) first get `resolver` from `request` if exists, otherwise get current thread's `resolver`. resolve `request.path_info` against `resolver`, then return the match object. (view function with its args and kwargs).
* retrieve/set the urlconf for the request. Return the view resolved, with its args and kwargs.

> [check_response]
* raise an error if the view return None or an uncalled coroutine.

> [make_view_atomic]
* make every database operation in `view` function atomic. (by using transaction).

> [process_exception_by_middleware]
* pass the exception to the exception middleware. If no middleware return a response for this exception, return None.

## reset_urlconf
* reset the URLconf after each request is finished.
