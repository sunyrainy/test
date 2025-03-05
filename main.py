# 这是一个示例 Python 脚本。


# 按 Ctrl+Alt+S 打开设置。
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
__name__ = '__main__'  # 定义 __name__ 变量。
__name__ = 'sqlite3'


if __name__ == '__main__':  # 判断是否是主模块
    print_hi('input PyCharm')
else:
    print_hi(f'output 1 PyCharm {__name__}')
    print_hi('output 1 PyCharm' + __name__)
print_hi('1 PyCharm')
print(__name__ * 2)  # 输出 __name__ * 2
print(__name__[2:7:2])
print(__name__[2:7:2])  # 输出 __name__[2:7:2]

print()
print(__name__, end="")
print(__name__[2:7:2], end="")  # 输出 __name__[2:7:2] 后不换行

statue = False  # 定义布尔变量
a = 4 + 3j  # 定义复数

isinstance(a, complex)  # 判断是否是复数True
print(a is complex)  # is 是判断是否是同一个对象False
del a  # 删除变量 a

complex(4, 3)  # 定义复数

b = True  # 定义布尔变量
c = False  # 定义布尔变量

print(b and not c)  # 输出 True
print(b or not c)  # 输出 True
print(not b)
print(statue)

array = [1, 2, 3, 4, 5]  # 定义数组
tupleValue = (1, 2, 3, 4, 5)  # 定义元组

print("---------------------")
"""
所有的数据类型都遵循连接的规则
元组和集合的区别在于
1.元组是不可变的，而集合是可变的。
2.元组的元素不能修改，而集合的元素可以修改。
"""
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

byteValue = b'Hello, world!'  # 定义字节串

a = 66
b = chr(a)
print(chr(a))  # 输出 ASCII 码对应的字符
print(str(a))  # 输出整数对应的字符串
print(float(a))  # 输出整数对应的字符串
print(ord(b))  # 输出字符对应的 ASCII 码

print(b is str)  # 输出 False
print(b is chr)  # 输出 True

a -= --a

"""
in 运算符用于判断一个值是否在指定的序列中
not in 运算符用于判断一个值是否不在指定的序列中
is 运算符用于判断两个变量是否引用同一个对象
is not 运算符用于判断两个变量是否引用不同对象
"""
e = 10
f = 20
list1 = [1, 2, 3, 4, 5]

if e in list1:
    print("1 - 变量 e 在给定的列表中 list 中")
else:
    print("1 - 变量 e 不在给定的列表中 list 中")

if f not in list1:
    print("2 - 变量 f 不在给定的列表中 list 中")
else:
    print("2 - 变量 f 在给定的列表中 list 中")

# 修改变量 a 的值
e = 2
if e in list1:
    print("3 - 变量 e 在给定的列表中 list 中")
else:
    print("3 - 变量 e 不在给定的列表中 list 中")

print("---------------------")
"""
del 语句用于删除一个对象
del 语句后面可以跟多个变量名，用逗号隔开，表示删除多个对象
del 语句也可以删除整个列表或字典，但不建议这么做
"""
del list1, e, f  # 删除多个对象

import math

x = -10.02
abs(x)  # 输出 x 的绝对值
math.ceil(x)  # 输出 x 的上入整数
math.exp(x)  # 输出 e 的 x 次幂
math.floor(x)  # 输出 x 的下舍整数
math.log(2)  # 输出 x 的自然对数
math.log10(10)  # 输出 x 的以 10 为底的对数
math.pow(x, 2)  # 输出 x 的 2 次幂
math.sqrt(4)  # 输出 x 的平方根

print(round(3.1415926, 2))  # 输出 3.14

print("---------------------")

array = []
print(array.__len__())  # 输出数组的长度
array.append(1)
array.append(2)
array.append(3)
array.pop()  # 删除数组的最后一个元素
print(array.__len__())  # 输出数组的长度
print(2 in array)
print(type(array))

print(isinstance(array, list))  # 判断是否是列表True

# 定义函数
if array.__len__() > 0:  # 判断数组是否为空`
    print(array.__len__())  # 输出数组的长度

for i in range(array.__len__()):  # 遍历数组
    print(array[i])  # 输出数组的元素

ite = iter(array)  # 创建迭代器
next(ite)  # 输出迭代器的第一个元素


def my_func(x):  # 定义函数
    while True:
        if x < 0:
            return  # 退出循环
        yield x  # 定义生成器
        x -= 1


my_gen = my_func(5)  # 调用函数生成器

print("-----------------------")

"""
生成器是一种特殊的迭代器，它不仅可以返回值，还可以产出值。
生成器函数使用 yield 语句来产出值，调用生成器函数时，函数会返回一个生成器对象。
生成器对象可以使用 next() 函数来获取下一个值，直到遇到 StopIteration 异常时退出循环。
"""

# for i in my_gen:  # 遍历生成器
#     print(i)  # 输出生成器的元素

while True:
    try:
        print(next(my_gen))  # 输出生成器的下一个元素
    except StopIteration:
        break  # 遇到 StopIteration 异常退出循环


