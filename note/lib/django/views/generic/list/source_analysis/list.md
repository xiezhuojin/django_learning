## MultipleObjectMixin(django.views.generic.base.ContextMixin)
* a mixin for views manipulating multiple objects.
> [allow_empty] ``` = True```
> [queryset] ``` = None```
> [model] ``` = None```
> [paginate_by] ``` = None```
> [paginate_orphans] ``` = 0```
> [context_object_name] ``` = Paginator```
> [paginator_class] ``` = Paginator```
> [page_kwarg] ``` = "page"```
> [ordering] ``` = None```

> [get_queryset]
* return the list of items for this view.
* The return value must be an iterable and may be an instance of ```QuerySet``` in which case ```QuerySet``` specific behavior will be enabled.

> [get_ordering] just return [ordering]
* return the field or fields to use for ordering the queryset.

> [paginate_queryset]
* paginate the queryset, if needed.

> [get_paginate_by]
* get the number of items to paginate by, or ```None``` for no pagination.

> [get_paginator]
* return an instance of the paginator for this view.

> [get_paginate_orphans]
* return the maximum number of orphans extend the last page by when paginating.

> [get_allow_empty]
* return ```True``` if the view should display empty lists and ```False``` if a 404 should be raised instead.

> [get_context_object_name]
* get the name of the item to be used in the context.

> [get_context_data]
* get the context for this view.

## BaseListView(MultipleObjectMixin, django.views.generic.base.View)
* a base view for displaying a list of object.

## MultipleObjectTemplateResponseMixin(django.views.generic.base.TemplateResponseMixin)
* mixin for responding a template and a list of objects.
> [template_name_suffix] ``` = "_list"```

> [get_template_name]
* return a list of template names to be used of the request. Must return a list. May not be called if [render_to_response] is overridden.

## ListView(MultipleObjectTemplateResponseMixin, BaseListView)
* render some list of objects, set by [model] or [queryset]. [queryset] can actually be any iterable of items, not just a queryset.
