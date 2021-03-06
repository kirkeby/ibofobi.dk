#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'https://ibofobi.dk'

DELETE_OUTPUT_DIRECTORY = True

# The 404-page does not work with relative URLs, since it does not have any
# one home, so use absolute URLs in production.
RELATIVE_URLS = False

DISQUS_SITENAME = "ibofobi"
GOOGLE_ANALYTICS = "UA-169526-1"
