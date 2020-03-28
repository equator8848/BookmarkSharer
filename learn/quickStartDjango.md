> 快速入门Django，主体基于官方文档
# 安装Django
- pip安装 `python -m pip install Django`
- 检验
```
>>> import django
>>> print(django.get_version())
```

# 构建项目
- 创建一个新项目 `django-admin startproject mysite`
## 项目结构
```
mysite/
    manage.py # 一个让你用各种方式管理 Django 项目的命令行工具
    mysite/ # 包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名 (比如 mysite.urls)
        __init__.py
        settings.py # Django 项目的配置文件
        urls.py # Django 项目的 URL 声明，网站的“目录”
        asgi.py # 作为你的项目的运行在 ASGI 兼容的Web服务器上的入口
        wsgi.py # 作为你的项目的运行在 WSGI 兼容的Web服务器上的入口
```
## 快速启动项目
- 利用一个简易的服务器启动服务 `python manage.py runserver`
- 指定IP与端口，`python manage.py runserver ip:port`
- 用于开发的服务器在需要的情况下会对每一次的访问请求重新载入一遍 Python 代码。所以你不需要为了让修改的代码生效而频繁的重新启动服务器。然而，一些动作，比如添加新文件，将不会触发自动重新加载，这时你得自己手动重启服务器

# 创建应用
> 项目是应用的集合，应用也可以应用在多个项目之中
- 创建一个应用 `python manage.py startapp app_name`
## 应用的结构
```
app_name/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
# 编写视图
- 在`views.py`中定义函数，相当于Spring中的（巨大的）controller
## 配置URL映射
- 在项目中配置应用路由，使用`include('val')`函数包含导入应用的路由
- 在应用中配置视图路由
- 当包括其它 URL 模式时你应该总是使用 include() ， admin.site.urls 是唯一例外
## path()详解
- 函数 path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name
- route 一个匹配 URL 的准则（类似正则表达式）
- view 当找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入
- kwargs 任意个关键字参数可以作为一个字典传递给目标视图函数
- name 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式？

# 数据库配置
- 在` mysite/settings.py`中配置数据库信息
- 配置时区 将`TIME_ZONE = 'UTC'`修改为`TIME_ZONE = 'Asia/Shanghai'`
- 使用其它数据库，需要下载对应的 database bindings
- 在`DATABASES 'default'`中配置
    - ENGINE 指定数据库，`django.db.backends.sqlite3`、`django.db.backends.mysql`
    - NAME 数据库的名称。如果使用的是 SQLite，数据库将是你电脑上的一个文件，在这种情况下， NAME 应该是此文件的绝对路径，包括文件名。默认值 os.path.join(BASE_DIR, 'db.sqlite3') 将会把数据库文件储存在项目的根目录
## 创建模型
- 模型，也就是数据库结构设计和附加的其它元数据
- 在`polls/models.py`中创建模型，一个模型是单独的一个类
## 激活模型
- 在项目中添加应用：在` mysite/settings.py`中的INSTALLED_APPS子项添加点式路径`polls.apps.PollsConfig`
- 通过运行 makemigrations 命令，Django 会检测对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次迁移`python manage.py makemigrations polls`
- 查看预执行的SQL `python manage.py sqlmigrate polls 0001`
- 自动执行数据库迁移并同步管理数据库结构 `python manage.py migrate`
- 迁移是非常强大的功能，它能让你在开发过程中持续的改变数据库结构而不需要重新删除和创建表 - 它专注于使数据库平滑升级而不会丢失数据

# 后台管理
> 管理界面不是为了网站的访问者，而是为管理者准备的
- 创建管理员账号 `python manage.py createsuperuser`，输入用户名、邮箱、密码
- 管理自定义模型 在`polls/admin`中配置`admin.site.register(Question)`




































































