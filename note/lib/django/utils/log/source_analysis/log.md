## request_logger
* ```logging.getLogger("django.request")```

## DEFAULT_LOGGING
* Default logging for Django. This sends an email to the site admins on every HTTP 500 error. Depending on DEBUG, all other log records are either send to the console (DEBUG=True) or discarded (DEBUG=False) by means of the require_debug_true filter.

## configure_logging
* using ```DEFAULT_LOGGING``` to config logging (logging.config.dictConfig) and call ```logging_config``` function with ```logging_settings```.

## AdminEmailHandler(logging.Handler)
* An exception log handler that emails log entries to site admins.

> [\__init__] setup [include_html], [email_backend], [reporter_class].

> [emit] setup ```subject```, ```message```, ```html_message``` from record, send them with [send_mail].

> [send_mail] call [mail.mail_admin] to send mail.

> [connection] call ```django.core.mail.get_connection``` to load an email backend and return an instance of it.

> [format_subject] escape CR and LF characters.

## CallbackFilter(logging.Filter)
* a logging filter that checks the return value of a given callable (which takes the record-to-be-logged as its only parameter) to decide whether to log a record.

> [\__init__] setup [callback]

> [filter] ```return callback(record)```

## RequireDebugFalse(logging.Filter)
* logging filter that checks ```settings.DEBUG``` is False

> [filter] ```return not settings.DEBUG```

## RequireDebugTrue(logging.Filter)
* logging filter that checks ```settings.DEBUG``` is True

> [filter] ```return settings.DEBUG```

## ServerFormatter(logging.Formatter)
* logging formatter that format record's message base on its status code

> [\__init__] setup [style]

> [format] format ```record.msg``` base on ```record_status_code``` and ```record.server_time```.

> [uses_server_time] ```return self._fmt.find('{server_time}') >= 0```

## log_response
* log errors based on HttpResponse status.
* log 5xx responses as errors and 4xx responses as warnings (unless a level is given as a keyword argument). The HttpResponse status_code requests are passed to the logger's extra parameter.
