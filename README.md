### 发布命令

ghp-improt output
git push https://github.com/jiyaodian/jiyaodian.github.io.git gh-pages:master


或者
git remote add site https://github.com/jiyaodian/jiyaodian.github.io.git
git push site gh-pages:master


或者
git checkout gh-pages
然后add想要的
then git push site gh-pages


### 环境
```shell
pip install pelican
pip install markdown
```

当commit到git的时候，自动提交到github上

添加git的hook。

添加以下内容到文件 .git/hooks/post-commit
```shell
pelican content -o output -s pelicanconf.py && ghp-import output && git push origin gh-pages
git push origin master
```
