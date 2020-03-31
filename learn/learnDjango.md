> 系统地学习Django框架，主体基于官方文档
# 安装Django
- 如果要在生产站点上使用 Django，请将 Apache 与 mod_wsgi 一起使用。 mod_wsgi 能以两种模式运行：嵌入模式或守护进程模式。在嵌入模式下，mod_wsgi 类似于 mod_perl —— 它在 Apache 中嵌入 Python，并在服务器启动时将 Python 代码加载到内存中。代码在 Apache 进程的整个生命周期中都保留在内存中，与其他服务器相比，这可以显着提高性能。在守护进程模式下，mod_wsgi 会生成一个处理请求的独立守护进程。守护进程可以作为与 Web 服务器不同的用户运行，可能会提高安全性。可以在不重新启动整个 Apache Web 服务器的情况下重新启动守护进程，从而可以更加无缝地刷新代码库。
- Django 支持许多其他部署选项。一个是 uWSGI ；它和 nginx 配合使用很好。此外，Django 遵循 WSGI 规范（ PEP 3333 ），允许它在各种服务器平台上运行
# 模型和数据库
> 模型准确且唯一的描述了数据，它包含储存的数据的重要字段和行为。一般来说，每一个模型都映射一张数据库表
## 模型
## 执行查询
## 聚合
## 搜索
## 管理器
## 执行原生SQL
## 数据库事务
## 多数据库
### 定义数据库
- 即使没有默认数据库，也要保留该字段（这样，你必须为所有的模型，包括你所使用的任何 contrib 和第三方 app 设置 DATABASE_ROUTERS，所以不会有任何查询路由到默认数据库）
```
# 在setting.py中配置
import pymysql
pymysql.install_as_MySQLdb()
```
```
DATABASES = {
    'default': {},
    'users': {
        'NAME': 'user_data',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_user',
        'PASSWORD': 'superS3cret'
    },
    'customers': {
        'NAME': 'customer_data',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'mysql_cust',
        'PASSWORD': 'veryPriv@ate'
    }
}
```
### 同步数据库
- migrate 管理命令一次只在一个数据库上进行操作。默认情况下，它在 default 数据库上操作，但提供 --database 的话，它可以同步到不同数据库
```
$ ./manage.py migrate # 配置了默认数据库的情况下
$ ./manage.py migrate --database=users
```
- 大部分 django-admin 命令像 migrate 一样操作数据库——它们一次只操作一个数据库，使用 --database  来控制所要使用的数据库
- 这个规则的一个例外是 makemigrations 命令。它验证数据库中的迁移历史，以便在创建新迁移之前发现现有迁移文件的问题（这可能是修改它们所产生）。默认情况下，它只检查 default 数据库，但建议在任何模型安装时，执行routers的allow_migrate()方法
### 自动数据库路由
- 默认路由方案确保对象对原始数据库保持粘性（比如，从 foo 数据库检索到的对象将被保持到同一个数据库）。默认路由方案确保当数据库没有指定时，所有查询回退到 default 数据库
- 默认路由在每个Django项目上是开箱即用的。如果想实现更多有趣的数据库分配行为，可以定义和安装自己的数据库路由
- 数据库路由是一个类，它提供四种方法
    - db_for_read(model, **hints) 建议用于读取“模型”类型对象的数据库
    - db_for_write(model, **hints) 建议用于写入模型类型对象的数据库
    - allow_relation(obj1, obj2, **hints) 如果允许 obj1 和 obj2 之间的关系，返回 True 。如果阻止关系，返回 False
    - allow_migrate(db, app_label, model_name=None, **hints) 决定是否允许迁移操作在别名为 db 的数据库上运行。如果操作运行，那么返回 True ，如果没有运行则返回 False ，或路由没有意见则返回 None
- 数据库路由 DATABASE_ROUTERS 配置安装。这个配置定义类名列表，每个类名指定了主路由(django.db.router)应使用的路由
- Django 的数据库操作使用主路由来分配数据库使用。每当查询需要知道正在使用哪个数据库时，它会调用主路由，提供一个模型和提示（如果可用的话），然后 Django 会依次尝试每个路由直到找到数据库。如果没有找到，它试着访问提示实例的当前 _state.db。如果没有提供提示实例，或者实例没有当前数据库状态，主路由将分配默认数据库
### 手动选择路由
- 查询 `Author.objects.using('default').all()`
- 保存 `my_object.save(using='legacy_users')`
- 删除
```
>>> u = User.objects.using('legacy_users').get(username='fred')
>>> u.delete() # will delete from the `legacy_users` database
```
## 表空间
## 数据库连接优化
## 数据库工具
## 模型关联API
## 数据库逆向工程
- 在数据库中创建表
- 逆向工程 peek，并不产生新的文件 `model.py` ：`python manage.py inspectdb`
- 导入到应用中 `python manage.py inspectdb > sharer/models.py`
# 处理HTTP请求
# 使用表单
# 模板
# 基于类的视图
# 迁移
# 管理文件
# 测试
# 用户认证
# 缓存框架
# 条件视图处理
# 邮件
# 日志
# 分页
# 性能与优化
# 序列化
# 配置
# 信号
# 系统检查框架
# 拓展包
# 异步支持