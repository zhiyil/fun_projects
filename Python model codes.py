# 1. 交换赋值
##不推荐
temp = a
a = b
b = a  

##推荐
a, b = b, a  #  先生成一个元组(tuple)对象，然后unpack

# 2. Unpacking
##不推荐
l = ['David', 'Pythonista', '+1-514-555-1234']
first_name = l[0]
last_name = l[1]
phone_number = l[2]  

##推荐
l = ['David', 'Pythonista', '+1-514-555-1234']
first_name, last_name, phone_number = l
# Python 3 Only
first, *middle, last = another_list

# 3. 使用操作符in
##不推荐
if fruit == "apple" or fruit == "orange" or fruit == "berry":
    # 多次判断  

##推荐
if fruit in ["apple", "orange", "berry"]:
    # 使用 in 更加简洁

# 4. 字符串操作
##不推荐
colors = ['red', 'blue', 'green', 'yellow']

result = ''
for s in colors:
    result += s  #  每次赋值都丢弃以前的字符串对象, 生成一个新对象  

##推荐
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)  #  没有额外的内存分配

# 5. 字典键值列表
##不推荐
for key in my_dict.keys():
    #  my_dict[key] ...  

##推荐
for key in my_dict:
    #  my_dict[key] ...

# 只有当循环中需要更改key值的情况下，我们需要使用 my_dict.keys()
# 生成静态的键值列表。

# 6. 字典键值判断
##不推荐
if my_dict.has_key(key):
    # ...do something with d[key]  

##推荐
if key in my_dict:
    # ...do something with d[key]

# 7. 字典 get 和 setdefault 方法
##不推荐
navs = {}
for (portfolio, equity, position) in data:
    if portfolio not in navs:
            navs[portfolio] = 0
    navs[portfolio] += position * prices[equity]
##推荐
navs = {}
for (portfolio, equity, position) in data:
    # 使用 get 方法
    navs[portfolio] = navs.get(portfolio, 0) + position * prices[equity]
    # 或者使用 setdefault 方法
    navs.setdefault(portfolio, 0)
    navs[portfolio] += position * prices[equity]

# 8. 判断真伪
##不推荐
if x == True:
    # ....
if len(items) != 0:
    # ...
if items != []:
    # ...  

##推荐
if x:
    # ....
if items:
    # ...

# 9. 遍历列表以及索引
##不推荐
items = 'zero one two three'.split()
# method 1
i = 0
for item in items:
    print i, item
    i += 1
# method 2
for i in range(len(items)):
    print i, items[i]

##推荐
items = 'zero one two three'.split()
for i, item in enumerate(items):
    print i, item

# 10. 列表推导
##不推荐
new_list = []
for item in a_list:
    if condition(item):
        new_list.append(fn(item))  

##推荐
new_list = [fn(item) for item in a_list if condition(item)]


# 11. 列表推导-嵌套
##不推荐
for sub_list in nested_list:
    if list_condition(sub_list):
        for item in sub_list:
            if item_condition(item):
                # do something...  
##推荐
gen = (item for sl in nested_list if list_condition(sl) \
            for item in sl if item_condition(item))
for item in gen:
    # do something...

# 12. 循环嵌套
##不推荐
for x in x_list:
    for y in y_list:
        for z in z_list:
            # do something for x &amp;amp; y  

##推荐
from itertools import product
for x, y, z in product(x_list, y_list, z_list):
    # do something for x, y, z

# 13. 尽量使用生成器代替列表
##不推荐
def my_range(n):
    i = 0
    result = []
    while i &amp;lt; n:
        result.append(fn(i))
        i += 1
    return result  #  返回列表

##推荐
def my_range(n):
    i = 0
    result = []
    while i &amp;lt; n:
        yield fn(i)  #  使用生成器代替列表
        i += 1
# *尽量用生成器代替列表，除非必须用到列表特有的函数。

# 14. 中间结果尽量使用imap/ifilter代替map/filter
##不推荐
reduce(rf, filter(ff, map(mf, a_list)))

##推荐
from itertools import ifilter, imap
reduce(rf, ifilter(ff, imap(mf, a_list)))
# *lazy evaluation 会带来更高的内存使用效率，特别是当处理大数据操作的时候。

# 15. 使用any/all函数
##不推荐
found = False
for item in a_list:
    if condition(item):
        found = True
        break
if found:
    # do something if found...  

##推荐
if any(condition(item) for item in a_list):
    # do something if found...

# 16. 属性(property)
##不推荐
class Clock(object):
    def __init__(self):
        self.__hour = 1
    def setHour(self, hour):
        if 25 &amp;gt; hour &amp;gt; 0: self.__hour = hour
        else: raise BadHourException
    def getHour(self):
        return self.__hour

##推荐
class Clock(object):
    def __init__(self):
        self.__hour = 1
    def __setHour(self, hour):
        if 25 &amp;gt; hour &amp;gt; 0: self.__hour = hour
        else: raise BadHourException
    def __getHour(self):
        return self.__hour
    hour = property(__getHour, __setHour)

# 17. 使用 with 处理文件打开
##不推荐
f = open("some_file.txt")
try:
    data = f.read()
    # 其他文件操作..
finally:
    f.close()

##推荐
with open("some_file.txt") as f:
    data = f.read()
    # 其他文件操作...

# 18. 使用 with 忽视异常(仅限Python 3)
##不推荐
try:
    os.remove("somefile.txt")
except OSError:
    pass

##推荐
from contextlib import ignored  # Python 3 only

with ignored(OSError):
    os.remove("somefile.txt")

# 19. 使用 with 处理加锁
##不推荐
import threading
lock = threading.Lock()

lock.acquire()
try:
    # 互斥操作...
finally:
    lock.release()

##推荐
import threading
lock = threading.Lock()

with lock:
    # 互斥操作...

# 20. 参考
# 1) Idiomatic Python: 

# http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html

# 2) PEP 8: Style Guide for Python Code: 

# http://www.python.org/dev/peps/pep-0008/                    