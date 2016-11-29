#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kai Blin'
SITENAME = u'PhDOps'
SITESUBTITLE = u'Tales from the underfunded cousin of DevOps, while trying to get research done.'
SITEURL = u'//phdops.kblin.org'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = u'pelican-bootstrap3'
BOOTSTRAP_THEME = u'simplex'

CC_LICENSE = u'CC-BY'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/kaiblin'),
          ('github', 'https://github.com/kblin'),)

TWITTER_USERNAME = u'kaiblin'
DISQUS_SITENAME = u'phdops'
USE_OPEN_GRAPH = True
TWITTER_CARDS = True
TWITTER_WIDGET_ID = u'591317301112270848'

DEFAULT_PAGINATION = 10
SHOW_DATE_MODIFIED = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
