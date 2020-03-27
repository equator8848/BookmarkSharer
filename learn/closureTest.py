# coding:utf-8
# Created by Equator at 2020/3/25
# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# f1、f2、f3分别对应了fs这个list的三个元素
f1, f2, f3 = count()
print(f1())
print(isinstance(f2(), int))
