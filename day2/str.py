# unicode 序列， byte序列， 字符串是不可变的

s = 'wangzenghui'
print(s)
print(s[1])

# 字符串连接
help(str.join)

lst = ['my', 'name', 'is ', 'wang']
print(lst)
print(' '.join(lst))
print(','.join(lst))
print('my' + ' name')

# 字符串分割  split rsplit splitlines partition rpartition
s1 = 'my name is wangzenghui'
print(s1.split('is'))
print(s1.split(' ', 1))
print(s1.split(' ',2))
print(s1.split(' ', -1))

print(s1.rsplit(' ',1))

# 反转
print(s[::-1])

h, *_ = s
print(h)
h, _, e, *_ = s
print(e)

s2 = 'my name is zenghui'
print(s2)
print(s2.split(' ',2))

a = 'wangzeng'
b= 'hui'

print(' '.join([a, b]))
## wangzeng hui

url = "url:http://www.zenghui.wang"
print(url)
print(url.split(':',1))
key, value =url.split(':', 1)
print(key)
print(value)

st3 = """i am tom 
how are you
and you
"""
print(st3)

s = "my name is tomcat"
print(s)
print(s.partition(' '))

url = 'url:http://www.zenghui.wang'
print(url.partition(':'))
key, _, value = url.partition(':')
print(key)
print(value)
print(url.split('//'))
a, b = url.split('//')
print(a)
print(b)

s = 'my name is wangzengHUI'
# 大写
print(s.upper())
# 首字母大写
print(s.capitalize())
# 首字母大写
print(s.title())
# 小写
print(s.lower())

# 大小写转化通常用在做比较的时候, 通常同意转化为全部大写或者全部小写在做比较。
print(s.upper().lower())

# 大小写互换
print(s.swapcase())

#####  程序世界的修改 ####
print(s)
help(s.center)
# 填充
print(s.center(80))
#                               my name is wangzengHUI
print(s.center(80, '#'))
#############################my name is wangzengHUI#############################

# 右补全
print(s.ljust(80, '#'))

# 左补全
print(s.rjust(80, '#'))

#  用0来填充
help(s.zfill)
print(s.zfill(80))

help(s.strip)
s = ' hahha nihao \n \t'
print(s.strip())

print(s.lstrip())
print(s.rstrip())

s = '##test##'
print(s.strip('#'))

##############    查找替换     ###########
s = 'my name is tomcat'
# 统计指定字符在字符串中的出现次数
print(s.count('i'))

print(s.find('t'))

print(s.index('t'))

# replace 替换
s = 'abc123abc123'
print(s.replace('abc','ABC'))
print(s.replace('ab','ABC',1))

print(s[1:3])

# 是否包含 __contains__
# name = 'wangzenghui'
# print(name.__contains__('zenghui'))
# print('zenghui' in name)

# 是否相等 __eq__
# name = 'wangzenghui'
# print(name.__eq__(name))

# 反射  __getattribute__

# 首字母大写 capitalize()
# name = 'wangzenghui'
# print(name.capitalize())

# 首字母小写  casefold（）
# name = 'Wangzenghui'
#result = name.casefold()
#print(result)

# wangzenghui居中，其他空格填充满20字符
#name = 'wangzenghui'
#result = name.center(20)
#print(result)

# [****Wangzenghui*****]
#result = name.center(20,'*')
#print(result)

# 查找name变量中n符出现的次数
# name = 'wangzenghui'
# print(name.count('n'))

# 查找name变量中字符n，在第2-5个字符间出现的次数
# name = 'wangzenghui'
# result = name.count('n',2,4)
# print(result)

# 指定字符编码
#name = '王增辉'
#result = name.encode('gbk')
#print(result)

# 判断字符是否以指定字符结尾
# name = 'wangzenghui'
# result = name.endswith('hui')
# print(result)

# 判断指定范围内的字符是否以指定字符结尾
# name = 'Wangzenghui'
# result = name.endswith('g',0,4)
# print(result)

# with 文件操作
# with open('nginx.log', 'wt') as f:
#     f.write('hello, world!')

# 将tab 转换成空格
# name = 'a\tboy'
# result = name.expandtabs()
# #print(len(result))
# print(result)

# 查找指定字符的数量
# name = 'wangzenghui'
# result = name.find('n')
# print(result)

# index 找不到就会抛出异常
# name = 'wangzenghui'
# result = name.index('y')
# print(result)

# 字符串拼接
# name = "tomcat {0} with {1}"
# result = name.format('good','haha')
# print(result)

# 判断字母+数字
# name = 'wangzenghui'
# result = name.isalnum()
# print(result)


# li = ['h','o','w','a','r','e','y','o','u']
# result = "".join(li)
# print(result)

# # 去除左边空格
# name = ' wangzenghui'
# print(name)
# result = name.lstrip()
# print(result)

# name = 'wang zenghui'
# print(name)
# result = name.lstrip('w')
# print(result)

# 以指定的字符为分割点
# name = 'wangzenghui'
# result = name.partition('zeng')
# print(result)

