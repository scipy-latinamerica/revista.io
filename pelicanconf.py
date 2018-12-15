#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SciPyLA'
SITENAME = 'Revista Python Científico América Latina'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

STATIC_PATHS = ['img', 'pages' ]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [('Home', '/index.html'),             
             ('Conferencia', 'http://conf.scipyla.org/'),
             ('Contacto', '/pages/contacto.html')]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'html5-dopetrope/'

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['liquid_tags.notebook', 'tipue_search']

# Search
#GOOGLE_SEARCH = True
TIPUE_SEARCH = True

#TEMPLATE_PAGES = {
#        'search.html': 'search.html',
#        }

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

# Theme variables
ABOUT_TEXT = "Revista de Python orientado a las ciencias mantenida por la comunidad de SciPyLA"
ABOUT_IMAGE = 'img/scipyla.nav.svg'
ABOUT_IMAGE_LOGO = 'img/scipyla-logo.svg'
FACEBOOK_USER = 'scipyla'
TWITTER_USER = 'ScipyLA'
LINKEDIN_USER = '8344796'
YOUTUBE_USER = 'UClb88lwUvlFikmhTzVGsVGA'
GOOGLEPLUS_USER = '116952396338000992599'
TELEGRAM_USER = 'scipyla'
COPYRIGHT = 'SciPyLA'
ABOUT_LINK = 'http://scipyla.org/'