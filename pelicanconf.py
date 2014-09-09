#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'我来我往'
SITENAME = u'我来我往'
SITEURL = ''
#SITEURL = 'http://blog.jyd.me'

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

DEFAULT_PAGINATION = 10

THEME = "themes/bootstrap3"
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DUOSHUO_SITENAME = "jydblog"
DUOSHUO_ID_PREFIX = "duoshuo_"
PYGMENTS_STYLE = "colorful"
HIDE_SIDEBAR = True

#主题设置
SHOW_ARTICLE_CATEGORY = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
#BOOTSTRAP_NAVBAR_INVERSE = True

#网站配置
FEED_DOMAIN = SITEURL
AUTHORS_SAVE_AS = ''
DATE_FORMATS = {
    'zh': "%Y-%m-%d",
}
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/favicon.ico': {'path': 'favicon.ico'}
        }

BAIDU_TONGJI = True
