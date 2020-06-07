#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ushk'
SITENAME = 'Dan Stoddart'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']
FORMATTED_FIELDS = ['summary', 'title']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll

LINKS = (('ArielAI', 'https://www.arielai.com/'),
         ('UCL Foundational AI Centre', 'https://aiucl.github.io/'),
         )
# Social widget
SOCIAL = (('Github', 'https://github.com/Ushk'),
          ('Linkedin', 'https://www.linkedin.com/in/dan-stoddart-079b8611a/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
