# hello word
print('hello world')

# python变量是一个指针， 指向一块内存空间, 跟随赋值运算符出现。
v = 1

# 变量的命名规则: 只能包含数字、字母和下划线， 只能以字母或者下划线开始，不能使用python解释器的保留字。
# 运算符： 算数运算符通常只针对数值类型，python是强类型的动态语言，一旦定义好类型无法改变，变量可以赋值。
# 比较运算符： == 相等， ！= 不等于， > 大于， >= 大于等于， < 小于， <= 小于等于，
# 逻辑运算符： 参与运算的成员只能是bool类型， 或者可以隐式转化为bool类型的 True, False, not True, 断路操作（从左往右计算）
# 位运算符

# 运算符的优先级： 算数运算符>比较运算符>逻辑运算符

# 表达式： 变量、常量、运算符组成

# -----  程序控制结构 -----
# 顺序结构
# 分支结构
 # 单分支结构
if 1 < 2:
    print('1 less than 2')
print('main block')
 # 双分支结构
if 1 < 2:
    print('1 less than 2')
else:
    print('1 bigger than 2')
 # 多分支结构
if 1 < 1:
    print('1 less than 1')
elif 1 > 1:
    print('1 bigger than 1 ')
else:
    print('err')

# 循环遍历: 循环体中绝对不要修改可迭代对象
# while 循环，循环体重需要修改条件，以使得条件为假
a = 1
while a < 10:
    print(a)
    a+=1

for i in range(0, 10):
    print(i)

# break 用于提前结束循环, continue 用于跳过之后的语句
for i in range(0, 10):
    if i == 3:
        continue
    print(i)

### ----- 内置数据结构 -----
# 五种内置数据结构： 列表、元组、字符串、集合、字典
# 解析式: 列表解析、生成器解析、集合解析、字典解析， 后三种python3 特有

# 线性结构： 列表、元组、字符串， 可以进行切片操作、解包封包。

# 列表的初始化
lst = list()
lst1 = []
lst2 = [1,2,3]
print(lst2,lst1,lst)

# 列表的下标/索引操作
print(lst2[0])
print(lst2[1])
print(lst2[-1])

# 列表元素的修改, 修改不存在的index位， 提示IndexError
lst = [1,23,2]
lst[0] = 1
lst[1] = 10
print(lst)

# 列表元素的增加：append,
help(list)
# --- append 追加单个元素
lst.append(12)
print(lst)

# --- insert: insert操作的索引超出范围，如果是正索引，等效与append， 如果是负索引，等效于insert(0,object)
lst.insert(1,22)
print(lst)

# --- extend: 追加多个元素
lst = [0,1,2,3,4,5]
lst.extend([23,13,23])
print(lst)

# 删除元素
# --- pop： 从最后移除元素
lst = [0,1,2,3,4,5]
print(lst.pop())
print(lst.pop(0))   ## 移除索引位置的值

# --- remove， 如果值不存在，抛出ValueError
lst = [90,11,1,23,4,5]
lst.remove(11)
print(lst)

# pop 为弹出索引对应的值， remove为删除从左边开始的第一个值。

# -- clear : 清除所有元素
lst = [12,32,12,42,23,41]
lst.clear()
print(lst)

#### ---- 查找统计元素 ----
# --- index  根据值查找索引
lst = ['a','b','a','c','d','a']
print(lst.index('a'))
print(lst.index('a',1))
print(lst.index('a',3,13))

# ---- count  统计值的出现次数
lst = ['a','b','a','c','d','a']
print(lst.count('a'))

# --- len 函数(内置函数)
lst = ['a','b','a','c','d','a']
print(len(lst))

# --- sort 排序函数
lst = ['a','b','a','c','d']
lst.sort()
print(lst)

# --- reverse 反转函数
lst = ['a','b','a','c','d']
lst.reverse()
print(lst)

# --- copy 方法
lst = ['a','b','a','c','d']
lst2 = lst.copy()
lst2.remove('a')
print(lst2)

print(id(lst))
print(id(lst2))

#### ---- 切片操作 ---- ####
lst = ['a','b','a','c','d']
# 从左往右的切片， 所以start一定要小于end,反之得到一个空列表
print(lst[0:2])
print(lst[2:-1])
print(lst[:2])

lst = list(range(0, 10))
print(lst)
print(lst[2:5:2])
print(lst[5:2:-1])   # 当step为负数的时候，从后往前数，此时start应该小于end 负责会返回孔列表。
print(lst[:-1])
print(lst[::-1])      # 反转

lst = list(range(0, 10))
print(lst[0::2])

# 对切片赋值，会替换切片原来的元素

#### ---- 解包封包 ---- ####
# 解包是把集合里的元素赋值给变量，
# 封包是把变量构建成元组
# 封包
def swap(a,b):
    a, b = b, a
    return (a, b)
print(swap(1,3))

x = 1
y = 3
x, y = y,x
print(x)
print(y)

t = 1,2,3,5
print(t)

# 解包
lst = [1, 2, 45, 23, 41, 49]

head, *tail = list(range(0, 10))
head, *mid, tail = [1, 3, 5 ,5, 8]
a, b, _, c, *_ = lst

lst = [1, [2, 3], 4]
a, (b, c), d = lst

lst = [1, [2,4,5,6,20], 10]
a, (b, *_, c), d = lst

#### ---- 字符串 ---- ####
# python3中是一个unicode序列， python2中是一个byte序列， 是一种数据结构,不可变对象

s = 'hello world'

# jobin 连接
lst = ['my', 'name', 'is', 'tomcat']
print(' '.join(lst))
print(','.join(lst))

# splite/rsplite, splitelines, partition, rpartition
s = 'my name is tomcat'
help(s.split())
print(s.split())
print(s.split('is'))
print(s.split(' ', 2))
print(s.split(' ', -1))

# 用法实例：
line = 'url:http://www.zenghui.wang'
print(line.split(':', 1))
key, value = line.split(':', 1)
print(key)
print(value)

line = 'url:http://www.zenghui.wang'
print(line.partition(':'))
key, *_, value = line.partition(':')
print(key)
print(value)

# capitalize 首字母大写
print(s.capitalize())

# title 所有字符首字母大写
print(s.title())

# lower 小写
# upper 大写
# swapcase 大小写转换


#### ---- 程序世界的修改 ---- ####

# center 填充， 默认空格
s = 'my name is tomcat'
print(s.center(80))
print(s.center(80,'#'))

# ljust/rjust 左/右填充
print(s.ljust(80))
print(s.ljust(80, '#'))
print(s.ljust(80) + '01')

# 0 填充
print(s.zfill(80))

# strip, lstrip, rstrip
s = ' hahaha ## nihao \n \t'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = '## test ##'
print(s.strip('#'))
