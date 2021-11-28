## Apps
* a registry that stores the configuration of installed applications. It also keeps track of models. 

> [\__init__] setup [self.all_models] (mapping of app labels => model names => model classes), [self.app_configs] (mapping of labels to AppConfig instances for installed apps), [self.stored_app_configs] (stack of app_configs), [self.apps_ready] (whether the registry is populated). [self._pending_operations] (Maps ("app_label", "modelname") tuples to lists of functions to be called when the corresponding model si ready.), then call [self.populate(installed_apps)] to populate apps.

> [populate]
* load application configurations and models. Import each application module and the each model module. 

> [check_apps_ready]
* raise an exception if all apps haven't been imported yet.

> [check_models_ready]
* raise an exception if all models haven't been import yet.

> [get_app_configs]
* raise an exception if all models haven't been imported yet.

> [get_app_configs] call [self.check_apps_ready] then return [self.app_configs.values()]
* import applications and return an iterable of app configs.

> [get_app_config] 
* import applications an returns an app config for the given label. 

> [get_models] (lru_cached) 
* return a list of all installed models. 
* By default, the following models aren't included:
    * auto-created models for many-to-many relations without an explicit intermediate table.
    * models that have been swapped out.

> [get_model]
* return the model matching the given `app_label` and `model_name`.

> [register_model] called by get_app_config()

> [is_installed]
* check whether an application with this name exists in the registry.

> [get_containing_app_config] look for an app config containing a given object. 

> [get_registered_model] 
* similar to get_model(), but doesn't require that an app exists with the given app_label.

> [get_swappable_settings_name] (lru cached)
* For a given model string (e.g. "auth.User"). return the name of the corresponding settings name if it refers to a swappable model. If the referred model is not swappable, return None.

> [set_available_apps] 
* push a new app_config to [self.app_configs]

> [unset_available_apps]
* cancel a previous call to [set_available_apps]

> [set_installed_apps] 
* enable a different set of installed apps for [self.get_app_configs].

> [unset_installed_apps]
* cancel a previous call to set_installed_apps

> [clear_cache]
* clear all internal caches.

> [lazy_model_operation]
* take a function and a number of ("app_label", "modelname") tuples, and when all the corresponding models have been imported and registered, call the function with the model classes as its arguments.

> [do_pending_operations]
* take a newly-prepared model and pass it to each function waiting for it. This is called at the very end of Apps.register_model().
