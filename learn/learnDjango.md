# 起步
## 安装
- pip安装 `python -m pip install Django`
- 检验
```
>>> import django
>>> print(django.get_version())
```
## 构建项目
- 创建一个新项目 `django-admin startproject mysite`
### 项目结构
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
## 创建应用
> A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects
- 创建一个应用 `python manage.py startapp app_name`
### 应用的结构
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
## 编写视图
- 在`views.py`中定义函数，相当于Spring中的（巨大的）controller
## 配置URL映射
- 在项目中配置应用路由，使用`include('val')`函数包含导入应用的路由
- 在应用中配置视图路由
- 当包括其它 URL 模式时你应该总是使用 include() ， admin.site.urls 是唯一例外
### path()详解
- 函数 path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name
- route 一个匹配 URL 的准则（类似正则表达式）
- view 当找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入
- kwargs 任意个关键字参数可以作为一个字典传递给目标视图函数
- name 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式？