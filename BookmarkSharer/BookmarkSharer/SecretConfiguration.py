from enum import Enum, unique


@unique
class SecretConfiguration(Enum):
    MYSQL_HOST = "132.232.2.232"
    MYSQL_PORT = '3306'
    MYSQL_USERNAME = 'ROOT'
    MYSQL_PASSWORD = 'LBJ.19980707'
    REDIS_LOCATION = 'redis://132.232.2.232:6379'
    REDIS_PASSWORD = 'equator8848'
