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
hosts = set(user_input.splitlines())

# 我们需要集合运算时

----- 集合的应用



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


