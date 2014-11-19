Title: mysql relpace
Slug: mysql-replace
Date: 2014-09-16 16:50:05
Tags: mysql
Category: technology
Author: jyd
Lang: zh
Summary: 好用的replace

感觉像是在撑博文数量，这都发。。⊙﹏⊙b

场景：把一条数据插入到数据库中，但如果数据库中已经有重复的key，则会出错，这时候就不能insert，直接更新就行。

如果先select判断key是否存在，然后在选择update或者insert，就太麻烦了。
这时候直接用replace就行了。

replace可以认为是insert和update的合并版本，先进行insert，如果有重复的数据了，则再用update。

详细参考：<http://dev.mysql.com/doc/refman/5.0/en/replace.html>