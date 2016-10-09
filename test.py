#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 选择排序
# test = [1,22,3,4,645,34,42,-5,12,543]
#
#
# for j in range(len(test)):
#     start = j
#     for i in range(j,len(test)):
#         if test[i] < test[start]:
#             start = i
#     tmp = test[start]
#     test[start] = test[j]
#     test[j] = tmp
#
# print(test)
#
#
#
#
# 插入排序
# data_set = [ 9,1,22,9,31,-5,45,3,6,2,11 ]
# for i in range(len(data_set)):
#     #position  = i
#     while i > 0 and data_set[i] < data_set[i-1]: # 右边小于左边相邻的值
#         tmp = data_set[i]
#         data_set[i] = data_set[i-1]
#         data_set[i-1] = tmp
#         i -= 1

# 希尔排序
data_set = [9, 1, 22, 9, 31, -5, 45, 3, 6, 2, 11]

import random
# data_set = [random.randrange(1,2000000) for i in range(1,2000000)]
step = int(len(data_set)/2)
while step >= 1:
    for i in range(len(data_set) - step):
        if data_set[i] > data_set[i + step]:
            data_set[i],data_set[i + step] = data_set[i + step],data_set[i]

    step = int(step/2)
else:
    for i in range(len(data_set)):
        while i > 0 and data_set[i] < data_set[i-1]: # 右边小于左边相邻的值
            tmp = data_set[i]
            data_set[i] = data_set[i-1]
            data_set[i-1] = tmp
            i -= 1
print(data_set)




# 1.将一个字符串逆序，不能使用反转函数

a = 'asfdjgsuyfgsydu'
temp = []
for i in a:
    temp.insert(0,i)
t = ''
for i in temp:
    t += i
print(t)


# 2.求从10到100中能被3或5整除的数的和

start = 0
for i in range(10,101):
    if i%3 or i%5:
        start += i
print(start)


# 3.Python是什么？使用Python的好处是什么?

# Python, 是一种面向对象、解释型计算机程序设计语言，由Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。
# Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)协议。
# Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。

# Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。
# 常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中[2]
# 有特别要求的部分，用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。
# 需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现

# 4.什么是 PEP 8?

# PEP8 是Python事实上的代码风格指南
# 是你的代码遵守PEP8 规则是一个好主意，当你和其他开发者共同完成一个项目时，他会是你代码更兼容。


# 5.What is pickling and unpickling?


# pickle模块接受任何Python对象并将它转换成一个字符串表示形式和转储到一个文件，利用自卸功能，这个过程被称为酸洗。而从存储的字符串表示形式检索原始Python对象的过程称为状态。

# 6.How Python is interpreted?

# 解释型语言就是编译成中间代码程序，在执行时靠翻译程序一起执行，边翻译边执行，当然是靠翻译程序才可以达到跨平台。


# 7.What are the tools that help to find bugs or perform static analysis?

# pylint


# 8.What are Python decorators?

# Python的装饰是一个具体的变化，我们在Python语法功能很容易改变。

# 9.What is the difference between list and tuple?

# 列表是Python的一种内置数据类型，list是一种有序的集合，可以随时添加和删除其中的元素。
# 获取list中的元素用角标获取，角标可以使用正角标，也可以使用负角标，越界时抛出IndexErro
# list中的元素的数据类型也可以不一样（就像Java一样），也可以在list内放另外一个list，这样也就形成了一个多维集合
#
# 元祖也是一种有序列表，和list非常类似，不同点是tuple一旦定义了就不可修改，在一定意义上这也提高了代码的安全性，查询方法和list一样，使用的时候能用tuple的就用tuple。
# 在定义只有一个元素的元祖时加入"逗号"以免产生和数学运算的歧义


# 10.What are the built-in type does python provides?什么是内置式Python提供了吗？

# 有可变和不可变的内置类型的内置类型的蟒蛇类型
#
# 列表
# 套装
# 词典
# 一成不变的内置类型
#
# 字符串
# 多元组
# 数

# 11.What is namespace in Python?命名空间在Python中是什么？
# 在Python中，每个名字都介绍有一个地方在它生活的地方，可以沉迷。这是被称为命名空间。它像一个盒子，一个变量名称映射到对象放置。当变量被搜了出来，这个盒子将被搜索，得到相应的对象。

# 12.What is lambda in Python?

# 这是一个表达的匿名函数经常被用来作为内联函数。

# 13.In Python what are iterators?

# 在Python中，迭代器用于迭代的一组元素，容器类列表。

# 14.What is unittest in Python?什么是单元测试在Python？

# Python中的单元测试框架被称为单元测试。它支持共享设置，自动化测试，测试关机代码，测试收藏等聚集

# 15.What are generators in Python?生成器在Python中是什么？

# 实现迭代器的方式称为生成器。这是一个正常的功能外，它的收益率的函数表达式。

# 16.How can you copy an object in Python?
# 深拷贝和浅拷贝
#复制在Python对象，你可以试着copy.copy（）或复制。在一般情况下deepcopy()。你不能复制所有对象，但大多。


# 17.What is module and package in Python?模块和包在Python中是什么？

# 在Python中，模块结构的编程方法。每个Python程序文件是一个模块，其中进口其他模块对象和属性。
#
# Python程序的文件夹是一个封装模块。一个包可以有模块或子文件夹。

# 18.Mention what are the rules for local and global variables in Python?提到Python中的局部变量和全局变量的规则是什么？

# 局部变量：如果一个变量被分配一个新的价值功能的身体内的任何地方，它被假定为本地。
#
# 全局变量：那只引用在函数内部的变量是隐式的全球。

# 19.Explain how can you make a Python Script executable on Unix?解释你如何在Unix使Python脚本执行？

# 在Unix使Python脚本的可执行文件，你需要做两件事情，
#
# 脚本文件的方式必须是可执行的，
# 第一行必须从#（#！/usr/local/bin或Python）

# 20.Explain how to delete a file in Python?解释如何删除Python的文件吗？

# 用一个命令os.remove（文件名）或取消（文件名）的操作系统。


# 21.How can you share global variables across modules?你怎么能跨模块共享全局变量？

#共享全局变量在模块在一个单一的程序，创建一个特殊的模块。在你的应用程序的所有模块导入配置模块。该模块将作为整个模块的全局变量。



# 22.Explain how can you generate random numbers in Python?解释你如何在Python中产生随机数？

# random.random()用于生成

# 23.Explain how can you access a module written in Python from C?解释你如何访问一个模块用Python写的C？

# import导入


# 24.Mention the use of // operator in Python?


# 25.Mention five benefits of using Python? python的好处



# 26.a=1, b=2, 不用中间变量交换a和b的值
# a,b = 2,1

# 27.请用自己的算法, 按升序合并如下两个list, 并去除重复的元素
list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
list3 = list(set(list1+list2))
print(list3)


# 28 写一个简单的socket
import socket

sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen(5)

conn,address = sk.accept()
sk.sendall(bytes("Hello world",encoding="utf-8"))


import socket

obj = socket.socket()
obj.connect(("127.0.0.1",8080))

ret = str(obj.recv(1024),encoding="utf-8")
print(ret)

# 29.请描述set的用途并举例说明
# 是一个无序且不重复的元素集合


# 30. 请简述python2.x 与python3.x的主要区别

