Title: Django developer gadgets
Date: 2005-09-10

I've written two gadgets for helping me when
developing Django sites. Since they might be useful
to others, I thought I would mention them here.

### `ibofobi.utils.`<span class="shy"> </span>`developer_http`

The first is a web-server which re-exec's itself
after every request, so that all resources are
reloaded for every request. It has worked very well
for me. It lives as `ibofobi.utils.developer_http.py`
in `http://mel.ibofobi.dk/~sune/r/ibofobi.git`.

You can either execute it directly, with `--bind`
and `--port` (it defaults to all interfaces port
8080). Or if you just want to WSGI-server in there
you can import `BaseWSGIServer` from the module.

### `ibofobi.middleware.`<span class="shy"> </span>`template_dirs_hacker`

The second gadget is a middleware which munges `django.conf.settings.TEMPLATE_DIRS` for every request. This is how I use it in my `settings.devel`:

    from main import *
    import admin

    ROOT_URLCONF = 'settings.urls.devel'
    MIDDLEWARE_CLASSES = ('ibofobi.middleware.template_dirs_hacker.TemplateDirsHacker',) + MIDDLEWARE_CLASSES
    ADMIN_MEDIA_PREFIX = admin.ADMIN_MEDIA_PREFIX
    TEMPLATE_DIRS_MAPPING = (
        ('/admin/', admin.TEMPLATE_DIRS),
        ('/', TEMPLATE_DIRS),
    )
    TEMPLATE_DIRS = []

And in my `settings.urls.devel` I have:

    (r'^admin/', include('django.conf.urls.admin')),
    (r'', include('settings.urls.main')),

So, when I request `/admin/` I get the admin site
with the proper `TEMPLATE_DIRS`, and when I request
anything else I get the main site with the `TEMPLATE_DIRS`
for that.