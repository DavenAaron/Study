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


