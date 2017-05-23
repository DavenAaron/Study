'''
all_item = 95
pager = 10
result =  all_item.__divmod__(10)
print(result)

age = 18
result = age.__eq__(19)
print(result)

age = 5
result = age.__floordiv__(6)
print(result)

age = 19
age = int(19)
print(age)
print(type(age))

age = 18
result = age.__add__(7)
result2 = age.__divmod__(7)
print(result)
print(result2)

# 取绝对值
age = -18
resulet = age.__abs__()
print(resulet)

age = 19
result = age.__add__(2)
print(result)
'''

name = 'wangzenghui'

# 获取类
#print(type(name))

# 获取类成员
#print(dir(name))

# name 里是否包含er字符
#result = name.__contains__('er')
#print(result)

# 字符串是否相等
#result1 = name.__eq__('wangzenghui')
#print(result1)


usernames = 'wangzenghhui'
ages = '18'

msg = '''
    name: %s
    ages: %s
''' %(usernames.ages)

print(msg)