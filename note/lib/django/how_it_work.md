## How request pass down to view function?(how django route?)
    * django.core.handlers.base.BaseHandler is the base handle function

    * urls.py from project is a list of URLPattern object.
    * how URLPattern and RoutePattern(RegexPattern) works?
        URLPattern
    * how to handle a list of URLPattern to get the route done?
        BaseHandler (WSGIHandler, ASGIHandler inherit it), has a function called get_resolver (it reads from setting, default is URLResolver), match url path against Pattern, then return a match object.