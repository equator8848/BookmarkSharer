# coding:utf-8
# Created by Equator at 2020/3/25
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(isinstance(f2(), int))
