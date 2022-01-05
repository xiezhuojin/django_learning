## SingleObjectMixin(django.views.generic.base.ContextMixin)
* provide the ability to retrieve a single object for further manipulation.
> [model] ```= None```
> [queryset] ```= None```
> [slug_field] ```= "slug"``` 
> [context_object_name] ```= None```
> [slug_url_kwarg] ``` = "slug"```
> [ok_url_kwarg] ``` = "pk"```
> [query_pk_and_slug] ``` = False```

> [get_object]
* return the object the view is displaying.

> [get_queryset]
* return the ```QuerySet``` that will be used to look up the object. this method is called by the default implementation of [get_object] and may be called if [get_object] is overridden.

> [get_slug_field]
* return the name of a slug field to be used to look up by slug

> [get_context_object_name]
* get the name to use for the object.

> [get_context_data]
* insert the single object into the context dict.

## BaseDetailView(SingleObjectMixin, django.views.generic_base.View)
* A base view for displaying a single object.
> [get] get ```context``` then return [render_to_response] with ```context```.

## SingleObjectTemplateResponseMixin(django.views.generic.base.TemplateResponseMixin)
> [template_name_field] ``` = None```
> [template_name_suffix] ``` = "_detail"```

> [get_template_name]
* return a list of template names to be used for the request. May not be called if ```render_to_response``` is overridden. Return the following list: 
    * the value of ```template_name``` on the view (if provided)
    * the contents of the ```template_name_field``` field on the object instance that the view is operating upon (if available)
    * ```<app_label>/<model_name><template_name_suffix>.html```

## DetailView(SingleObjectTemplateResponseMixin, BaseDetailView)
* render a "detail" view of an object. by default that is a model instance looked up from [queryset], but the view will support display of *any* object by overriding [get_object]
