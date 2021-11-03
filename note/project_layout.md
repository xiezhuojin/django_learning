django_site/                # Django project container
    manage.py               # (read) command live utility that lets you interact with this Django project
    django_site/            # the actual python package for your project. Its name is the python package name you'll need to use to import anything inside it(e.g. django_site.urls)
        __init__.py
        settings.py         # settings/configuration for this Django project.
        urls.py             # The URL declarations for this Django project
        asig.py             # An entry-point for ASGI-compatible web servers to serve your project.
        wsgi.py             # An entry-point for WSGI-compatible web servers to serve your project.