import datetime
import time

if __name__ == '__main__':
    # 时间戳
    print(time.time())
    # 时间元组
    print(time.localtime())
    print(time.localtime(time.time()))
    # 可读时间
    print(time.asctime(time.localtime(time.time())))
    # 时间元组格式化
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print(time)
