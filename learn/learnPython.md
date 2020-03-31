# Python基础语法
> 主体是《廖雪峰Python教程》的笔记，后续会自己补充内容
---
# Python基础
## Python标准文件模板
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
```
## 基础的输入输出
- 输出 `print()`，该函数可以接受多个字符串，字符串之间使用逗号隔开，输出时遇到逗号将会输出空格
- 输入 `input()`，该函数接受用户输入一个字符串并通过返回值返回，该函数的参数字符串即提示用户输入的提示语
## 数据类型
### 整数
- Python可以处理任意大小的整数
### 浮点数
- 使用数学写法或者科学计数法
- Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
### 字符串
- 使用单引号或者双引号括起来的任意文本
- 使用 `\`转义字符转义，`\r`表示字符串默认不转义
### 布尔值
- `True`或者`False`两种值
- 布尔运算 and or not
### 空值
- `None`，它不等于0，它是有意义的
### 变量
- Python是动态类型的语言，变量名仅仅是一个代号
### 常量
- Python中没有真正的常量，不像Java有final关键字，一般常量全大写
### 除法`/`与`//`（地板除）
- 一般的除法，其结果为浮点数，即使是两个整数相除
- 地板除的结果是整数，其对结果取整
- `%`为取余运算
## 字符编码
### Unicode编码
- Unicode编码一般用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode编码
### UTF-8编码
- UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节
- 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
- 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器
### 编码与解码
- 使用`encode()`方法将Unicode编码的字符串编码为指定编码方式的bytes
- 使用`decode()`方法按指定的编码方式将bytes解码为Unicode编码的字符串
- 在python源文件首部，加上`# -*- coding: utf-8 -*-`注释，提示编译器按照UTF-8编码读取
### 格式化输出
- 使用`%` 进行格式化输出
- 使用字符串的`format()`函数，该函数的参数依次将`{0}`、`{1}`替换
## 使用list与tuple
### list
- 一种有序的集合，列表、动态数组，从前往后索引下标从0开始，从后往前从-1开始
- append追加、insert指定索引插入、pop删除末尾的元素、pop(i)删除
- 定义一个空的列表 []
### tuple
- 元组，一种不能改变的列表
- 定义一个空的元组 ()，定义一个只有一个元素的元组，加上逗号避免歧义 (xxx,)
- tuple所谓的“不变”是说，tuple的每个元素，指向永远不变，但指向的这个东西本身是可变的
## 条件判断
- 只要一个变量是非零数值、非空字符串、非空list等，就判断为True，否则为False
```
if statement:
    do something
elif statement:
    do something
else:
    do something
```
## 循环
### for...in 循环
- 依次迭代list或tuple中的每个元素
- Python提供一个range()函数，可以生成一个整数序列（从0开始）
### while循环
### break与continue
## 使用dict以及set
### dict
- 字面量定义 `d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}`
- 添加 `d[key]=value`
- 删除 `d.pop(key)`
- 查找 `d[key]`，如果值不存在则会抛出异常；`d.get(key)`，返回默认值None
- dict的key必须是不可变对象
### set
- set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
- 字面量定义 `s = set([1, 2, 3])`
- 添加 `s.add(key)`
- 删除 `s.remove(key)`
### 不可变对象
- Immutability模式
---
# 函数
## 调用函数
- 在交互式命令行通过help(func_name)查看func_name函数的帮助信息
- 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
## 定义函数
- 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回，没有return语句自动返回None
- 空函数 pass关键字
- isinstance检查参数类型 `if not isinstance(x, (int, float)):`
- 返回多个值，`x, y = move(100, 100, 60, math.pi / 6)`，其实是返回了一个元组（在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值）
## 函数参数
### 位置参数 调用函数时，传入的实参按照位置顺序与形参绑定
### 默认参数
- `def power(x, n=2)`
- 调用带有默认参数的函数，默认参数可以按顺序传入
- 不按照顺序传入默认参数时，可以显式指定使用的默认参数
- 定义默认参数要牢记一点：默认参数必须指向不变对象。Python函数在定义的时候，默认参数L的值就被计算出来了，如果默认参数不是不可变对象，那么默认参数将会有记忆性！
```
# 错误的写法
def add_end(L=[]):
    L.append('END')
return L
# 利用None这个不可变对象改进
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
return L
```
### 可变长参数
- `def calc(*numbers)`，函数内部参数接受一个元组
- 如果已经有一个list或者tuple，可以在实参前加上`*`，将其与可变长形参关联
### 关键字参数
- `def person(name, age, **kw)`
- 将关键字参数封装为一个dict
- 同样，当已经拥有一个dict时，可以在实参前加上`**`，将其与关键字参数关联
### 命名关键字参数
- `def person(name, age, *, city, job)`或者`def person(name, age, *args, city, job)`
- 限制关键字参数的名字，调用函数时命名关键字参数必须传入参数名
- 如果没有可变参数，就必须加一个`*`作为特殊分隔符。如果缺少`*`，Python解释器将无法识别位置参数和命名关键字参数
### 参数组合
- 各种参数之间可以自由组合，但是需要满足顺序：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
- 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
## 递归函数
- 尾递归：尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
- 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环
- Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题
---
# 高级特性
## 切片 Slice （Java中的substring）
> 取一个list或tuple的部分元素
- `L[a:b]`，取`[a,b)`
- 如果索引a是0，a可以省略
- 倒数切片 `L[a,b]`，取`[a,b]`范围的元素，b从-1开始
- 指定切片步长 `L[a:b:c]`
- 所有数字 `L[:]`，复制数组
- tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
## 迭代
- list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
- 默认情况下，dict迭代的是key。如果要迭代value，可以用`for value in d.values()`，如果要同时迭代key和value，可以用`for k, v in d.items()`
- 字符串也是可迭代对象，迭代字符串里的字符
- 通过isinstance判断是否是Iterable实例从而判断是否是可迭代对象
- 在迭代时访问下标：使用enumerate函数 `for key, value in enumerate(['A', 'B', 'C'])`
- 在迭代循环中可以同时引用多个变量，每个变量与迭代元素中的项一一对应
## 列表生成器
> 快速创建一个list
- `L=[action for x in Li statement]` 对Li中的每一个元素进行statement判断之后，进行action操作
- 使用嵌套循环输出全排列
```
[m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```
- 列表生成器也可以使用多个变量
- **for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else**
## 生成器
> 利用创建规则创建一个生成器，依次获取list的值而不是一下子创建一个完整的list，节约了内存空间
- 列表生成器 `L = [x * x for x in range(10)]`，生成器`g = (x * x for x in range(10))`，区别仅在于最外层的[]和()
- 每次调用next函数，计算生成器的下一个值，当没有更多元素时，抛出StopIteration异常
- 一般通过for循环迭代生成器对象
- 使用yield可以将一个函数变成一个生成器，变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行，一般使用for循环迭代
- 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束
## 迭代器
- 可以直接作用于for循环的对象统称为可迭代对象：Iterable，可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
- 生成器都是Iterator对象，但list、tuple、dict、set、str虽然是Iterable，却不是Iterator。把list、dict、str等Iterable变成Iterator可以使用iter()函数
- Python的for循环本质上就是通过不断调用next()函数实现的
---
# 函数式编程
- 函数式编程——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算
- 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
- Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言
## 高阶函数
- 变量可以指向函数，函数名也是变量
- 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
### map
- map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
### reduce
- reduce把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
```
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> reduce(fn, [1, 3, 5, 7, 9])
13579
```
### filter
- filter()接收一个函数和一个序列,把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
- 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
### sorted
- sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
- 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
## 函数作为返回值
- 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
## 闭包
- 在一个函数之中定义了一个内部函数，内部函数可以引用外部函数的参数和局部变量，当外部函数返回内部函数时，相关参数和变量都保存在返回的函数中
- 注意到返回的内部函数在其定义内部引用了外部函数的局部变量，所以当一个函数A返回了一个函数B后，A内部的局部变量还被B函数引用
- 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
- 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
- 词法作用域与动态作用域
    - 词法作用域（静态作用域）是在书写代码或者说定义时确定的，而动态作用域是在运行时确定的
    - 词法作用域关注函数在何处声明，而动态作用域关注函数从何处调用，其作用域链是基于运行时的调用栈的
    - 词法作用域的函数中遇到既不是形参也不是函数内部定义的局部变量的变量时，去函数定义时的环境中查询。动态域的函数中遇到既不是形参也不是函数内部定义的局部变量的变量时，到函数调用时的环境中查。
