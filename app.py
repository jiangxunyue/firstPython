import logging;
logging.basicConfig(
    level=logging.INFO
);
from datetime import datetime
from aiohttp import web
import asyncio
import threading
import functools


@asyncio.coroutine
def hello1():
    print("hello world1 (%s)"  % threading.current_thread())
    r = yield from asyncio.sleep(1)
    print("hello end1 (%s)"  % threading.current_thread())

@asyncio.coroutine
def hello2():
    print("hello world2 (%s)"  % threading.current_thread())
    r = yield from asyncio.sleep(2)
    print("hello end2 (%s)"  % threading.current_thread())

# 获取evenloop
loop = asyncio.get_event_loop()
# 两个coroutine是由同一个线程并发执行的。
tasks = [hello2(), hello1()]
print('---------------')
#执行coruntine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# 偏函数
max2 = functools.partial(max, 10)

print(max2(4, 5))


print()
arr = ['a', 'b', 'c']
# 数组的forin循环变量为元素本身
for item in arr:
    print(item)
# 将数组用enumerate转化为索引-元素对后，forin循环变量为index和元素本身
for index,item  in enumerate(arr):
    print(
        'index: %d,  value: %s' % (index, item)
    )
print()

arr2 = ('ab', 'bc', 'cd')

# 元组的forin循环变量为元素本身
for item in arr2:
    print(item)
# 将元组用enumerate转化为索引-元素对后，forin循环变量为index和元素本身
for index,item  in enumerate(arr2):
    print(
        'index: %d,  value: %s' % (index, item)
    )

dict1 = {'a': 1, 'b': 2, 'c': 3, 'aa': 11}
# dict的forin循环变量为key
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
for item in dict1:
    print('dict : %s' % item)

# 默认情况下，dict迭代的是key。
# 如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()
for value in dict1.values():
    print('dict value : %s' % value)

for key, value in dict1.items():
    print('dict key: %s | value : %s' % (key, value))

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
print('isinstance: %s' % isinstance('abc', Iterable))
print('enumerate(\'uvw\')  type: %s' % type(enumerate('uvw')))


for ch in enumerate('uvw'):
    print('str iterable: ', ch)

from collections import Iterable

print('isinstance: %s'  %  isinstance('abc', Iterable))


from sklearn import datasets
# iris = datasets.load_iris()
# digits = datasets.load_digits()
# print(digits.data)



import time
print('localTime: ', time.localtime(time.time()));
print(time.localtime(time.time()))

tup = ('physics', 'chemistry', 1997, 2000);

print(tup);

tup2 = tup * 2
print('tup2: ', tup2)
# del tup;
# print("After deleting tup : ")
# print(tup);


def printMM(*args):
    for var in args:
        print('var', var)


printMM('a', 1, 2)


sum = lambda arg1, *args: print(arg1, args);
sum('11', '22', 33)