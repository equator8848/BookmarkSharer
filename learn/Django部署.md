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
- 启动Django应用-命令方式
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
- 启动Django项目-配置文件方式
```
[uwsgi]
# socket 为上线使用，http为直接作为服务器使用。
socket = 127.0.0.1:8080 #ip和端口号可以改
http = 127.0.0.1:8080
chdir = /data/BookmarkSharer/BookmarkSharer
module = BookmarkSharer.wsgi:application
home = /data/BookmarkSharer/venv/
master = true
processes = 4
threads = 2
# 下面的参数不一定要加
# pidfile=uwsgi.pid   uwsgi.pid 和uwsgi.log会在启动uwsgi时自动生成在项目目录下。
# daemonize=uswgi.log
# max-requests=2000
# chmod-socket=664
# vacuum=true
```
```
# uwsgi启动
uwsgi --ini uwsgi.ini
#uwsgi 停止
uwsgi --stop uwsgi.pid
```
# 安装Nginx
 