## resolve
* get `urlconf` then use it to resolve `path`.

## reverse
* get url of given view, view can be viewname or a view function,

## reverse_lazy
* `lazy(reverse, str)

## clear_url_caches
* clear url caches by calling `get_callable.cache_clear()`, `_get_cached_resolver.cache_clear()`, `get_ns_resolver.cache_clear()`.

## set_script_prefix
* set the script prefix for the current thread.

## get_script_prefix
* return the currently active script prefix. 

## clear_script_prefex
* unset the script prefix for the current thread.

## set_urlconf (USEFUL)
* set the URLconf for the current thread (overriding the default one in settings.) If `urlconf_name` is None, revert back to the default.

## is_valid_path
* return the `ResolverMatch` if the given path resolves against the default URL resolver, False otherwise. 

## translate_url
* given a URL (absolute or relative), try to get its translated version in the `lang_code` language.
