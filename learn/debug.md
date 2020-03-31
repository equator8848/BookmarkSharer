# Django 数据库连接错误
> ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3
## 解决方法一：降低Django版本
- Django连接MySQL时默认使用MySQLdb驱动，但MySQLdb不支持Python3，因此需要将MySQL驱动设置为pymysql
- 项目中的setting.py中配置
```
import pymysql
pymysql.install_as_MySQLdb()
```
## 解决方法二：升级mysqlclient？？？
```
pip install -U mysqlclient
```
# 关于import
## 导入模块
- `from . import module_abc`
## 导入类
- `from .ClassX import ClassX`