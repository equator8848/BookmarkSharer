# 安装|升级 Python
- https://zhuanlan.zhihu.com/p/34024112
- `wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz`
# 安装pip
```
1.  yum -y install epel-release

2.  yum -y install python-pip

3.  pip install -U pip
```
# 安装并测试 uwsgi
> Web Server Gateway Interface
- 全局安装而不是虚拟环境 `pip install uwsgi`
- 创建test.py
- 启动uswgi `uwsgi --http [ip]:8080 --wsgi-file test.py`  注意，ip填127.0.0.1会导致外部无法访问
- 映射Django项目 `uwsgi --chdir /data/BookmarkSharer/BookmarkSharer  --home /data/BookmarkSharer/venv/ --http :8080 --module BookmarkSharer.wsgi:application --enable-thads`
- 启动Django应用
```
uwsgi --chdir=/path/to/your/project \
    --module=mysite.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=mysite.settings \
    --master --pidfile=/tmp/project-master.pid \
    --socket=127.0.0.1:49152 \      # can also be a file
    --processes=5 \                 # number of worker processes
    --uid=1000 --gid=2000 \         # if root, uwsgi can drop privileges
    --harakiri=20 \                 # respawn processes taking more than 20 seconds
    --max-requests=5000 \           # respawn processes after serving 5000 requests
    --vacuum \                      # clear environment on exit
    --home=/path/to/virtual/env \   # optional path to a virtualenv
    --daemonize=/var/log/uwsgi/yourproject.log      # background the process
```
# 安装Nginx
 