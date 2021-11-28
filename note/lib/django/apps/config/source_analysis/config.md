### AppConfig
* class representing a Django application and its configuration.
> [\__init__] setup [self.name] (full python path to the application e.g. 'django.contrib.admin'), [self.module] (root module for the application e.g. <module 'django.contrib.admin' from 'django/contrib/admin/\__init__.py'>), [self.apps] (reference to the Apps registry that holds this AppConfig. Set by the registry when it registers the AppConfig instance). [self.models_module] (module containing models e.g. <module 'django.contrib.admin.models' from 'django/contrib/admin/models.py'>. Set by [import_models()]). [self.models] (mapping of lowercase model names to model classes.).

> [default_auto_field] (cached property) just returns [settings.DEFAULT_AUTO_FIELD].

> [_is_default_auto_field_overridden]

> [_path_from_module]
* attempt to determine app's filesystem path from its module.

> [create] (class method) this eventually returns app_config_class(app_name, app_module). 
* factory that creates an app config from an entry in INSTALLED_APPS.

> [get_model]
* return the model with the given case-insensitive `model_name`

> [get_models]
* return an iterable of models. 
* By default, the following models aren't included: 
    * auto-created models for many-to-many-relations without an explicit intermediate table. 
    * models that have been swapped out.

> [import_models]

> [ready] override this method in subclasses to run code when django starts.
