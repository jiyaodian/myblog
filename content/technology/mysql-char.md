Title: mysql的字符
Slug: mysql-char
Date: 2014-09-25 09:24:45
Tags: mysql
Category: technology
Author: jyd
Lang: zh
Summary: mysql的字符，一个字母算一个字符，一个中文也算一个字符，原来一直以为都理解错了。

在mysql里面，我们把字段定义成char(10)或者varchar(10)的时候，我们定义的是10个字符。

在mysql里面，对于ASCII，每个字符占用1byte；对于UTF-8，每个字符占用3byte。

所以varchar(10)是可以保存10个中文的。

<http://stackoverflow.com/questions/10081500/mysql-char-varchar-character-sets-storage-sizes>

<http://dev.mysql.com/doc/refman/5.0/en/charset-unicode-utf8.html>