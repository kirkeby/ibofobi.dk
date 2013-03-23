#!/usr/bin/env python
# -*- coding: utf-8 -*- #

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

TEMPLATE_PAGES = {
    'pages/index.html': 'index.html',
    'pages/about/index.html': 'about/index.html',
}