## 匿名函数
- 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
- 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
## 装饰器
- 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
- 注解+装饰者模式实现AOP功能？
```
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
```
- 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂
```
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```
## 偏函数
- `functools.partial`就是帮助我们创建一个偏函数的
- 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单，无需自己写一个包装函数
- 创建偏函数时，实际上可以接收函数对象、`*args`和`**kw`这3个参数
---
# 模块
- 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）
- 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
- 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块
- 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块
## 作用域
- 有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
- 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，一般用于标记，自己的变量一般不要用这种变量名
---
# 面向对象编程
- 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数
- 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念
- 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
  而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递
- 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）
- 面向对象的设计思想是抽象出Class，根据Class创建Instance
- 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法
## 类与实例
### 类的定义
- class后面紧接着是类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
```
class Student(object):
    pass
```
### 构造函数 __init__
- __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
- 和普通的函数相比，在类中定义的函数（方法）只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
### 数据封装
- 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节、
- 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
## 访问限制
- 让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
- 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
## 继承与多态
- 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）
- 当子类存在与父类一样的方法时，子类的方法覆盖了父类的方法
- 啥是多态：在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
- 多态的好处：调用一个函数或者方法时，可以传入父类和其对应的任何子类，编译器自动调用实际类型的方法
- 动态语言的“鸭子类型”：它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子（只要一个对象有对应的方法，即可调用）
## 获取对象信息
### type()
- 判断基本数据类型可以直接写int，str
- 判断一个对象是否是函数：可以使用types模块中定义的常量
### isinstance()
- 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
- isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
- 还可以判断一个变量是否是某些类型中的一种：`isinstance([1, 2, 3], (list, tuple))`
### dir()
- 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
- 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
- 如果试图获取不存在的属性，会抛出AttributeError的错误，可以传入一个default参数，如果属性不存在，就返回默认值
## 实例属性和类属性
- 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性
- 如果不是绑定在self上的属性，其为类属性，相当于Java的静态属性
## 使用__slots__
> 限制实例的属性
- 例子：只允许添加name、age属性
```
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```
- __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
## 使用@property
- 对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的
- 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
```
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

>>> s = Student()
>>> s.score = 60 # OK，实际转化为s.set_score(60)
>>> s.score # OK，实际转化为s.get_score()
60
>>> s.score = 9999
Traceback (most recent call last):
  ...
ValueError: score must between 0 ~ 100!
```
- 可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
## 多重继承
- 多重继承可以避免类的爆炸
```
class Dog(Mammal, Runnable):
    pass
```
- MixIn 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn
- MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
## 定制类
> 自定义惯用方法实现类的定制
### __str__ （相当于Java的toString方法）
- 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
### __iter__
- 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
### __getitem__
- 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
### __setitem__
- 把对象视作list或dict来对集合赋值
### __delitem__
- 用于删除某个元素
### __getattr__
- 在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
- 可以把一个类的所有属性和方法调用全部动态化处理，实现链式调用
### __call__
- 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
```
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.
```
- 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
## 枚举类
- 当需要定义大量常量时，可以为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能
```
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
```
- 示例
```
class StatusCode(Enum):
    SUCCESS = 2000
    BAD_REQUEST = 4000
    PARAMETER_ERROR = 4001
    FORBIDDEN = 4003
    SERVER_ERROR = 5000
```
- value属性则是自动赋给成员的int常量，默认从1开始计数
- 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
- @unique装饰器可以帮助我们检查保证没有重复值
```
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```
- 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
- Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
## 使用元类
### type()
- 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
- type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
```
>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
```
- 要创建一个class对象，type()函数依次传入3个参数
    - class的名称；
    - 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    - class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
