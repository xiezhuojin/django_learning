## utc
* UTC time zone as a tzinfo instance (pytz.utc)

## get_fixed_timezone
* return a tzinfo instance with a fixed offset from UTC

## get_default_timezone (lru_cached)
* return the default time zone as a tzinfo instance. this is the time zone defined by settings.TIME_ZONE

## _active
* ```_active = Local()```

## get_default_timezone_name
* ```return _get_timezone_name(get_current_timezone)``` to return the name of the currently active time zone.

## _get_timezone_name
* return the offset for fixed offset timezones, or the name of timezone if not set.

## activate
* set the time zone for the current thread.

## deactivate
* unset the time zone for the current thread.

## override(ContextDecorator)
* temporarily set the time zone for the current thread.
* this is a context manager that uses django.utils.timezone.activate() to set the timezone on entry and restores the previously active timezone on exit.

> [\__init__] setup [timezone]

> [\__enter__] save ```_active.value``` the old timezone, call ```deactivate``` to clear ```_active.value```, then ```activate(self.timezone)``` to setup ```_active.value```

> [\__exit__] opposite of [\__enter__]

## template_localtime
* check if the value is a datetime and converts it to local time if necessary.
* this function is designed for use by the template engine.

## localtime
* convert an aware datetime.datetime to local time.

## now
* return an aware or naive datetime.datetime, depending on settings.USE_TZ.

## is_aware
* determine if a given datetime.datetime is aware.

## is_naive
* determine if a given datetime.datetime is naive

## make_aware
* make a naive datetime.datetime in a given time zone aware.

## make_naive
* make an aware datetime.datetime naive in a given time zone.

## _is_pytz_zone
* checks if a zone is a pytz zone

## _datetime_ambiguous_or_imaginary
