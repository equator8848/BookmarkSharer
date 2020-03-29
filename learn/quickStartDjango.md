> 快速入门Django，主体基于官方文档
# 概述
- Django与标准的MVC框架不太一样，Django的MVC对应的是Model、Template、View
- 可以这么说， Django 是一个 "MTV " 框架，即 "模型(Model) "、 "模板(Template)" 和 "视图(View)
- 在 Django 中，控制器可能指的是框架本身，框架会根据 Django 的 URL 配置，将请求分发到适当的视图（view）
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

# 再议视图
- 每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 HttpResponse 对象，或者抛出一个异常，比如 Http404

# 模板
- 在应用根目录创建templates目录
- 应该在应用的templates目录创建以应用名称命名的目录来避免重名
- 引用的时候使用相对路径引用 `polls/xxx.html`
## 渲染模板并返回HttpResponse
### 传统做法
```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```
### 使用快捷函数 render()
> render()函数将请求对象作为它的第一个参数，模板名作为它的第二个参数，字典作为它的第三个可选参数。它返回使用给定上下文呈现的给定模板的HttpResponse对象
```
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```
## 抛出异常
- 抛出一个404异常
```
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```
- 使用快捷函数抛出404异常 get_object_or_404()
```
from django.shortcuts import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```
- get_list_or_404() 函数，工作原理和 get_object_or_404() 一样，除了 get() 函数被换成了 filter() 函数。如果列表为空的话会抛出 Http404 异常
## 避免URL硬编码
- 硬编码和强耦合的链接，对于一个包含很多应用的项目来说，修改起来是十分困难的
- 然而因为在polls.urls的url()函数中通过name参数为URL定义了名字，你可以使用`{% url %}`标签代替它
```
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
修改为
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
## 为URL添加命名空间
- 在一个真实的 Django 项目中，可能会有五个，十个，二十个，甚至更多应用。Django 如何分辨重名的 URL？
```
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
- 修改对应的模板
```
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
修改为
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

# 通用视图
> 这些视图反映基本的 Web 开发中的一个常见情况：根据 URL 中的参数从数据库中获取数据、载入模板文件然后返回渲染后的模板。 由于这种情况特别常见，Django 提供一种快捷方式，叫做“通用视图”系统
##  ListView
- 显示一个对象列表
- ListView 使用一个叫做 <app name>/<model name>_list.html 的默认模板；我们使用 template_name 来告诉 ListView 使用我们创建的已经存在的 "polls/index.html" 模板
## DetailView
- 显示一个特定类型对象的详细信息页面
- DetailView 期望从 URL 中捕获名为 "pk" 的主键值，所以我们为通用视图把参数改成pk
- 默认情况下，通用视图 DetailView 使用一个叫做 <app name>/<model name>_detail.html 的模板

# 自动化测试
- 自动化测试是由某个系统帮你自动完成的。当你创建好了一系列测试，每次修改应用代码后，就可以自动检查出修改后的代码是否还像你曾经预期的那样正常工作。你不需要花费大量时间来进行手动测试
## 代码测试
- 测试一个应用 `python manage.py test polls`
- Django如何寻找 polls 应用里的测试代码
    - 找django.test.TestCase的子类
    - 在类中寻找测试方法即以test开头的方法
## 视图测试
- Django 提供了一个供测试使用的 Client 来模拟用户和视图层代码的交互。我们能在 tests.py 甚至是 shell 中使用它
## 测试用例
- 当需要测试的时候，测试用例越多越好

# 静态资源
- django.contrib.staticfiles 存在的意义：它将各个应用的静态文件（和一些你指明的目录里的文件）统一收集起来，这样一来，在生产环境中，这些文件就会集中在一个便于分发的地方
- Django 将在应用的static目录下查找静态文件，同样以应用名创建目录以隔离资源重名问题
- images目录一般创建在`polls/static/polls`下
- `{% static %}` 等模板标签在静态文件（例如样式表）中是不可用的，因为它们不是由 Django 生成的。你仍需要使用**相对路径**的方式在你的静态文件之间互相引用

# 自定义管理页面
## 自定义后台表单
- 重排字段
```
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
```
- 将表单分为几个字段集
``` 
from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets 元组中的第一个元素是字段集的标题
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
```
## 添加关联对象
- 每个使用 ForeignKey 关联到另一个对象的对象可以在添加时添加其关联的对象
- 可以在创建被参照对象是一起创建参照对象
``` 
from django.contrib import admin

from .models import Choice, Question

# StackedInline改为TabularInline，可以使得关联对象以一种表格式的方式展示，显得更加紧凑
class ChoiceInline(admin.StackedInline):
    model = Choice # 定义关联模型
    extra = 3 # 定义插槽数目


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
```
## 自定义后台更改列表
- 默认情况下，Django 显示每个对象的 str() 返回的值。但有时如果我们能够显示单个字段，它会更有帮助。为此，使用 list_display 后台选项，它是一个包含要显示的字段名的元组，在更改列表页中以列的形式展示这个对象
```
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')
```
- 可以点击列标题来对这些行进行排序
- 过滤器，使用 list_filter
``` 
list_filter = ['pub_date']
```
- 搜索框 在列表的顶部增加一个搜索框。当输入待搜项时，Django 将搜索 question_text 字段。你可以使用任意多的字段——由于后台使用 LIKE 来查询数据，将待搜索的字段数限制为一个不会出问题大小，会便于数据库进行查询操作
```
search_fields = ['question_text']
```
## 自定义工程模板
- 在工程目录（指包含 manage.py 的那个文件夹）内创建一个名为 templates 的目录
- 在 TEMPLATES 设置中添加 DIRS 选项，DIRS 是一个包含多个系统目录的文件列表，用于在载入 Django 模板时使用，是一个待搜索路径
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

# 编写可重用程序
## 打包应用
- 打包工具 setuptools
















































