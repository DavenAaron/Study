#####   无序且不重复的元素集合

# s1 = set()
# s1.add('wangzenghui')
# print(s1)

# 将列表转换成无序列表
# print(set(['tomcat','pig','dog','dog']))

# s2 = set(['tomcat','pig','dog','dog','xiao'])
# print(s2)
# s3 = s2.difference(['pig','dog'])
# print(s3)

# s2 = set(['dog','tom','cat','pig'])
# s2.difference_update(['dog','pig'])
# print(s2)

# 随机pop
# s2 = set(['dog','tom','cat','pig'])
# s2.pop()
# print(s2)

# 移除指定集合元素
# s2 = set(['dog','tom','cat','pig'])
# s2.remove('pig')
# print(s2)


# 交集 & 并集
# s1 = set(['tom','cat','big'])
# s2 = set(['big','age'])

# 交集
# print(s1.intersection(s2))

# 并集
# print(s1.symmetric_difference(s2))

# s1 中有，但是s2中没有的
# print(s1.difference(s2))
