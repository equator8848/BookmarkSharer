# 启动内嵌开发服务器
python BookmarkSharer/manage.py runserver

# 数据库逆向工程
python BookmarkSharer/manage.py inspectdb >BookmarkSharer/api/models/models.py