# 字符替换
# name = 'wangzenghui'
# result = name.replace('n','H',1)
# print(result)

#指定分割字符，将字符串分裂成多个字符串组成的列表
# name = 'wangzenghui'
# print(name.split('n'))

# name = """
# wang
# zeng
# hui
# """
# #result = name.splitlines()
# result = name.splitlines()
# print(result)

# 检测字符串是否以指定字符串开头
# name = 'wangzenghui'
# result = name.startswith('wang')
# print(result)

# name = '   tomcat'
# result = name.strip()
# print(result)

# 大小写转换
# name = 'Wang Zenghui'
# result = name.swapcase()
# print(result)

# 连接符 join
# lst = ['my', 'name', 'is', 'tomcat']
# print(' '.join(lst))
# print(','.join(lst))

# a = 'zhang'
# b = 'san'
# print(' '.join([a, b]))

## 每次创建新的对象
# s = ''
# for x in lst:
#     s += ' ' + x
# print(s)

# 字符串的分割
# split，rsplit,splitlines,partition,rpartition

# split 将字符串分割成列表
# s = 'my name is wangzenghui'
# print(s.split())

# 指定默认分割字符为is（从左往右分割）
# s = 'my name is wangzenghui'
# print(s.split('is'))

# 指定分隔符及其分割次数 (分割次数为-1，则分割所有)
# s = 'my name is wangzenghui'
# print(s.split(' ',1))

## --- rsplit   从右往左分割指定次数
# s = 'my name is wangzenghui'
# print(s.rsplit(' ', 1))

# 配置文件中使用示例
# line = 'url:http://zenghui.wang'
# key,value = line.split(':', 1)
# print(key,value)

# splitlines  按行分割
# text = """i am tom
# i am jenk
# i am jenkins
# # """
# print(text.splitlines())
# ## 保留换行符
# print(text.splitlines(True))

# 根据指定的分隔符将字符串进行分割（三部分，分隔符前字符+分隔符+分隔符后字符， 默认分隔符为空格）
# s = 'my name is wangzenghui'
# print(s.partition(' '))

# line = 'url:http://zenghui.wang'
# print(line.partition(':'))
# key, _, value= line.partition(':')
# print(key,value)

# 从右往左方式  rpartition

# ---- 字符填充(左右) ljust & rjust

#满80个字符，不足的以*填充
# s = 'my name is wangzenghui'
# print(s.ljust(80,'*'))
# print(s.rjust(80,'*'))


# ----- strip, lstrip, rstrip
# s = ' haha, how are you? \n \t'
# print(s.strip())

# s = '#### hahaha ####'
# print(s.strip('#'))

# ---- endswith
# s = '####test##'
# print(s.endswith('test',0,8))

# ---- 查找替换
# count, find, rfind, index, rindex, replace
# s = '### test ####'
# print(s.count('#'))
# # 查找元素首次出现的位置
# s.find('e')

# 将指定元素替换成指定元素 n次
# s = 'abc123abc123'
# print(s.replace('abc','xyz'))
# print(s.replace('123','234',1))


# -----  字符格式化
# name = 'wangzenghui'
# message = 'i am %s' % (name,)
# print(message)

# message = 'i am %(name)s' % {'name':'wangzenghui'}
# print(message)

# message = 'i am %(name)s, my name is %(name)s' % {'name': 'wangzenghui'}
# print(message)

# message = 'i am %s, my name is %s' % ('wangzenghui', 'wangzenghui')
# print(message)

## ------------  查找替换 ----------------
# count,find,rfind,index,rindex,replace

# ---- 字符串替换 replace，
# s = '123124sdfasfae'
# print(s.replace('fa','WZ'))

# ---- 统计字符串出现的次数
# s = 'abc234Abcd'
# print(s.count('b'))

# ---- 字符串查找 find,rfind
# s = 'abc234abeab'
# print(s.find('c'))

# s = 'abc234abeab'
# print(s.rfind('a'))

# ---- 替换  replace
# s = 'abc234abeab'
# print(s.replace('abc','ABC'))
#
# # ---- 替换从左往右第一个
# print(s.replace('ab','AB',1))
#
# # ---- 替换所有
# print(s.replace('ab','AB',-1))


# ---------  字符格式化
# name = 'wangzenghui'
# message = 'i am %s' % (name,)
# print(message)

# message = 'i am %(name)s' % {'name':'wangzenghui'}
# print(message)

# message = 'i am %(name)s, my name is %(name)s' % {'name': 'wangzenghui'}
# print(message)

# message = 'i am %s, my name is %s' % ('wangzenghui', 'wangzenghui')
# print(message)

# print('i am %s' % 'tomcat')


# --------- format 方法
# print('i am {}'.format('wangzneghui'))
# print('i am {}, my age is {}'.format('wangzenghui','18'))
# print('i am {1}, my age is {0}'.format(18,'wangzenghui'))
# print('i am {name}, my age is {age}'.format(name='wangzenghui',age=18))
# print('i am {name}, my name is {name}'.format(name='wanzenghui'))