- 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
- 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂
### metaclass
- 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
- 先定义metaclass，就可以创建类，最后创建实例
- metaclass允许你创建类或者修改类
- 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
## 实例方法、类方法、静态方法
### Python的三种方法
- 普通实例方法，第一个参数需要是self，它表示一个具体的实例本身
- 如果用了classmethod注解，它的第一个参数不是self而是cls，它表示这个类本身
- 如果用了staticmethod注解，那么就可以无视这个self，而将这个方法当成一个普通的函数使用
- 实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用
### 类方法与静态方法的区别
- 类方法用在模拟java定义多个构造函数的情况：由于python类中只能有一个初始化方法，不能按照不同的情况初始化类
```
class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def class_method_create(cls, title):
        book = cls(title=title)
        return book

    @staticmethod
    def static_method_create(title):
        book= Book(title)
        return book

book1 = Book("use instance_method_create book instance")
book2 = Book.class_method_create("use class_method_create book instance")
book3 = Book.static_method_create("use static_method_create book instance")
print(book1.title)
print(book2.title)
print(book3.title)
```
- 类中静态方法方法调用静态方法和类方法调用静态方法：静态方法调用另一个静态方法，如果改用类方法调用静态方法，可以让cls代替类
```
class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():  # 在静态方法中调用静态方法
        print "在静态方法中调用静态方法"
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):  # 在类方法中使用静态方法
        print "在类方法中使用静态方法"
        return cls.averag(cls.X, cls.Y)

foo = Foo()
print(foo.static_method())
print(foo.class_method())
```
- 继承类中的区别？
---
# 异常处理
## 错误处理
- `try...except...finally...`机制：当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块
```
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
```
- 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
- 所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
- raise抛出一个异常
- raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
## 调试
### 打印大法 print
### 断言 assert
- 启动Python解释器时可以用-O参数来关闭assert。关闭后可以把所有的assert语句当成pass来看
### 日志 logging
### 调试器 pdb
> 以参数-m pdb启动
- 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
- 输入命令l来查看代码
- 输入命令n可以单步执行代码
- 输入命令p 变量名来查看变量
- 输入命令q结束调试，退出程序
### 设置断点 pdb.set_trace()
- 程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
## 单元测试
> 测试驱动开发（TDD：Test-Driven Development）
- 单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对abs()函数原有的行为造成影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试
- 为了编写单元测试，我们需要引入Python自带的unittest模块
- 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承
- 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
- unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()
- 另一种重要的断言就是期待抛出指定类型的Error
- 在命令行通过参数-m unittest直接运行单元测试
- 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
## 文档测试
> 自动执行写在注释中的代码
- 当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行
---
# IO
- IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。
- 同步和异步的区别就在于是否等待IO执行的结果
## 文件读写
### 读取文件
- 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
    - 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在
    - 如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
    - 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list（如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便）
    - 调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
