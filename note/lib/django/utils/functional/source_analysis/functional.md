## cached_property
* decorator that converts a method with a single self argument into a property cached ont the instance.

> [name] ``` = None```
* will be deprecated in Django 4.0

> [func] (staticmethod)
* return raise ```TypeError```

> [\__init__]
* setup [func] and [\__doc__] which get from given function.

> [\__set_name__]
* set the function name, not that important.

> [\__get__]
* call the function and put the return value in instance.__dict__ so subsequent attribute access on the instance returns the cached value instead of calling cached_property.__get__().

## classproperty
* decorator that converts a method with a single cls argument into a property that can be accessed directly from the class.

> [\__init__]
* setup [fget] which is the method passed.

> [\__get__]
* just return the result of [fget]

> [getter]
* first setup [fget], then return self. Not that important.

## Promise
* base class for the proxy class created in the closure of the lazy function. It's used to recognize promises in code.

## lazy
* turn any callable into a lazy evaluated callable, result classes or type is required -- at least one is needed so that the automatic forcing of the lazy evaluation code is triggered. Results are not memoized; the function is evaluated on every access.

### __proxy__(Promise) (functools.total_ordering)
* encapsulate a function call and act as a proxy for methods that are called on the result of that function. The function is not evaluated util on the the methods on the result is called.

    > [\__prepared] ``` = False```
    > [\__init__] if [\__prepare], call [\__prepare_class__], then then [\__prepared] to true.
    * collects [\__args] and [__kw] for calling the function.

    > [\__reduce__]
    * return the lazy result of function, and [\__args], [\__kw], [resultclasses]

    > [\__repr__]
    * representation of proxy

    > [\__prepare_class] (classmethod)
    * turn every method of given class into a lazy evaluated method.

    > [\__promise__] (classmethod)
    * build a wrapper around some magic method

    > [\__text_cast] ```return func(*self.__args, **self.__kw)```

    > [\__bytes_cast] ```return bytes(func(*self.__args, **self,__kw))```

    > [\__bytes_cast_encoded] ```return func(*self.__args, **self.__kw).encode()```

    > [\__cast] return [\__bytes_cast], [\__text_cast], or func(*self.__args, **self.__kw) base on function's resultclasses.

    > [\__str__] ``` return str(self.__cast())```

    > [\__eq__] ```other = other.__cast()``` if ```other``` is instance of ```Promise```, then compare them.

    > [\__lt__]
    * just like [\__eq__]

    > [\__hash__] return the hash of ```self.__cast()```

    > [\__mod__]
    * just like [\__eq__]

    > [\__add__]
    * just like [\__eq__]

    > [\__radd__]
    * just like [\__add__], but in right order

    > [\__deepcopy__]
    * return the deepcopy of ```self```

    [\__wrapper__] (@wraps(func))
    * creates the proxy object, instead of the actual value

## _lazy_proxy_unpickle ```return lazy(func, *resultclasses)(*args, **kwargs)```

## lazystr ```return lazy(str, str)(text)```
* shortcut for the common case of a lazy callable that returns str.

## keep_lazy
* a decorator that allows a function to be called with one or more lazy arguments. If some of the args are lazy, the function is evaluated immediately, otherwise a __proxy__ is returned that will evaluate the function when needed.

## keep_lazy_text
* a decorator for functions that accept lazy arguments and return text.

## empty ``` = object()```

## new_method_proxy
* helper function to wrapping method of```LazyObject```

## LazyObject
* a wrapper for another class that can be used to delay instantiate wrapped class.
* by subclassing, you have the opportunity to intercept and instantiation, if you don't need to do that, use ```SimpleLazyObject```

> [_wrapped] ``` = None```
* avoid infinite recursion when tracing __init__

> [\__init__] set [\_wrapped] to ```None```

> [\__setattr__] basically set attribute for [\_wrapped]

> [\__delattr__]
* reverse of [\__setattr__]

> [\_setup]
* must be implemented by subclasses to initialize the wrapped object.

> [\__reduce__]
* basically the same as ```__proxy__```, but function on [_wrapped]

> [\__copy__]
* basically the same as ```__proxy__```, but function on [_wrapped]

> [\__deepcopy__]
* basically the same as ```__proxy__```, but function on [_wrapped]

> [\__bytes__] ``` = new_method_proxy(bytes)```
> [\__str__] ``` = new_method_proxy(str)```
> [\__bool__] ``` = new_method_proxy(bool)```

> [\__dir__] ``` = new_method_proxy(dir)```

> [\__class__] ``` = property(new_method_proxy(operator,attrgetter("__class__")))```
> [\__eq__] ``` = new_method_proxy(operator.eq)```
> [\__lt__] ``` = new_method_proxy(operator.lt)```
> [\__gt__] ``` = new_method_proxy(operator.gt)```
> [\__ne__] ``` = new_method_proxy(operator.ne)```
> [\__hash__] ``` = new_method_proxy(hash)```

> [\__getitem__] ``` = new_method_proxy(operator.getitem)```
> [\__setitem__] ``` = new_method_proxy(operator.setitem)```
> [\__delitem__] ``` = new_method_proxy(operator.delitem)```
> [\__iter__] ``` = new_method_proxy(iter)```
> [\__len__] ``` = new_method_proxy(len)```
> [\__contains__] ``` = new_method_proxy(operator.contains)```

## unpickle_lazyobject
* used to unpickle lazy objects. just return its argument, which will be the wrapped object.

## SimpleLazyObject(LazyObject)
* a lazy object initialized from any function. designed for compound objects of unknown type. For builtin know type, use ```django.utils.functional.lazy```

## partition
* split the values into two sets, based on the return value of the function (True/False)
