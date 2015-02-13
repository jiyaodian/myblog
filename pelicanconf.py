#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'jyd'
SITENAME = u'我来我往的博客'
import os
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

DEFAULT_PAGINATION = 10

THEME = "themes/pelican-elegant"
SITESUBTITLE = 'Follow Your Heart'
CSS_FILE = 'screen.css'
METADATA = '记录、分享技术信息'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
RECENT_POST_COUNT = 1
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
