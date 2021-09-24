#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ardho Ainullah'
SITENAME = 'Archives Hiko'
SITEURL = ''


ARTICLE_URL = "{slug}/"
ARITCLE_SAVE_AS = "{slug}/index.html"
TAG_URL = "/tag/{slug}"
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

DEFAULT_PAGINATION = 7

DEFAULT_METDADATA = {'Status':'draft'}
FILENAME_METADATA = "(?P<title>)"
STATIC_PATHS = ['images','extra','extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/thumb.webp':{'path':'thumb.webp'},
    'extra/CNAME':{'path':'CNAME'},
    'extra/robots.txt':{'path':'robots.txt'},
}


DIRECT_TEMPLATES= ['about','index','blog','tag',"article",'404']
PAGINATED_TEMPLATES = {'blog':None}
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/{number}', '{base_name}/{number}{extension}/'),
)

SITEMAP = {
    "format": "xml",
    "priorities": {
        "indexes": 0.5,
    },
    "changefreqs": {
        "indexes": "daily",
    }
}
