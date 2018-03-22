'''
函数
'''
'''
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

return None可以简写为return。
'''


def my_abs(x):
    if x >= 0:
        return x
    else:
        return None

print(my_abs(-11))

def power(x, n = 2):
    return x * n

print(power(10))

def enroll(name, age, city = 'beijing', sex = 'man'):
    print(
        'name: ', name,
        '\nage: ', age,
        '\ncity: ', city,
        '\nsex: ', sex
    )

enroll(
    'xiaoming',
    10
)
print('\n')
# 可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('xiaolu', 12, sex='woman')
# 第三个参数不再是city，而是指定为sex；
enroll('xiaolu', 12, sex='woman')

'''
默认参数必须指向不变对象，
Python函数在定义的时候，默认参数的值就生成出来了，每次使用默认参数都会读取同一个值
'''
'''
默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：

先定义一个函数，传入一个list，添加一个END再返回：

def add_end(L=[]):
    L.append('END')
    return L
当你正常调用时，结果似乎不错：

>>> add_end([1, 2, 3])
[1, 2, 3, 'END']
>>> add_end(['x', 'y', 'z'])
['x', 'y', 'z', 'END']
当你使用默认参数调用时，一开始结果也是对的：

>>> add_end()
['END']
但是，再次调用add_end()时，结果就不对了：

>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

原因解释如下：

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

要修改上面的例子，我们可以用None这个不变对象来实现：

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
现在，无论调用多少次，都不会有问题：

>>> add_end()
['END']
>>> add_end()
['END']
为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
'''


'''
可变参数
我们把函数的参数改为可变参数：

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

>>> calc(1, 2)
5
>>> calc()
0
如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])
14
这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

>>> nums = [1, 2, 3]
>>> calc(*nums)
14
*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
'''

def numbersLength(*numbers):
    for n in numbers:
        print(n)

numbersLength(1, 2, 3)
print()
nums = [3, 4, 5];
numbersLength(*nums)

# 关键字函数
def keywordFunc(a, b, **kw):
    print('a: ', a, '\nb: ', b, '\nkw: ', kw)

# 关键字函数会将扩展参数组装为dict
keywordFunc(10, 11, key1='abc', key2='nmb')

# 要传递dict作为关键字参数，需要用**符号将dict展开
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {"key3": 'bbb', "key4": 'aaa'}
keywordFunc(12, 123, **extra)

# 命名关键字参数
'''
关键字参数不限制传入的键名，
为了限制传入的键名可以使用命名关键字函数
形式：
def nameKeyWordFunc(a, b, *, job, name):
    pass

'*'之前为普通参数(位置相关)，后面为关键字参数(位置无关，需要key=value形式传入)
'''
def nameKeyWordFunc(a, b, *, job='Engineer', name):
    print(a)
    print(b)
    print(job)
    print(name)

nameKeyWordFunc('ke', 'le', name='ddd')

'''
参数组合

在Python中定义函数，
可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

def groupArgsFunc(a, b, c, *variableArgs, **kw):
    print('----------------')
    print(a)
    print(b)
    print(c)
    print(variableArgs)
    print(kw)

arr = [1, 2, 3]
kw = {"key3" : '---', "key4": '====='}
groupArgsFunc('q', 'b', 'g', *arr, **kw)

'''
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

print(len(arr))

#  元组
t = ('a', 'b', ['A', 'B'])
print(t)

# 一个元素的元组需要加逗号，不然会被识别为数学运算的括号
t2 = (1, )
print(t2)

# pip3 安装
# 异步框架aiohttp：
#
# 前端模板引擎jinja2：
# MySQL 5.x数据库，从官方网站下载并安装，安装完毕后，请务必牢记root口令。为避免遗忘口令，建议直接把root口令设置为password；
# MySQL的Python异步驱动程序aiomysql：


# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
# x = b'ABC'

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# encode('ascii');
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print('中文: ', len('中文'))
print('中文bytes: ', len('中文'.encode('utf-8')))


# from multiprocessing import Process, Queue
# import os, time, random
#
# print('pid: ', os.getpid(), '\n__name__: ', __name__)
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()
#

# 装饰器
'''
装饰器
'''
import functools

def logBeginAndEnd(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('logBeginAndEnd: %s' % ('begin'))
        result = func(*args, **kw)
        print('logBeginAndEnd: end')
        return result
    return wrapper

@logBeginAndEnd
def func1():
    print('in func')

func1()
print(func1.__name__)
print()

# 带参数修饰器
def decorateWithText(text):
    def innerDecorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
             print('%s -------- begin' % text)
             returnValue = func(*args, **kw)
             print('%s -------- end' % text)
             return returnValue
        return wrapper
    return innerDecorate

# 应用多个修饰器
@logBeginAndEnd
@decorateWithText('===decorateWithText====')
def kka(args):
    print('_kkkk_______: %s' %args)

kka('iiiiiiii')