- 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现
```
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
```   
- Python引入了with语句来自动帮我们调用close()方法
```
with open('/path/to/file', 'r') as f:
    print(f.read())
```
### file-like Object
- 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行
- StringIO就是在内存中创建的file-like Object，常用作临时缓冲
### 二进制文件
- 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
### 字符编码
- 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件 `f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')`
### 写文件
- 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
- 可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了
- 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
## StringIO与BytesIO
> 很多时候，数据读写不一定是文件，也可以在内存中读写。StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口
### StringIO
- StringIO顾名思义就是在内存中读写str
- 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
- getvalue()方法用于获得写入后的str
### BytesIO
- 如果要操作二进制数据，就需要使用BytesIO
## 操作文件与目录
> Python内置的os模块也可以直接调用操作系统提供的接口函数
- `print(os.name)` 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
- 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，要获取某个环境变量的值，可以调用`os.environ.get('key')`
- 查看当前目录的绝对路径 `os.path.abspath('.')`
- 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来 `os.path.join('/Users/michael', 'testdir')`（把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符）
- 创建一个目录 `os.mkdir('/Users/michael/testdir')`
- 删掉一个目录 `os.rmdir('/Users/michael/testdir')`
- 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名（可以直接让你得到文件扩展名）
- 对文件重命名 `os.rename('test.txt', 'test.py')`
- 删掉文件 `os.remove('test.py')`
- 复制文件 shutil模块提供了copyfile()的函数，还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
- 获取拓展名 `os.path.splitext(x)`
## 序列化
### Pickle
- pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
- 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
- 反序列化得变量和原来的变量是完全不相干的对象，它们只是内容相同而已
- Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系
### Json
> Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
- Json与Python数据类型对应表

