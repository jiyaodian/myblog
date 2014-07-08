#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'我来我往'
SITENAME = u'我来我往'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ((u'旧博客', 'http://jyd.me/'),
         ('王宇的博客', 'http://blog.hellofe.com/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "themes/bootstrap3"
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DUOSHUO_SITENAME = "jydblog"
DUOSHUO_ID_PREFIX = "duoshuo_"
PYGMENTS_STYLE = "colorful"
HIDE_SIDEBAR = True
