#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

AUTHOR = u'Sune Kirkeby'
SITENAME = u'ibofobi.dk'
SITEURL = 'http://ibofobi.dk'
TIMEZONE = 'Europe/Copenhagen'
DEFAULT_LANG = u'en'

THEME = '.'
THEME_STATIC_PATHS = []

STATIC_PATHS = ['css', 'js', 'images']
STATIC_SAVE_AS = 'static/{path}'

ARTICLE_URL = 'blog/archive/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

DIRECT_TEMPLATES = ['tags', 'categories', 'archives']

# Pelican only understands md/rst 'pages', so we have to tell it to that html
# means it's a template-page.
TEMPLATE_PAGES = {}
for path, dirnames, filenames in os.walk('content/pages'):
    for filename in filenames:
        if filename.endswith('.html'):
            path = os.path.join(path, filename)
            content_path = path.split('/', 1)[1]
            output_path = content_path.split('/', 1)[1]
            TEMPLATE_PAGES[content_path] = output_path