def food_fun(x):  # 定义函数

    t = x.__len__()
    while True:
        if t <= 0:
            return  # 退出循环
        else:
            x.append(t)  # 尝试修改全局变量
            t -= 1


def foor_fool(a, b):  # 定义主函数

    while b > 0:
        a.append(b)  # 尝试修改全局变量
        b -= 1

    print(a)

    food_fun(a)  # 调用函数 food_fun
    if (a.__len__() > 20):
        print("food_fun_list 长度大于 20", end="")
        print(a)
        print(f"food_fun_list 长度大于 20，内容是{a}")
        return a
    else:
        foor_fool(a, 0)  # 递归调用函数


a = [1, 2, 3, 4, 5]  # 定义全局变量
foor_fool(a, 2)

print("---------------------")
"""
装饰器是 Python 高阶函数的一种，它可以用来修改其他函数的行为。
装饰器是一个函数，它接受一个函数作为参数，并返回一个修改过的函数。
"""


def repeat(n):
    def decorator(func):  # 定义装饰器函数
        def wrapper(*args, **kwargs):  # 定义装饰器函数
            for _ in range(n):  # 重复执行 n 次
                print(f"执行 {n} 次")
                result = func(*args, **kwargs)  # 调用被装饰函数
                print(result)
                print(type(result))
            return result
        return wrapper
    return decorator

@repeat(3)  # 调用装饰器
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
print("---------------------")

"""
字典的 update() 方法用于更新字典，如果字典中已有相同的键，则会覆盖原有的值。
字典的 pop() 方法用于删除字典中的元素。
"""

tel = {}
tel["Alice"] = "123456"
print(tel)
tel.update({"Alice": "654321"})
tel.update({"Bob": "123456"})
print(tel)
tel.pop("Alice")
print(tel)

from Tool import good  # 导入模块

Good = good.Good("xiaoming", 20)

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fib(10)

print("---------------------")

open("test.txt", "w").write("hello, world!")  # 写入文件
open("States", "w").write("hello, world!")  # 写入文件

fileObj = open("States", "a")
fileObj.write("\nhello, world1!")  # 追加写入文件
fileObj.write("\nhello, world2!")  # 追加写入文件
fileObj.write("\nhello, world3!")  # 追加写入文件
fileObj.close()

print("---------------------")

fTTT = open("States", "r")
stringValue = fTTT.readlines()  # 读取文件内容
Findex = fTTT.tell()  # 输出文件指针位置
print(Findex)
print(stringValue)
fTTT.close()

print("---------------------")

inputStr = input("你输入的是:")
print(inputStr)

print("---------1------------")
with open("States", "r") as fTTT:  # 读取文件内容
    stringValue = fTTT.readlines()
    Findex = fTTT.tell()
    print(Findex)
    print(stringValue)
    value = fTTT.fileno()
    print(value)

print("---------1-----------")
"""
pickle 模块可以将 Python 对象序列化成字节流，并将字节流写入文件。
pickle 模块可以将字节流反序列化成 Python 对象。
"""
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

selfref_list.append(data1)

output = open('data.pkl', 'wb')
pickle.dump(data1, output)  # 序列化对象并写入文件
pickle.dump(selfref_list, output, -1)  # 序列化对象并写入文件
output.close()


inputPickle = open('data.pkl', 'rb')  # 读取文件内容
data = pickle.load(inputPickle)  # 反序列化对象
print(data)

with open('data.pkl', 'rb') as inputPickle:  # 读取文件内容
    data = pickle.load(inputPickle)  # 反序列化对象
    print(data)
inputPickle.close()


print("---------------------")
"""
# 三元运算符
"""
a=10
a=1 if 10==1 else 2  # 三元运算符
print("---------------------")
str2 = "a"
num = 10
t = ord(str2)
print(t + 10)

print("---------------------")
"""
# 异常处理
"""
try:
    y = a/0
except (ZeroDivisionError, NameError):
    print("除数不能为0")


try:
    y = a/0
except (ZeroDivisionError, NameError) as error:
    print(error)
finally:
    print("try程序执行结束")

    try:
        y = a / 0
    except (ZeroDivisionError, NameError) as error:
        print(error)
    finally:
        print("try程序执行结束")

        # raise ValueError("自定义异常")  # 触发异常


print("---------------------")
"""
文件夹API
"""
import os
curr_dir =os.getcwd()  # 获取当前工作目录
print(curr_dir)

files = os.listdir(curr_dir)  # 获取当前目录下的文件列表
print("目录下的文件:", files)

"""
正则表达式
"""
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

"""
针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
"""
import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

"""
:mod:glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:
"""
import glob
glob.glob('*.py')

"""
日期时间
"""
import datetime

#获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-07-17 15:30:45


"""
数据压缩
模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
"""
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
zlib.decompress(t)
zlib.crc32(s)


# input('\n\n please input any key to exit.')  # 按 Enter 键退出脚本。


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
