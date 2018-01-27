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

# 切片操作
l3 = [0,1,2,3,4,5,6,7,8,9]
print(l3)
print(l3[2:6:2])
print(l3[::3])