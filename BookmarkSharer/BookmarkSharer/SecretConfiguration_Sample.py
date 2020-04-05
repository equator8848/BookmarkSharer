from enum import Enum, unique


@unique
class SecretConfiguration(Enum):
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = '3306'
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = '123456'
    REDIS_LOCATION = 'redis://127.0.0.1:6379'
    REDIS_PASSWORD = '123456'
    GITHUB_CLIENT_ID = 'fdafasdf5453gfgs'
    GITHUB_CLIENT_SECRET = 'fdsafaerer4523534v5cf342ccxcrrrrrrrrrrr23'
    GITHUB_CALLBACK_URL = 'http://localhost:8000/bookmarkSharer/api/user/github_login_callback'
