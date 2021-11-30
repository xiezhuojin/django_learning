## Command(BaseCommand)
* starts a lightweight web server for development.
> [server_cls] (class variable) set to [django.core.servers.basehttp.WSGIServer]

> [add_argument]
* add addtional argument, e.g. `addrport`, `--ipv6`, `--nothreading`, `--noreload`

> [execute] basically just call [super().execute]

> [get_handler] return the default WSGI handler [django.core.servers.basehttp.get_internal_wsgi_application] for the runner.

> [handler] basically just call [self.run]

> [run] basically just call [self.inner_run]

> [inner_run] print some lint, then just call [django.core.servers.basehttp.run].
