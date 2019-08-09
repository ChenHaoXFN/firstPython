# input 记录键盘录入
num = input("输入您购买的数量:")

price = input("输入单价:")

# 使用 函数 int() 将字符串变成数字
# 使用函数 float() 将字符串变为小数
print("您得支付 ", int(num) * float(price))

