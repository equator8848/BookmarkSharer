# 安装|升级 Python
- https://zhuanlan.zhihu.com/p/34024112
- `wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz`
# 安装pip
```
1.  yum -y install epel-release

2.  yum -y install python-pip

3.  pip install -U pip
```
# 安装uwsgi
> Web Server Gateway Interface
- 全局安装而不是虚拟环境 `pip install uwsgi`
- 创建xxx.py
- 启动uswgi `uwsgi --http [ip]:8080 --wsgi-file test.py`  注意，ip填127.0.0.1会导致外部无法访问