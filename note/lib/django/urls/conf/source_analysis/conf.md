## include
> if `arg` is instance of tuple, get `urlconf_module` and `app_name` from arg, otherwise `urlconf_module` = `arg`; if `urlconf_module` is a module string, import it; get `patterns` and `app_name` from ``urlconf_module` and check whether they are valid; recursively get `pattern` from every element of `patterns` and check them. Finally, return `urlconf_module`, `app_name`, `namespace`.
* include `urlconf` (a list of urlconf) from urlconf string.

## _path
> if `view` is a list or tuple. return `URLResolver`; if `view` is callable, return `URLPattern`.
* return `URLResolver` or `URLPattern` based on `view`.

## path
* partial(_path, Pattern=RoutePattern)

## re_path
* partial(_path, Pattern=RegexPattern)
