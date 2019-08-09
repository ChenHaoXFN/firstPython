# 格式化
# 定义name = 小明，输出 我的名字叫 小明 ，请多多关照
name = "小明"
print("我的名字叫", name, "，请多多关照!")
print("我的名字叫 %s %s ，请多多关照!" % (name, name))

# 定义整数 number，输出  我的学号是 0000019
number = 19
print("我的学号是 %06d " % number)

# 定义数量，单价，总价
price = 2.5
weight = 20
print("苹果一斤 %.2f 元，买了 %.2f 斤，一共需要 %.2f 元！" % (price, weight, price * weight))

# 输出百分号
point = 10
print("%.3f%%" % point)
