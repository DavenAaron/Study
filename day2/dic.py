######    ----------  集合  ----------    ######
# 元素是唯一 无序的

# 定义空集合
#s = set()
#s1 = {1,2,3}
#print(type(s))
#print(s1)

# s.add() 添加元素， 非重复元素
#s = {1,2,3,4,5}
#print(s)
#s.add(9)
#print(s)

# s.update()
#s = {1,2,3,4,5,6}
#s.update([1,31,9,115,346])
#print(s)
# > {1, 2, 3, 4, 5, 6, 9, 115, 346, 31}

#### 删除 remove,discard,pop,clear ####
s = {1,2,3,4,5,6}

# remove 删除不存在的会抛错，discard则不会
#s.remove(1)
#s.discard(2)
#print(s)
#
## pop 无序的，空集合pop时，抛错
#s = {1,4,32,123,34}
#print(s.pop())
#
## clear 清空
#
##### 修改 （没有一个方法可以直接修改集合中的某个具体元素,因为无法定位某个元素）
#for x in set('wangzenghui'):
#    print(x)
#
#'m' in set('wangm')
#
#####  集合的集合运算  交并差补集合  ####
#a = {1,2,3}
#b = {2,3,4}
#
#print(a.union(b))
#print(a.intersection(b))
#print(a.difference(b))
## 对称差集
#print(a.synmetric_difference(b))

# 超集与子集
a = {1,2,3,4}
b = {3,4}
print(a.issuperset(b))
print(a.issubset(b))

# 判断两个集合是否不相交
print(a.isdisjoint(b))

####  集合的应用 #####

# 元素需要唯一而对顺序没有需求
# hosts = set(user_input.splitlines())

# 我们需要集合运算时

######  字典与字典的增删查改  ####

# 字典声明
d = {'name':'wangzengui','age':'19'}
print(d)
# 设置元素默认值
d.setdefault('from','rizhao')
print(d.get('from'))
print(d['from'])
# 访问字典中的值
print("dname:", d['name'])
# 修改字典(新增/更新)
d['from'] = 'shandong'
d['age'] = 20
print(d)

# ---  字典内置的函数和方法   ----
# 字典元素的个数， 即键的总数
dict1 = {'name': 'wangzenghui','Age':19,'Class':'First'}
print(len(dict1))

# --- 字典包含的内置方法 ---
# 删除字典内的所有元素
dict2 = {'name': 'wangzenghui','Age':19,'Class':'First'}
dict2.clear()
print(dict2)

# 字典的浅复制
dict3 = {'name': 'wangzenghui','Age':19,'Class':'First'}
dict4 = dict3.copy()
print(dict4)

# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print("new dict: %s" % str(dict))
dict = dict.fromkeys(seq, 43)
# - 应用 
print(d.fromkeys([1,2,3], False))
hosts = [1,2,3]
print(dict.fromkeys(hosts, False))

#  以列表返回可遍历的(键, 值) 元组数组
dict = {'name': 'wangzenghui','Age':19,'Class':'First'}
print(dict.items())

# 以列表返回字典所有keys/values
print(dict.keys())
print(dict.values())

# 返回指定键的值，如果值不在字典中返回default值
dict = {'name': 'wangzenghui','Age':19,'Class':'First'}
print(dict.get('name', 'tomcat'))
print(dict.get('from', 'beijing'))

# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict = {'name': 'wangzenghui','Age':19,'Class':'First'}
print(dict.setdefault('name', 'king'))
print(dict.setdefault('from', 'beijing'))
print(dict)

# update() 将字典dict1的键值更新到dict里
dict = {'name': 'wangzenghui','Age':19,'Class':'First'}
dict1.update(dict)
print(dict1)

# pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
dict = {'name': 'wangzenghui','Age':19,'Class':'First'}
print(dict.pop('name'))

# popitem() 随机返回并删除字典中的一对键值（一般是末尾对）
dict = {'name': 'wangzenghui','Age':19,'Class':'First'}
print(dict.popitem())


# dic = {'k1':'v1','k2':'v2'}
# print(dic)
# new_dic = dic.fromkeys(['k1','k2'],'v23')
# print(new_dic)

# dic = {'k1':'v1','k2':'v2'}
# print(dic.get('k1'))
# print(dic.get('k2'))
# print(dic.get('k3'))
# print(dic.get('k3','tomcat'))      # 获取值，如果不存则设置默认值

# print(dic.keys())
# print(dic.values())
# print(dic.items())
#
# for k in dic.keys():
#     print(k)
#
# for v in dic.values():
#     print(v)
#
# for k,v in dic.items():
#     print(k,v)

# 删除指定给定键所对应的值，返回这个值并从字典中把他移除 .pop()
# dic = {'k1':'v1','k2':'v2'}
# dic.pop('k1')
# print(dic)

# 随机删除 .popitem()
# dic = {'k1':'v1','k2':'v2'}
# dic.popitem()
# print(dic)

# 设置key 默认值 .setdefault()
# dic = {'k1':'v1','k2':'v2'}
# dic.setdefault('k4',12312)
# dic['k8'] = 234
# print(dic)

# 字典更新  .update()
# dic = {'k1':'v1','k2':'v2'}
# dic.update({'k2':123123})
# print(dic)

# # 练习题
# dic = {}
# all_list = [11,22,33,44,55,66,77,88,99,101,123]
#
# for i in all_list:
#     if i>66:
#         if 'k1' in dic.keys():
#             dic['k1'].append(i)
#         else:
#             dic['k1'] = [i,]
#     else:
#         if 'k2' in dic.keys():
#             dic['k2'].append(i)
#         else:
#             dic['k2']=[i,]
#
# print(dic)


