## FormMixin(django.views.generic.base.ContextMixin)
* provide a way to show and handle a form in a request.
> [initial] ``` = {}```
> [form_class] ``` = None```
> [success_url] ``` = None```
> [prefix] ``` = None```

> [get_initial]
* return the initial data to use for forms on this view.

> [get_prefix]
* return the prefix to use for forms.

> [get_form_class]
* return the form class to use.

> [get_form]
* return an instance of the form to be used in this view.

> [get_form_kwargs] keyword arguments are ```{"initial": self.get_initial(), "prefix": self.get_prefix(), "data": self.request.POST, "files": self.request.FILES}```
* return the keyword arguments for instantiating the form.

> [get_success_url]
* return the URL to redirect to after processing a valid form.

> [form_valid]
* if the form is valid, redirect to the success url.

> [form_invalid]
* if the form is invalid, render the invalid form.

> [get_context_data]
* insert the form ([get_form]) into the context dict.

## ModelFormMixin(FormMixin, SingleObjectMixin)
* provide a way to show and handle a ```ModelForm``` in a request.

> [fields] ``` = None```
* field to show, save

> [get_form_class] return ```model_form.modelform_factory(model, fields=self.fields)```
* return the form class to use in this view.

> [get_form_kwargs]
* return the keyword arguments for instantiating the form.

> [get_success_url]
* return the URL to redirect to after processing a valid form.

> [form_valid]
* if the form is valid. save the associated model.

## ProcessFormView(django.views.generic.base.View)
* render a form on GET and processes it on POST.

> [get]
* handle GET requests: instantiate a blank version of the form.

> [post]
* handle POST requests: instantiate a form instance with the passed POST variables and then check if it's valid.

> [put]
* PUT is a valid HTTP verb for creating (with a known URL) or editing object, note that browsers only support POST for now.

## BaseFormView(FormMixin, ProcessFormView)
* a base view for displaying a form.

## FormView(django.views.generic.base.TemplateResponseMixin, BaseFormView)
* a view for displaying a form and rendering a template response.

## BaseCreateView(ModelFormMixin, ProcessFormView)
* base view for creating a new object instance.
* Using this base class requires subclassing to provide a response mixin.

> [get] basically just ```return super().get(request, *args, **kwargs)```

> [post] basically just ```return super().post(request, *args, **kwargs)```

## CreateView(SingleObjectTemplateResponseMixin, BaseCreateView)
* view for creating a new object, with a response rendered by a template.

## BaseUpdate(ModelFormMixin, ProcessFormView)
* just like ```BaseCreateView```, but difference name.

## UpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView)
* view for updating an object, with a response rendered by a template.
> [template_name_suffix] ``` = "_form"```

## DeletionMixin
* provide the ability to delete objects.
> [success_url] ``` = None```

> [delete]
* call the [delete] method on the fetched object and then redirect to the success URL.

> [post]
* same as [delete].

> [get_success_url] ```return self.success_url.format(**self.object.__dict__)```

## BaseDeleteView(DeletionMixin, BaseDetailView)
* base view for deleting an object.
* using this base class requires subclassing to provide a response mixin.

## DeleteView(SingleObjectTemplateResponseMixin, BaseDeleteView)
* view for deleting an object retrieved with self.get_object(), with a response rendered by a template.
> [template_name_suffix] ``` = "_confirm_delete"```
