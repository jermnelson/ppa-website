#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jeremy Nelson'
SITENAME = 'Pikes Peak Aikido'
DEBUG = False
BASE = {'theme': 'ppa-theme',
        'gdocid': '0B-8QrT1VCyEkfmR4c2tEcWhvVHl0RlNFSzVJUzhIeFFUd2dDOTBKbTR4VlBmU2V4WWZHRWc'}
ION = {'theme': 'ppa-ion-theme',
       'gdocid': '0B-8QrT1VCyEkfmQyTHZJMlMtcnRKM1o1a0FscHFEVU1yVXNsMTIxRU1XZXIxU1ZqSjhuSms'}
ZEROFOUR = {'theme': 'ppa-zerofour-theme',
            'gdocid': '0B-8QrT1VCyEkfjM4N1hFemV0OURfajlWR1ZTZURVV21VUTFSV1pKM3RTWHVoZkRyYXZtams'}
ACTIVE = ZEROFOUR
if DEBUG:
    SITEURL = ''
else:
    SITEURL = 'https://www.googledrive.com/host/{}'.format(ACTIVE.get('gdocid'))

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

SHOW_ARTICLE_AUTHOR = True

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
         ('Eishen Ryu Kenjutsu', 'http://'),
         ('Kashiwa Bujinkan Ninjutsu', 'http://www.kbninjutsu.com/'))

# Social widget
SOCIAL = (('Facebook', '#'),
          ('Twitter', '#'),)


DEFAULT_PAGINATION = 10

THEME = ACTIVE.get('theme')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']
