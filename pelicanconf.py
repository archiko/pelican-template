#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ardho Ainullah'
SITENAME = 'Archiko - Python, Math And Data Scients.'
SITEURL = ''


ARTICLE_URL = "{slug}"
ARITCLE_SAVE_AS = "{slug}"
TAG_URL = "tag/{slug}"
#TAG_SAVE_AS = "tag/{slug}"

THEME = 'themes'
PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%d, %b %Y"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

#ACTIVE WHEN POSTS > 10
#DEFAULT_PAGINATION = 5

FILENAME_METADATA = "(?P<title>)"
STATIC_PATHS = ['images','extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}


DIRECT_TEMPLATES= ['about','index','blog','tag',"article",'404']
PAGINATED_TEMPLATES = {'blog':None}
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}', '{base_name}/{number}{extension}/'),
)

