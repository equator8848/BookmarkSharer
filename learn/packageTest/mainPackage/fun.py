import sys

print(sys.path)
# 正确
# from learn.packageTest.main.packageA import a

# 正确
#from packageA import a

# 错误
# from .packageA import a

# a.a()

# from packageA.a import a
# a()

# ValueError: attempted relative import beyond top-level package
# from ...packageTest.out import out

from learn.packageTest.out import out
# from learn.packageTest.out import out
out()


