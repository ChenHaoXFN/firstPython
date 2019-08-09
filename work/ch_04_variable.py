# 变量
name = "王五"
print(name)

# python 是弱类型语言，可以根据变量自动推断出类型
# int
age = 12
print(age)

# boolean
sex = True

# float
wWeight = 75.5
high = 175.0

# 也可以是用 type 来查看该变量的类型
print(type(sex))
print(type(age))
print(type(high))
# !!--- 在 python3中 没有长整型，全部都是int ---!!

# 单价
price = 3.8
# 数量
weight = 50
money = price * weight
print("总价为", money)