|JSON类型|Python类型|
|----|----|
|{}	|dict|
|[]	|list|
|"string"	|str|
|1234.56	|int或float|
|true/false	|True/False|
|null	|None
- json.dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
- 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
- 定制类序列化：可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为自定义类专门写一个转换函数，再把函数传进去即可
- 转换任意的类 `json.dumps(s, default=lambda obj: obj.__dict__)`，因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
---
# 进程与线程
- 对于操作系统来说，一个任务就是一个进程（Process）
- 在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）
- 由于每个进程至少要干一件事，所以，一个进程至少有一个线程
## 多进程
- Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
- 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
- 利用`os模块中的fork()创建进程`（仅限于Linux）
```
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
```
- multiprocessing模块提供了一个Process类来代表一个进程对象（跨平台）
- Pool 进程池：启动大量的子进程，可以用进程池的方式批量创建子进程
- subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
- 进程间通信 Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
- 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了
## 多线程
> Python的线程是真正的Posix Thread，而不是模拟出来的线程
- Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块
### 创建线程
- 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
- 主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2
```
t = threading.Thread(target=loop, name='LoopThread')
t.start()
```
### Lock
- 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
```
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

```
### 多核CPU
- Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核
- Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响？？？
## ThreadLocal
- 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁
- **但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦**
- ThreadLocal的使用
    - 创建全局ThreadLocal ` tl = threading.local()`
    - 绑定 `tl.val = xxx`
    - 获取 `tl.val`
- ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
- 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
## 进程与线程
### 计算密集型 vs. IO密集型
- 计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写
- 第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。
### 异步IO
- 如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务
- 在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势
- 对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。我们会在后面讨论如何编写协程
## 分布式进程
> 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上
- Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序
---
# 正则表达式
## 基础
- 如果直接给出字符，就是精确匹配
- 用\d可以匹配一个数字
- 用\w可以匹配一个字母或数字
- 用.可以匹配任意字符
- 匹配变长字符串 用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
- 用\s可以匹配一个空格（也包括Tab等空白符）
## 进阶
- 要做更精确地匹配，可以用[]表示范围，比如`[0-9]`、`[a-z]`、`[A-Z]`
- A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'
- ^表示行的开头，^\d表示必须以数字开头
- $表示行的结束，\d$表示必须以数字结束
## re模块
- Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意（强烈建议使用Python的r前缀，就不用考虑转义的问题了）
- match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
## 分组
- 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
- 如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来，groups获取一个列表
- 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
## 贪婪匹配
- 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
- 加个?就可以让\d+采用非贪婪匹配
## 编译与预编译
- 在Python中使用正则表达式时，re模块内部会干两件事情：
    - 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
    - 用编译后的正则表达式去匹配字符串。
