this module converts requests URLs to callback view functions.

URLResolver is the main class here. Its resolve() method take a URL (as a string) and returns a ResolverMatch object which provides access to all attribute of the resolved URL match.

## ResolverMatch
> [\__init__] setup instance variables. Some important variables is [self.func], [self.args], [self.kwargs], [self.url_name].

> [\__getitim__]

> [\__repr__]

## get_resolver
* return resolver from current thread

## _get_cached_resolver
* return a `URLResolver` object by providing `urlconf`.

## get_ns_resolver
* build a namespaced resolver for the given parent URLconf pattern. This makes it possible to have captured parameters in the parent URLconf pattern.

## LocaleRegexDescriptor
* return locale version of regular expression pattern.

## CheckURLMix
> [describe]
* format the URL pattern for display in warning messages.

> [\_check_pattern_startswith_slash]
* check whether regex pattern begins with a forward slash.

## RegexPattern(CheckURLMixin)
> [\__init__] setup some instance variable [self._regex], [self._regex_dict], [self._is_endpoint], [self.name], [self.converters],

> [match] match given path against [self.regex]. If matched, return the `kwargs`, `args`, `path` extracted from that match object. Otherwise, `None`.

> [check]
* check regex pattern is startswith slash or with trailing doller. Then return `warnings`.

> [\_check_include_trailing_dollar]
* check whether regex pattern ends with dollar sign.

> [\_compile]
* compile and return the given regular expression.

## _PATH_PARAMETER_COMPONENT_RE
* regular expression of r'<(?:(?P<converter>[^>:]+):)?(?P<parameter>[^>]+)>', it matches pattern like this `<int>age`.

## _route_to_regex
* convert a patch pattern into a regular expression. Return the regular expression and a dictionary mapping the capture names to the converter. For example, 'foo/<int:pk>' returns '^foo\\/(?P<pk>p[0-9]+)` and `{'pk': <django.urls.converters.IntConverter>}`.
* it searches `_PATH_PARAMETER_COMPONENT_RE` against `route` til the end of `route`. if it found a match, append the matched part to `parts` and put `parameter`: `converter` to `converters` (which is a map).

## RoutePattern(CheckURLMixin)
> [\__init__] setup some instance variable. e.g. [self._route], [self._regex_dict], [self._is_endpoint], [self.name], [self.converters].

> [match]
* match `path` against [self.regex], if there is a match return `path[match.end():], (), kwargs`.

> [check]
* return warning (just like [RegexPattern.check])

> [\_compile]
* return the first part of [_route_to_regex] (which is the regular expression of `route`).

## LocalePrefixPattern
* not that important

## URLPattern
> [\__init__] setup instance variable. e.g. [self.pattern], [self.callback], [self.default_args], [self.name].

> [check]
* return warning (just like [RegexPattern.check])

> [_check_pattern_name]
* return warning (just like [RegexPattern.check])

> [resolve] match `path` against `self.pattern` (which return `new_path`, `args`, `kwargs`, update `kwargs` with [self.default_args]), then return [ResolverMatch(`self.callback`, `args`, `kwargs`, `self.pattern.name`, `route=str([self.pattern]))].
* resole `path` against `self.pattern`, when there is a match, call `self.callback` (this can be recursive, this is the basically the same of `path` in your "urls.py").


## URLResolver
> [\__init__] setup instance variables like [self.pattern], [self.urlconf_name], [self.callback], [self.default_kwargs], and etc.

> [check]
* check whether [self.url_patterns] and [self.resolve_error_handler] is valid.

> [\_check_custom_error_handlers]
* check [self.resolve_error_handler]'s signature. (All handlers takes (request, exception) arguments except `handler500` which takes (request)).

> [\_populate]
* short-circuit if called recursively in this thread to prevent infinite recursion. Concurrent threads may call this at the same time and will need to continue, to set 'populating' on a thread-local variable.



> [url_patterns] (cached property) try to iter [self.urlconf_module] otherwise [self.urlconf_module]
* check [self.urlconf_module] otherwise [self.urlconf_module] is iterable.