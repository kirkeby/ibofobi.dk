#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

AUTHOR = u'Sune Kirkeby'
SITENAME = u'ibofobi.dk'
SITEURL = 'http://ibofobi.dk'
TIMEZONE = 'Europe/Copenhagen'
DEFAULT_LANG = u'en'

TYPOGRIFY = True

THEME = '.'
THEME_STATIC_PATHS = []

FILES_TO_COPY = [
    ('pages/stuff/curriculum-vitae/cv.pdf', 'stuff/curriculum-vitae/cv.pdf'),
]

STATIC_PATHS = ['css', 'js', 'images', 'files']
STATIC_SAVE_AS = 'static/{path}'

ARTICLE_URL = 'blog/archive/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = AUTHOR_URL + 'index.html'

CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

DIRECT_TEMPLATES = ['blog/index']
PAGINATED_DIRECT_TEMPLATES = ['blog/index']

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
