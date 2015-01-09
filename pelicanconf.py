#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jeremy Nelson'
SITENAME = 'Pikes Peak Aikido'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Aikido Schools of Ueshiba', 'http://asu.org/'),
         ('Boulder Aikikai', 'http://www.boulderaikikai.org/'),
         ('Castle Rock Aikido', 'http://www.craikido.com/'),
         ('Aikido for Veterans', '#'),
         ('Kashiwa Bujinkan Ninjutsu', 'http://www.kbninjutsu.com/'))

# Social widget
SOCIAL = (('Facebook', '#'),
          ('Twitter', '#'),)


DEFAULT_PAGINATION = 10

#THEME = 'ppa-ion-theme'
THEME = 'ppa-zerofour-theme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']