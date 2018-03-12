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


# note  基础语法-4 start