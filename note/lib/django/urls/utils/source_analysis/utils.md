## get_callable
* return a callable corresponding to `lookup_view`
    * if lookup_view is already a callable, return it
    * if lookup_view is a string import path that can be resolved to a callable, import that callable and return it, otherwise raise an exception.

## get_mod_func
* convert `django.views.news.stories.story_detail` to ['django.views.news.stories', 'story_detail'].
