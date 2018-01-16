#####   append, insert, index, remove, del, pop #####


# li = list([1,2,3])
# print(li)
# li.extend((11,22,))
# print(li)

# li = list([1,2,3])
# li.insert(0,'tomcat')
# print(li)

# li = list([1,34,21])
# li.append(12)
# print(li)
# 取列表中第0个元素（默认最后一个元素）
#li = list([1,54,62])
#print(li.pop(0))   # 取第一个值
#print(li.pop(1))   # 取第一个值
# print(li.pop())   # 取最后一个值

# 删除第一次出现的指定的值
# li = list([1,2,3,1])
# li.remove(1)
# li.remove(3)
# print(li)

# 将列表值反转
#li = [12,34,123,123]
#li.reverse()
#print(li)

#  列表元素排序
#  li = [123,34,1,23,142]
# li.sort()
# print(li)

# 列表尾部追加
# li = list([1,3,5,234,123])
# li.append('tomcat')
# print(li)

# 获取指定元素在列表中的位置(从0开始)
# li = list([123,23,1233,432])
# print(li.index(23))
# print(li.index(432))

# 列表跟数组之间的转换
# li = [12,342,123,434]
# print(type(li))
# tu = tuple(li)
# print(type(tu))

# count 统计列表中指定元素的出现次
#li = [1,3,4,5,5,343,23]
#print(li)
#print(li.count(5))


# 统计列表的长度
#print(len(li))

# sort 列表排序
li1 = ['b','c','er','df']
li1.sort()
print(li1)
li1.sort(reverse=True)
print(li1)

# copy 方法
l2 = ['e','f','c','f','d']
print(l2)
l3 = l2.copy()
print(l3)
print(id(l2))
print(id(l3))

lst1 = [1,4,1,2,23,1231,89,34]
print(lst1)

print(lst1[4:-1])
print(lst1[2:])

print(lst1[5:2:-1])

# 从后往前
print(lst1[::-1])


# 对切片赋值，会替换切片原来的元素, 非连续的会抛错。
l4 = list(range(0,10))
print(l4)
## [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l4[3:5] = ['x']
print(l4)
## [0, 1, 2, 'x', 5, 6, 7, 8, 9]

l5 = list(range(0,10))
print(l5)
l5[1:6:2] = ['x','y','z']
print(l5)
## [0, 'x', 2, 'y', 4, 'z', 6, 7, 8, 9]

# 解包是把集合里的元素赋值给变量， 解包就是吧元素一次性赋值给变量
# 解包
x,y = [1,3]
print(x)

# 封包
t = 1, 3
print(t)

x, y = y, x
print(x)
print(y)

head, *tail = list(range(0,10))
print(head)
## 0
print(tail)
## [1, 2, 3, 4, 5, 6, 7, 8, 9]

def it(lst):
    head, *tail = lst
    print(head)
    it(tail)

h, *t = [1, 2]
print(t)

h, *t = [23,34,34]
print(t)
print(h)

head, *mid, tail = [1, 2, 3, 4, 5]
print(head)
print(mid)
print(tail)

lst = list(range(10))
print(lst)
a, b, _, c, *_ = lst
print(lst)
print(a)
print(b)
print(c)

h, *_, t = lst
print(h)
print(t)

lst = [1, [2,3], 4]
a, (b,c), d = lst
print(a)
print(d)

lst = [1,[2,3,4,5,6], 7]
a, (b, *_, c), d= lst
print(a)
print(b)
print(c)
print(d)

a, b, c, _, *_ = [1,2,3,4,5,6]
print(a)
print(b)
print(c)

a, *_, b = [1,2]
print(a)
print(b)