- 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配
- 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串
---
# 常用内建模块
> Python之所以自称“batteries included”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用
## datetime
> 时间与日期
## collections
> 高级集合
## base64
> Base64是一种用64个字符来表示任意二进制数据的方法
## struct
> 解决bytes和其他二进制数据类型的转换
## hashlib
> 提供了常见的摘要算法，如MD5，SHA1等
## hmac
> Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
## itertools
> 提供了非常有用的用于操作迭代对象的函数
## contextlib
> 只要正确实现了上下文管理，就可以用于with语句
## urllib
> urllib提供了一系列用于操作URL的功能
## XML
> 操作XML
## HTMLParser
> 解析HTML
- HTMLParser自动将tag和attrs都转为小写
- 自定义一个类，继承自HTMLParser，实现其方法
- 实际上很垃圾
---
# 常用第三方库
## Pillow
> PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了
## requests
> 一个Python第三方库，处理URL资源特别方便
## charset
> 检测编码
## psutil
>在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用
---
# 虚拟环境
> 在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。所有第三方的包都会被pip安装到Python3的site-packages目录下
- 每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境（virtualenv是第三方库）
## 安装
- pip3 install virtualenv
## 创建虚拟环境
0. 记单词：virtual 虚拟的，environment 环境
1. 创建目录 `mkdir myproject`、`cd myproject`
2. 创建一个独立的Python运行环境，命名为venv `virtualenv --no-site-packages venv` （加上了参数--no-site-packages，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境）
3. 新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境 `source venv/bin/activate`
## PyCharm创建虚拟环境
1. Setting -> Project -> Project Interpreter
2. Add -> Virtual Environment
## 原理
- virtualenv是如何创建“独立”的Python运行环境的呢？原理很简单，就是把系统Python复制一份到virtualenv的环境，用命令source venv/bin/activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境
---
# GUI
> Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写
- 我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。所以，我们的代码只需要调用Tkinter提供的接口就可以了
--- 
# 网络编程
> 网络编程对所有开发语言都是一样的，Python也不例外。用Python进行网络编程，就是在Python程序本身这个进程内，连接别的服务器进程的通信端口进行通信
## TCP/IP
## TCP编程
## UDP编程
---
# 电子邮件
- 电子邮件软件被称为MUA：Mail User Agent——邮件用户代理
- Email从MUA发出去，不是直接到达对方电脑，而是发到MTA：Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商，比如网易、新浪等等
- 发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议
- 收邮件时，MUA和MDA使用的协议有两种：POP：Post Office Protocol，目前版本是3，俗称POP3；IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等
## SMTP发送邮件
- SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件
- Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
## POP3接收邮件
- Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件
- POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象
---
# 数据库操作
## 访问SQLite
- SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成
- Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用
## 访问Mysql
- MySQL是Web世界中使用最广泛的数据库服务器
## SQLAlchemy
- 数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个list表示多行，list的每一个元素是tuple，表示一行记录。
- 但是用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来。（即ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上）
---
# Web开发
## HTTP协议
## WSGI接口
- WSGI（Web Server Gateway Interface）接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求
- python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用
## Web框架
- Django：全能型Web框架；
- web.py：一个小巧的Web框架；
- Bottle：和Flask类似的Web框架；
- Tornado：Facebook的开源异步Web框架。
## 模板
---
# 异步IO
## 协程
> 协程，又称微线程，纤程。英文名Coroutine
- 子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
- 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
- 协程的特点在于是一个线程执行
- 协程最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显
- 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多
- 利用多核CPU最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能
- Python对协程的支持是通过generator实现的。在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
- 子程序就是协程的一种特例 —— Donald Knuth
## asyncio
> asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
- 异步操作需要在coroutine中通过yield from完成
- 多个coroutine可以封装成一组Task然后并发执行
## async/await
> 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读
- async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换
    - 把@asyncio.coroutine替换为async
    - 把yield from替换为await
## aiohttp
> asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架