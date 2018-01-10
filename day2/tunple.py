# 元组是不可变的

t = (1,3,4,234,123,1)
print(t)
print(t[1])

print(t.count(1))
print(len(t))

print(t.index(4))




t1 = (23.4,5,23,234,23,13,53,456)

print(t1[3:5])
lst1 = [23.4,5,23,234,23,13,53,456]
print(lst1[3:5])

lst2 = list(range(0,10))
print(lst2)
lst2[3:5] = ['x']
print(lst2)

# 解包
x, y = [1,3]
print(x)
print(y)

# 封包
t3 = 1, 3
print(type(t3))

