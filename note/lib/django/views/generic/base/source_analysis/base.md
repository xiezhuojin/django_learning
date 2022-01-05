## logger
* ```logger  = logging.getLogger("django.request")

## ContextMixin
* A default context mixin that passes the keyword arguments received [get_content_data] as the template context.

> [get_context_data] update ```kwargs``` with setting `view` to `self`, and [self.extra_context]

## View
* intentionally simple parent class for all views. Only implements dispatch-by-method and simple sanity checking.

> [http_method_names] equals ```["get", "post", "put", "patch", "delete", "head", "options"]```

> [\__init__] go through keyword arguments, and either save their values to our instance, or raise an error.
* called in the URLconf; can contain helpful extra keywork arguments, and other things.

> [as_view]
* main entry point for a request-response process.

> [setup]
* initialize attributes shared by all view methods.

> [dispatch]
* try to dispatch to the right method; if a method doesn't exist, defer to the error handler. Also defer to the error handler if the request method isn't on the approved list.

> [http_method_not_allowed]
* log method not allowed, then return a `HttpResponseNotAllowed` response.

> [options]
* handle responding to requests for the OPTIONS HTTP verb.

> [\_allowed_methods]
* just return `self.http_method_names` as a list if each of them has the corresponding method.

## TemplateResponseMixin
* a mixin that can be used to render a template
> [template_name] ```= None```
> [template_engine] ```= None```
> [response_class] ```= TemplateResponse```
> [content_type] ```= None```

> [render_to_response]
* return a response, using the [response_class] for this view, with template rendered with the given context. pass ```response_kwargs``` to the constructor of the response class.

> [get_template_names]
* return a list of template names to be used for the request. Must return a list. May not be called if [render_to_response] is overridden.

## TemplateView(TemplateResponseMixin, ContextMixin, View)
* render a template. Pass keyword arguments from the URLconf to the context.
> [get] get `context` from [get_context_data](**kwargs), then return [render_to_response](`context`).

## RedirectView(View)
* provide a redirect on any GET request.
> [permanent] ```= False```
> [url] ```= None```
> [pattern_name] ```= None```
> [query_string] ```= False```

> [get_redirect_url]
* return the URL redirect to. Keyword arguments from the URL pattern match generating the redirect request are provided as kwargs to this method.

> [get]
* return ```HttpResponsePermanentRedirect```, ```HttpResponseRedirect```, or ```HttpResponseGone``` base on ```url```.

> [head] ```return self.get(request, *args, **kwargs)```
> [post] ```return self.get(request, *args, **kwargs)```
> [options] ```return self.get(request, *args, **kwargs)```
> [delete] ```return self.get(request, *args, **kwargs)```
> [put] ```return self.get(request, *args, **kwargs)```
> [patch] ```return self.get(request, *args, **kwargs)```
