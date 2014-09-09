Title: ipython 自动加载代码
Slug: ipython-auto-reload-code
Date: 2014-09-09 17:44:02
Tags: ipython, tools
Category: tools
Author: jyd
Lang: zh
Summary: ipython自动加载最新代码，方便测试。

```
In [1]: %load_ext autoreload

In [2]: %autoreload 2

In [3]: from foo import some_function

In [4]: some_function()
Out[4]: 42

In [5]: # open foo.py in an editor and change some_function to return 43

In [6]: some_function()
Out[6]: 43
```

<http://ipython.org/ipython-doc/2/config/extensions/autoreload.html>